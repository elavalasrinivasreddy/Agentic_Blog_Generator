from src.states.blog_generator_state import BlogState

class BlogNode:
    def __init__(self,llm):
        self.llm = llm

    def title_generator(self,state:BlogState):
        """
        This function generates the title for the blog based on user topic
        """
        try:
            prompt = f"""
            Generate a catchy and relevant title for a blog post about {state['topic']} in language {state['language']}.
            The title should be engaging and suitable for a general audience.
            Return only the title, without any additional text in markdown format.
            """
            response = self.llm.invoke(prompt)
            return {"blog": {"title":response.content}}
        except Exception as e:
            raise ValueError(f"Error occured while generating title: {e}")
        
    def content_generator(self,state:BlogState):
        """
        This function generates the content for the blog based on user topic and title  
        """
        try:
            prompt = f"""
            Generate a catchy and relevant content for a blog post about {state['topic']} in langauge {state['language']} for the title {state['blog']['title']}.
            The content should be engaging and suitable for given title.
            Return only the content, without any additional text(including title) in markdown format.
            """
            response = self.llm.invoke(prompt)
            return {"blog": {"title":state['blog']['title'],"content":response.content}}
        except Exception as e:
            raise ValueError(f"Error occured while generating content: {e}")