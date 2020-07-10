# 创建对象的基类:
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WeiboPicture(Base):
    __tablename__ = "weibo_picture"
    # 表的结构:
    id = Column(Integer, primary_key=True, comment="主键")
    item_id = Column(String(255), comment="微博id")
    pic_url = Column(String(255), comment="配图链接")
    crawl_time = Column(String(200), comment="爬虫时间")
