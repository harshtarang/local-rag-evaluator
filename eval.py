from datasets import load_dataset

fiqa_eval = load_dataset("explodinggradients/fiqa", "ragas_eval")
print(fiqa_eval)

from ragas.metrics import (
    answer_relevancy,
    faithfulness,
    context_recall,
    context_precision,
)

from ragas import evaluate
from ragas.llms import LangchainLLMWrapper
from langchain_community.chat_models import ChatOllama

mistral = ChatOllama(model="mistral")
mistral_wrapper = LangchainLLMWrapper(langchain_llm=mistral)

faithfulness.llm = mistral_wrapper

result = evaluate(
    fiqa_eval["baseline"].select(range(3)), # selecting only 3
    metrics=[
        context_precision,
        faithfulness,
        answer_relevancy,
        context_recall,
    ],
)

df = result.to_pandas()
print(df.head())