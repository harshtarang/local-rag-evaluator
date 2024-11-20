import json
import pandas as pd
from datasets import Dataset 

def clean_answer_text(ans: str) -> str:
    return ans.replace("\n", "\\n")

model = "mistral"
prompt = "basic"
num_chunks = 7
with open(f"answers/rag/{model}/answers_{prompt}_{num_chunks}.json", "r") as f:
    qna = json.load(f)
print(qna)


df = pd.read_json("ground_truth_final.json")
# print(df.head())
answers = qna["answers"]
contexts = qna["contexts"]
print(answers)


df['contexts'] = contexts
df['answer'] = answers

print(df.head())

df.to_json(f"answers/rag/{model}/evaluation_{prompt}_{num_chunks}.json")