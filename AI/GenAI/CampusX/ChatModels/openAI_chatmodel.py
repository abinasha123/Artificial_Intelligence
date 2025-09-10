from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
result=ChatOpenAI(model='gpt-4.1',max_completion_tokens=20,temperature=1)

output=result.invoke("capital of South Africa in 3 word")
print(output.content)