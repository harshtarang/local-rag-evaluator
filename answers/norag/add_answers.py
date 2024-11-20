import json
import pandas as pd
from datasets import Dataset 

def clean_answer_text(ans: str) -> str:
    return ans.replace("\n", "\\n")

model = "mistral"
with open(f"answers/norag/answers_{model}.json", "r") as f:
    qna = json.load(f)
# print(qna)

df = pd.read_json("ground_truth_final.json")
# print(df.head())
answers = list(qna.values())
print(answers)

# # print(len(df))
# # print(len(answers))

question_df = df.loc[:, ['question']]

df = df.assign(answer='')

i=0
for idx, q in question_df.iterrows():
    # print(f"Index: {idx}, Q: {q['question']}")
    df.at[idx, 'answer'] = clean_answer_text(answers[i])
    i +=1
    # df.at[idx, 'contexts'] = ['No context']

print(df.head())

df.to_json("answers/norag/mistral7b.json")