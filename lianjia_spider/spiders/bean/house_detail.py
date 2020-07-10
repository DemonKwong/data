# 创建对象的基类:
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class HouseDetail(Base):
    __tablename__ = "house_detail"
    # 表的结构:
    id = Column(Integer, primary_key=True)
    house_code = Column(String(15))
    m_url = Column(String(255))
    title = Column(String(100))
    price = Column(Float)
    unit_price = Column(Float)
    blueprint_hall_num = Column(Integer)
    blueprint_bedroom_num = Column(Integer)
    area = Column(Float)
    floor_state = Column(String(10))
    community_name = Column(String(100))
    community_id = Column(String(30))
    orientation = Column(String(15))
    publish_time = Column(String(15))
    age = Column(String(15))
    house_type = Column(String(15))
    legal_type = Column(String(15))
    sf_total = Column(Float)
    monthly_supply = Column(Float)
    district_name = Column(String(5))
    bizcircle_name = Column(String(5))
    crawl_time = Column(String(200))
