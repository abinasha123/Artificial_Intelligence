from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
documents=[
    "Virat kohli is a good batsman",
    "Bumra is a good bowler",
    "Ravindra jadeja is a good all rounder"
]
embedding=OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)
result=embedding.embed_documents(documents)
print(result)