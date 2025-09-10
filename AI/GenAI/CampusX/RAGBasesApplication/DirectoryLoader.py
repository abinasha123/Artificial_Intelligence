from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader

loader=DirectoryLoader(
    path='RAGBasesApplication/book',
    glob='*pdf',
    loader_cls=PyPDFLoader
)
docs=loader.load()
print(len(docs))
print(docs[1])
