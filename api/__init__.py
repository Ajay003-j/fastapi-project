from fastapi import FastAPI
import psycopg2.extras
import psycopg2
from api import modele
from api.database import engine
from psycopg2.extras import RealDictCursor
from api.route import user,books,auth

modele.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(books.router)
app.include_router(auth.router)

while True:

    try:

        conn = psycopg2.connect(
            host='localhost',
            port=5432,
            user='postgres',
            password='Ajay2004',
            database='api_db',
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        break

    except Exception as e:

        print(f"Database connection error: {e}")