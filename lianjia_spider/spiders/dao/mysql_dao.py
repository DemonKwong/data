from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class MysqlDAO:
    def __init__(self):
        #self.engine = create_engine('mysql+mysqlconnector://root:kjw123456@47.115.40.104:3306/spider')
        self.engine = create_engine('mysql+mysqlconnector://root:kjw123456@47.115.40.104:13306/spider?charset=utf8mb4')

    def save(self, object):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        session.add(object)
        session.commit()
        session.close()

    def select_one(self, item_id, type):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        result = session.query(type).filter(type.item_id == item_id).first()
        session.commit()
        session.close()
        return result

    def update_one(self, type, item_id, text):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        session.query(type).filter(type.item_id == item_id).update({"text": text})
        session.commit()
        session.close()
