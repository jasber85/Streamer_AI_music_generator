# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 16:16:04 2022

@author: jasbe
"""
import numpy as np
import random
import torch
from torch.utils.data import DataLoader, Dataset 
from transformers import AdamW, BertForQuestionAnswering, BertTokenizerFast, BertForSequenceClassification
from tqdm.auto import tqdm
import pandas as pd
from torch.nn.utils.rnn import pad_sequence
import os
from berttest import get_predictions,SentimentAnalysis_Dataset,tokenizer,create_mini_batch,PRETRAINED_MODEL_NAME,NUM_LABELS
import statistics
from bert_output import bert_out


filepath = "Chatmodel.pt"

model = BertForSequenceClassification.from_pretrained(
    PRETRAINED_MODEL_NAME, num_labels=NUM_LABELS)

if os.path.exists(filepath):
    try:

        model.load_state_dict(torch.load(filepath))
        print("checkpoint loaded")
    
    except:

        os.remove(filepath)
        print("checkpoint deleted")

def Sentiment_Analysis():
    godjj_test=pd.read_csv("msg.csv",encoding="unicode_escape")
    godjj_test.to_csv("msg.tsv", sep="\t", index=False)
    testset = SentimentAnalysis_Dataset('test', tokenizer=tokenizer,DATASET='msg.tsv')
    testloader = DataLoader(testset, batch_size=256, 
                            collate_fn=create_mini_batch)
    predictions = get_predictions(model, testloader)
    
    # 生成 Kaggle 繳交檔案
    df = pd.DataFrame({"Category": predictions.tolist()})
    df_pred = pd.concat([testset.df.loc[:, ["index"]], testset.df.loc[:, ["user"]], testset.df.loc[:, ["msg"]], 
                              df.loc[:, 'Category']], axis=1)
    df_pred.to_csv('bert_1_prec_training_samples.csv', index=False,encoding='UTF-8')
    a = bert_out()
    if a[0] == 0:
        print('negative')
    elif a[0] == 1:
        print('neutral')
    elif a[0] == 2:
        print('positive')
    return a
# 0:負面 1:中立 2:正面 