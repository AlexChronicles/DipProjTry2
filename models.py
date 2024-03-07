from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from db_conf import Base

class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    FIO = Column(String)
    time_stamp = Column(DateTime(timezone=True), server_default=func.now())