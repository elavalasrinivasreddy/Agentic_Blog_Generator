from langgraph.graph import StateGraph, START, END
from src.states.blog_generator_state import Blog_State
from src.llms.groq import groq_model

class agentic_blog_graph:
    def __init__(self,llm):
        self.llm = llm
        self.graph = StateGraph(Blog_State)

    def build_graph(self):
        """
        Build the graph to generate the blog content on user given topic
        """

        # Nodes
        self.graph.add_node("title_generator",)
        self.graph.add_node("content_generator",)

        # Edges
        self.graph.add_edge(START, "title_generator")
        self.graph.add_edge("title_generator", "content_generator")
        self.graph.add_edge("content_generator", END)

        return self.graph.compile()