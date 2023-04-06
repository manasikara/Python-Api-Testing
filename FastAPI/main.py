# the lesson source --> https://www.youtube.com/watch?v=0sOvCWFmrtA
# docs --> https://fastapi.tiangolo.com/tutorial/first-steps/
# host --> http://127.0.0.1:8000
# auto-reload --> uvicorn main:app --reload

from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
def root():
    return {"message": "this is a get command"}


@app.get("/posts")
def get_posts():
    return {"data": "These are posts"}

 
@app.post("/createpost")
def pocre_posts(new_post: Post):
    print(new_post.title)
    print(new_post.content)
    print(new_post.published)
    print(new_post.rating)
    return {"data": "new post"}
# https://youtu.be/0sOvCWFmrtA?t=4470


# in continuous, gradual development... ¯\_( ͡° ͜ʖ ͡°)_/¯
