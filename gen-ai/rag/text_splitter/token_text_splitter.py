from langchain_text_splitters import TokenTextSplitter
from langchain_text_splitters import CharacterTextSplitter
from langchain_text_splitters import TextSplitter
from langchain_community.document_loaders import TextLoader

splitter = TokenTextSplitter(
    separator="",
    chunk_size=10,
    chunk_overlap=2,
)

loader = TextLoader("documents/notes.txt")
document = loader.load()

chunks = splitter.split_documents(document)

for chunk in chunks:
    print('metadata:', chunk.metadata)
    print('page_content:', chunk.page_content)
    print(' ')