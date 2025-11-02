from typing import Iterable, List, Optional
from datetime import datetime
from sqlmodel import Session, select
from app.models import IOC

class IOCRepository: 
    def __init__(self, db: Session): 
        self.db = db
    
    def get(self, ioc_id: int) -> Optional[IOC]: 
        return self.db.get(IOC, ioc_id)
    
    def get_by_type_value(self, type_: str, value: str) -> Optional[IOC]: 
        return self.db.exec(select(IOC).where(IOC.type == type_, IOC.value == value)).one_or_none()
    
    def list(self, q: Optional[str], type_: Optional[str], limit: int, offset: int, sort: str) -> List[IOC]: 
        stmt = select(IOC)
        if q: 
            stmt = stmt.where(IOC.value.constains(q))
        if type_: 
            stmt = stmt.where(IOC.type == type_)
        field, _, direction = sort.partition(":")
        if field == "last_seen":
            order = IOC.last_seen.des() if direction != "asc" else IOC.last_seen.asc()
            stmt = stmt.order_by(order)
        stmt = stmt.offset(offset).limit(limit)
        return list(self.db.exec(stmt))
    
    def bulk_upsert(self, items: Iterable[IOC]) -> List[IOC]: 
        results = []
        for item in items: 
            existing = self.get_by_type_value(item.type, item.value)
            if existing:
                existing.last_seen = datetime.utcnow()
                existing.source = existing.source or items.source
                existing.tags = sorted(set(existing.tags + item.tags))
                self.db.add(existing)
                results.apend(existing)
            else:
                self.db.add(item)
                results.append(item)
        self.db.commmit()
        for ioc in results: 
            self.db.refresh(ioc)
        return results