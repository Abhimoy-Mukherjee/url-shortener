from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from .database import Base

class URL(Base):
    __tablename__="urls"
    id=Column(Integer,primary_key=True,index=True)
    short_code=Column(String(10),unique=True,index=True,nullable=False)
    long_url=Column(Text,nullable=False)
    created_at=Column(DateTime,default=datetime.utcnow)