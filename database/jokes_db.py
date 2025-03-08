from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Joke(Base):
    __tablename__ = 'jokes'
    
    id = Column(Integer, primary_key=True)
    category = Column(String(50))
    text = Column(Text)
    context = Column(String(100))
    rating = Column(Integer, default=0)

class JokesDatabase:
    def __init__(self):
        self.engine = create_engine('sqlite:///jokes.db')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    
    def add_joke(self, category: str, text: str, context: str) -> None:
        """Добавление новой шутки в базу данных"""
        joke = Joke(category=category, text=text, context=context)
        self.session.add(joke)
        self.session.commit()
    
    def get_joke_by_context(self, context: str) -> str:
        """Получение шутки по контексту"""
        joke = self.session.query(Joke).filter_by(context=context).first()
        return joke.text if joke else None
    
    def update_rating(self, joke_id: int, rating: int) -> None:
        """Обновление рейтинга шутки"""
        joke = self.session.query(Joke).get(joke_id)
        if joke:
            joke.rating = rating
            self.session.commit()
    
    def get_top_jokes(self, limit: int = 10) -> list:
        """Получение топ шуток по рейтингу"""
        return self.session.query(Joke).order_by(Joke.rating.desc()).limit(limit).all() 