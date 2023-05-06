from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float, Text, Date, Time, Table


class Movies(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    overview = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    category = Column(String(100), nullable=False)
