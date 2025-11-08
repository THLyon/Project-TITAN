from typing import Iterable, List, Optional, Tuple
from datetime import datetime
from sqlmodel import Session, select
from sqlalchemy import asc, desc
from app.models import IOC

class IOCRepository:
    def __init__(self, db: Session):
        self.db = db

    def get(self, ioc_id: int) -> Optional[IOC]:
        return self.db.get(IOC, ioc_id)

    def get_by_type_value(self, type_: str, value: str) -> Optional[IOC]:
        stmt = select(IOC).where(IOC.type == type_, IOC.value == value)
        return self.db.exec(stmt).one_or_none()

    def _parse_sort(self, sort: str) -> Tuple[str, bool]:
        field, _, direction = (sort or "").partition(":")
        field = field or "last_seen"
        direction = (direction or "desc").lower()
        is_asc = direction == "asc"
        return field, is_asc

    def list(
        self,
        q: Optional[str],
        type_: Optional[str],
        limit: int,
        offset: int,
        sort: str
    ) -> List[IOC]:
        stmt = select(IOC)

        if q:
            stmt = stmt.where(IOC.value.contains(q))  # SQLAlchemy compiles this safely
        if type_:
            stmt = stmt.where(IOC.type == type_)

        field, is_asc = self._parse_sort(sort)
        if field == "last_seen":
            order_col = IOC.last_seen.asc() if is_asc else IOC.last_seen.desc()
            stmt = stmt.order_by(order_col)
        else:
            # Fallback order to stable, recent-first listing
            stmt = stmt.order_by(IOC.last_seen.desc())

        stmt = stmt.offset(offset).limit(limit)
        return list(self.db.exec(stmt))

    def bulk_upsert(self, items: Iterable[IOC]) -> List[IOC]:
        results: List[IOC] = []
        for item in items:
            existing = self.get_by_type_value(item.type, item.value)
            if existing:
                existing.last_seen = datetime.utcnow()
                # keep original source if present, otherwise take incoming
                existing.source = existing.source or item.source
                # guard against None and de-dup tags
                existing_tags = existing.tags or []
                incoming_tags = item.tags or []
                existing.tags = sorted(set(existing_tags + incoming_tags))
                self.db.add(existing)
                results.append(existing)
            else:
                # ensure tags isn’t None
                if item.tags is None:
                    item.tags = []
                self.db.add(item)
                results.append(item)

        self.db.commit()
        for ioc in results:
            self.db.refresh(ioc)
        return results
