import uvicorn
from fastapi import FastAPI, Request
from src.graphs.blog_generator_graph import AgenticBlogGraph
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

@app.post("/blog_content")
async def blog_content(request: Request):
    """
    This function calls the blog generation graph by providing user topic and language.
    """
    try:
        request_body = await request.json()
        topic = request_body.get("topic")
        language = request_body.get("language")
        if topic:   
            blog_generator = AgenticBlogGraph()
            graph = blog_generator.build_graph()
            result = graph.invoke({"topic": topic, "language":language})
            return {"data":result,"status":200,"message":"Blog content generated successfully"}
        else:
            return {"data":None,"status":400,"message":"Topic is required"}
    except Exception as e:
        raise ValueError(f"Error occured while generating blog content: {e}")

if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8000,reload=True) 