from fastapi import FastAPI,HTTPException,status
from api.route import to_do,post,auth
from api import modele,dependancy
app = FastAPI()

app.include_router(to_do.router,prefix="/signin")
app.include_router(post.router,prefix="/posts")
app.include_router(auth.route)

modele.Base.metadata.create_all(bind=dependancy.engine)

