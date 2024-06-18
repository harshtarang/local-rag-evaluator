# Generate Synthetic Test Set for RAGAs Evaluation
## Load documents
### Deps
from langchain.document_loaders import DirectoryLoader
### Loading
loader = DirectoryLoader("C:/Users/harsh/Downloads/UF docs/v3/") # input_path defined in project setup
documents = loader.load()
## Update metadata
### Encapsulate
def update_metadata():
  for document in documents:
      document.metadata['filename'] = document.metadata['source']
### Run
update_metadata()
## Build Models for use in generator
### Deps
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import TokenTextSplitter
from ragas.testset.extractor import KeyphraseExtractor
from ragas.testset.docstore import InMemoryDocumentStore

### Build
mistral = ChatOllama(model="mistral")
llama3 = ChatOllama(model="llama3:8b")
embeddings = OllamaEmbeddings(model="mistral")
keyphrase_extractor = KeyphraseExtractor(llm=mistral)
splitter = TokenTextSplitter(chunk_size=2500, chunk_overlap=100)
## Generate Test Set
### Deps
from ragas.testset.generator import TestsetGenerator
from ragas.testset.evolutions import simple, reasoning, multi_context
### Generate
generator = TestsetGenerator.from_langchain(
    generator_llm=mistral,
    critic_llm=llama3,
    embeddings=embeddings,
)

testset = generator.generate_with_langchain_docs(documents, test_size=20, raise_exceptions=False, with_debugging_logs=True, distributions={simple: 1.0, reasoning: 0.0, multi_context: 0.0})
df = testset.to_pandas()

df.dropna()
df.to_csv("ground_truth_admissions_v3.csv")