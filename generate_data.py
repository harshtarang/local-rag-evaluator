from langchain_community.document_loaders import PyPDFLoader
from ragas.testset import TestsetGenerator
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.chat_models import ChatOllama
from ragas.testset.docstore import InMemoryDocumentStore
from ragas.testset.extractor import KeyphraseExtractor
from ragas.run_config import RunConfig
from langchain.text_splitter import TokenTextSplitter
from langchain_community.embeddings import GPT4AllEmbeddings

from ragas.llms import LangchainLLMWrapper
from ragas.embeddings.base import (
    BaseRagasEmbeddings,
    LangchainEmbeddingsWrapper,
    LlamaIndexEmbeddingsWrapper,
)
llm = ChatOllama(model="mistral")
mistral_wrapper = LangchainLLMWrapper(langchain_llm=llm)

loader = PyPDFLoader("C:/Users/harsh/Downloads/UF docs/admissions/UF_Freshman_DatesAndDeadlines.pdf")
documents = loader.load()



# Add custom llms and embeddings
generator_llm = LangchainLLMWrapper(langchain_llm=mistral_wrapper)
critic_llm = LangchainLLMWrapper(langchain_llm=mistral_wrapper)
# embeddings_model = FastEmbedEmbeddings()
fast_embeddings = FastEmbedEmbeddings(model_name="BAAI/bge-base-en")
gpt4all_embd = GPT4AllEmbeddings(model_name = "all-MiniLM-L6-v2.gguf2.f16.gguf")
embeddings= LangchainEmbeddingsWrapper(gpt4all_embd)

splitter = TokenTextSplitter(chunk_size=1024, chunk_overlap=20)
keyphrase_extractor = KeyphraseExtractor(llm=critic_llm)
doc_store = InMemoryDocumentStore(
    splitter=splitter,
    embeddings=embeddings,
    extractor=keyphrase_extractor,
)

# Change resulting question type distribution
testset_distribution = {
    "simple": 0.25,
    "reasoning": 0.5,
    "multi_context": 0.0,
    "conditional": 0.25,
}

# percentage of conversational question
chat_qa = 0.0


dataset_generator = TestsetGenerator.from_langchain(
    generator_llm=llm,
    critic_llm=llm,
    embeddings=embeddings,
    docstore=doc_store,
)


# RunConfig.max_workers=4
test_set = dataset_generator.generate_with_langchain_docs(
    documents=documents,
    test_size=2,
    distributions=testset_distribution,
 #   run_config=RunConfig
)

# test_set = dataset_generator.generate(
#     test_size=2,
#     distributions=testset_distribution,
#  #   run_config=RunConfig
# )

test_df = test_set.to_pandas()
print(test_df.head())