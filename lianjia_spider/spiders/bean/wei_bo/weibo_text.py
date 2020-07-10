# 创建对象的基类:
from sqlalchemy import Column, Integer, String, create_engine, TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WeiboText(Base):
    __tablename__ = "weibo_text"
    # 表的结构:
    id = Column(Integer, primary_key=True, comment="主键")
    user_id = Column(String(10), comment="博主id")
    name = Column(String(255), comment="博主名称")
    item_id = Column(String(255), comment="微博id")
    text = Column(TEXT(), comment="微博文本")
    publish_time = Column(String(200), comment="发博时间")
    crawl_time = Column(String(200), comment="爬虫时间")

# engine = create_engine('mysql+mysqlconnector://root:kjw123456@47.115.40.104:13306/spider')
# WeiboText.metadata.create_all(engine)