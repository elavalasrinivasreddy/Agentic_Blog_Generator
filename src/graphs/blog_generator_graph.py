from langgraph.graph import StateGraph, START, END
from src.states.blog_generator_state import BlogState
from src.llms.groq import Groq
from src.nodes.blog_generator_node import BlogNode

class AgenticBlogGraph:
    def __init__(self):
        self.llm = Groq().get_llm()
        self.graph = StateGraph(BlogState)

    def build_graph(self):
        """
        Build the graph to generate the blog content on user given topic
        """

        self.blog_node = BlogNode(self.llm)
        # Nodes
        self.graph.add_node("title_generator",self.blog_node.title_generator)
        self.graph.add_node("content_generator",self.blog_node.content_generator)

        # Edges
        self.graph.add_edge(START, "title_generator")
        self.graph.add_edge("title_generator", "content_generator")
        self.graph.add_edge("content_generator", END)

        return self.graph.compile()

# Below code for langsmith debugging purpose
graph = AgenticBlogGraph().build_graph()