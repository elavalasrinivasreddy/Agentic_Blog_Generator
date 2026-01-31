from sphinx.search import languages
from typing_extensions import TypedDict
from pydantic import BaseModel, Field

class Blog(BaseModel):
    title: str = Field(description="The title of the blog.")
    content: str = Field(description="The main content of the blog.")

class BlogState(TypedDict):
    topic: str
    blog: Blog
    language: str