from openai import api_key
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

class Groq:
    def __init__(self):
        load_dotenv()

    def get_llm(self):
        """
        This function returns the llm model
        """
        try:
            os.environ["GROQ_API_KEY"] = self.GROQ_API_KEY = os.getenv("GROQ_API_KEY")
            llm = ChatGroq(
                model = "llama-3.1-8b-instant",
                api_key = self.GROQ_API_KEY
            )
            return llm
        except Exception as e:
            raise ValueError(f"Error occured while getting llm model: {e}")