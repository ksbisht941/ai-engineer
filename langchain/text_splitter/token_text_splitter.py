from langchain_text_splitters import TokenTextSplitter
from langchain_community.document_loaders import PyPDFLoader

splitter = TokenTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

loader = PyPDFLoader("documents/GRU.pdf")
document = loader.load()

chunks = splitter.split_documents(document)

print('metadata:', chunks[0].metadata)
print('page_content:', chunks[0].page_content)

# for chunk in chunks:
#     print('metadata:', chunk.metadata)
#     print('page_content:', chunk.page_content)
#     print(' ')