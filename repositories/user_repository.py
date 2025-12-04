# repository.py: This file contains the database repository for the application
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import User

class UserRepository:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    
    def get_user(self, user_id):
        return self.session.query(User).filter(User.id == user_id).first()
    
    def create_user(self, user):
        self.session.add(user)
        self.session.commit()
        return user
