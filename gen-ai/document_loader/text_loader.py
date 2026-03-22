from langchain_community.document_loaders import TextLoader

loader = TextLoader("documents/notes.txt")
document = loader.load()

print('metadata:', document[0].metadata)
print(' ')
print('page_content:', document[0].page_content)