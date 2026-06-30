from langchain_ollama import ChatOllama
from config.settings import settings

def get_ollama_llm()-> ChatOllama:
    return ChatOllama(
        model=settings.model,
        temperature=0
    ) 
