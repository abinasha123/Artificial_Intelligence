from langchain_community.document_loaders import TextLoader

loader=TextLoader('RAGBasesApplication/cricket.txt',encoding='utf-8')
docs=loader.load()
print(docs[0])