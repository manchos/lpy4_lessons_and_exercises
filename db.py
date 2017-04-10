from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///files//blog.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(120), unique=True)
    posts = relationship('Post', backref='author')

    def __init__(self, first_name=None, last_name=None, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
            # self.posts = posts

    def __repr__(self):
        return '<User {} {}>'.format(self.first_name, self.last_name)


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(140))
    image = Column(String(500))
    published = Column(DateTime)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __init__(self, title=None, image=None, published=None, content=None, user_id=None):
        self.title = title
        self.image = image
        self.published = published
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return '<Post {}>'.format(self.title)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
