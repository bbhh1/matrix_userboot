from sqlalchemy import Column, String, UnicodeText, Integer, desc, delete
from sqlalchemy import asc, desc
import base64
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
badb = base64.b64decode("cG9zdGdyZXM6Ly9taHZlYWZkcTpKSHdwaVJ5cUJ5bG9JcmRsdGRERXRpa3g2TDFNdEVWMUBkdW1iby5kYi5lbGVwaGFudHNxbC5jb20vbWh2ZWFmZHE==")
reda = badb.decode("UTF-8")

BASE = declarative_base()
engine = create_engine(reda, pool_size=5, max_overflow=-1, echo=True)
BASE.metadata.bind = engine
BASE.metadata.create_all(engine)

def close(session, engine):
    """
    ----------
    session : sqlalchemy.orm.sessionmaker.sessionmaker
    engine : sqlalchemy.engine.Engine
    """
    session.expunge_all()
    engine.dispose()



class bankc(BASE):
    __tablename__ = "bank"
    user_id = Column(String(14), primary_key=True)
    first_name = Column(UnicodeText)
    balance = Column(Integer)
    bank = Column(UnicodeText)

    def __init__(self, user_id, first_name, balance, bank):
        self.user_id = str(user_id)
        self.first_name = first_name
        self.balance = int(balance)
        self.bank = bank


bankc.__table__.create(checkfirst=True)


def add_bank(
    user_id,
    first_name,
    balance,
    bank,
):
    
    Session = sessionmaker(bind=engine, autoflush=False)
    session = Session()
    to_check = get_bank(user_id)
    if not to_check:
        user = bankc(str(user_id), first_name, int(balance), bank)
        session.add(user)
        session.commit()
        return True
    user = bankc(str(user_id), first_name, int(balance), bank)
    session.add(user)
    session.commit()
    close(session, engine)
    return True

def update_bank(user_id, money):
    
    Session = sessionmaker(bind=engine, autoflush=False)
    session = Session()
    to_check = get_bank(user_id)
    if not to_check:
        return False
    rem = session.query(bankc).filter(bankc.user_id == int(user_id)).one()
    rem.balance = int(money)
    session.commit()
    close(session, engine)
    return True

def des_bank():
    
    Session = sessionmaker(bind=engine, autoflush=False)
    session = Session()
    ba = session.query(bankc).order_by(desc(bankc.balance)).all()
    close(session, engine)
    return ba

def del_bank(user_id):
    
    Session = sessionmaker(bind=engine, autoflush=False)
    session = Session()
    to_check = get_bank(user_id)
    if not to_check:
        return False
    reda = session.query(bankc).filter(bankc.user_id==str(user_id)).one()
    return reda
    session.delete(reda)
    session.commit()
    close(session, engine)

def get_bank(user_id):
    
    Session = sessionmaker(bind=engine, autoflush=False)
    session = Session()
    try:
        if _result := session.query(bankc).get(str(user_id)):
            return _result
        return None
    finally:
        session.close()
        close(session, engine)

def get_all_bank():
    
    Session = sessionmaker(bind=engine, autoflush=False)
    session = Session()
    try:
        return session.query(bankc).all()
    except BaseException:
        close(session, engine)
        return None
    finally:
        session.close()
        close(session, engine)
