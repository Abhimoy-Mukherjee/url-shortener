import random
import string
from sqlalchemy.orm import Session
from .models import URL

def generate_short_code(length=6):
    characters=string.ascii_letters+string.digits
    return "".join(random.choices(characters,k=length))

def create_short_url(db:Session,long_url:str):
    short_code=generate_short_code()
    while db.query(URL).filter(URL.short_code==short_code).first():
        short_code=generate_short_code()

    url=URL(short_code=short_code,long_url=long_url)
    db.add(url)
    db.commit()
    db.refresh(url)
    return url
          