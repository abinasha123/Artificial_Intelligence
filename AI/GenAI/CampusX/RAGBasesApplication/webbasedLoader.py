from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model='gpt-4.1')
loader=WebBaseLoader('https://www.amazon.in/Whirlpool-Refrigerator-205-WDE-CLS/dp/B0BSRVL2VV/ref=sr_1_2?_encoding=UTF8&content-id=amzn1.sym.58c90a12-100b-4a2f-8e15-7c06f1abe2be&dib=eyJ2IjoiMSJ9.WeNO08BDbM9HwjBZfrKHXUMi1QQo22id3_xnDyYQ-fHSXfW9SLcuvC0j-TC3VP3tvlW2cys_zgNJ45Uyko1MftFdC4qqa89k-5pFvOXydCQsghMiVfbT4SeOG5oAgfttSxCUOBJsbKuXMIywoHwDDGLpgYRmzIlxWrJzne7WW-LhxK_wCbu6S9fdF9vSzTVN4_nHDwhQDMQTYsHbeOOnKrTPpp9P27s9N-Ry7Ix31cX9NWe_wqcVmN0rGuChZXCuow_y5qE5Twr7bxVWkceFsattyhlPLh5iiRePI95BNHU.k8pEsdTNIypoNtC2-Vl8970_Z8LrtA5eqJ09rZuePwc&dib_tag=se&pd_rd_r=33c6b665-5169-4af2-a142-a65fc1195938&pd_rd_w=MSkGJ&pd_rd_wg=C49Nu&qid=1757492169&refinements=p_85%3A10440599031&rps=1&s=kitchen&sr=1-2&th=1')
page_content=loader.load()
prompt = f"""
Use the following context to answer the question.

Context:
{page_content}

Question: Which Model is this. Describe in 2 lines?
"""

result=model.invoke(prompt)
print(result.content)
#print(docs)