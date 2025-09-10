from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'Tell me about Jasprit'

embedding=OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)
doc_embedding=embedding.embed_documents(documents)
qry_embedding=embedding.embed_query(query)

score_val=cosine_similarity([qry_embedding],doc_embedding)[0]
print("score=",score_val)
enumerate_value=enumerate(score_val)
print(enumerate_value)
list_val=list(enumerate_value)
sorted_value=sorted(list_val,key=lambda x:x[1])
print("Sorted value =",sorted_value)
index,score=sorted_value[-1]
print(query)
print(documents[index])
print("similarity score is:", score)

