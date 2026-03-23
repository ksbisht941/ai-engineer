from langchain_community.document_loaders import WebBaseLoader

url = "https://en.wikipedia.org/wiki/Recurrent_neural_network"

loader = WebBaseLoader(url)

document = loader.load()

print('metadata:', document[0].metadata)
print(' ')
print('page_content:', document[0].page_content)