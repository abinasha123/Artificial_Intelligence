from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()
model=ChatOpenAI()
class Review(TypedDict):
    summary:str
    sentiment:str

structured_model=model.with_structured_output(Review) 
str="""Yes, a chatbot created in Python can be effectively integrated with a React frontend. This is a common and robust approach for building modern web applications with AI capabilities."""   
result=structured_model.invoke(str)
print(result)
print(result['summary'])
print(result['sentiment'])

