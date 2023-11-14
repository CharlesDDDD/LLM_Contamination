import pandas as pd
def prepare_mmlu():
    data = pd.read_csv("/home/yz979/chunyuan/QA/MMLU/data/mc1.csv")
    return data['slot_question'].values
    print(data['slot_question'])
def prepare_truthfulqa():
    data = pd.read_csv("/home/yz979/chunyuan/QA/TruthfulQA/data/fill_in_mc1.csv")
    return data['question'].values

