from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('RAGBasesApplication/dl-curriculum.pdf')
docs=loader.load()
print(len(docs))
print(docs[0].page_content)