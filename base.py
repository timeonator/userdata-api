import sqlalchemy
import os
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)

    def __init__(self, name):      
        self.name = name

basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tapes.db')
url = 'sqlite:///' + os.path.join(basedir, 'user.db')
engine = sqlalchemy.create_engine(url)
session = sqlalchemy.orm.scoped_session(sqlalchemy.orm.sessionmaker())
session.configure(bind=engine, autoflush=False, expire_on_commit=False)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
u = User('Bob')
session.add(u)
u=User('Margret')
session.add(u)
session.commit()
