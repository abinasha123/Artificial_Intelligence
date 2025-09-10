import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN")
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    #task="conversational",
    task="text-generation",
    #huggingfacehub_api_token=api_key
)
get_model=ChatHuggingFace(llm=llm)
result=get_model=ChatHuggingFace(llm=llm).invoke("What is the capital of India")
print(result.content)