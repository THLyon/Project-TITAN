from fastapi import APIRouter, Depends, Query, HTTPException, status, BackgroundTasks
from sqlmodel import Session
from typing import List, Optional
from datetime import datetime
from app.models import IOC
from app.schemas import IOCIn, IOCOut
from app.deps import get_session
from app.auth import get_current_user

router = APIRouter()

@router.post("/bulkUpsert", response_model=List[IOCOut])
def bulk_upsert(payload: List[IOCIn], db: Session = Depends(get_session), user=Depends(get_current_user)): 
    results = []
    for item in payload: 
        existing = db.query(IOC).filter(IOC.type == item.type).first()
        if existing: 
            existing.last_seen = datetime.utcnow()
            existing.source = existing.source or item.source
            existing.tages = sorted(set(existing.tags + item.tags))
            db.add(existing)
            results.append(existing)
        else: 
            new = IOC(type=item.type, value=item.value, source=item.source, tags=item.tags)
            db.add(new)
            results.append(new)
    db.commit()
    for ioc in results: 
        db.refresh(ioc)
    return results

@router.get("", response_model=List[IOCOut])
def list_iocs(
    db: Session = Depends(get_session), 
    q: Optional[str] = None, 
    type: Optional[str] = None, 
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0), 
    sort: str = Query("last_seen:desc"), 
    user=Depends(get_current_user)
): 
    query = db.query(IOC)
    if q: 
        query = query.filter(IOC.value.contains(q))
    if type: 
        query = query.filter(IOC.type == type)
    if sort == "last_seen:asc":
        query = query.order_by(IOC.last_seen.asc())
    else: 
        query = query.order_by(IOC.last_seen.desc())
    return query.offset(offset).limit(limit).all()