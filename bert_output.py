import pandas as pd
import numpy as np
from func_mode import mode
# from bert_train import SentimentAnalysis_Dataset

def bert_out():
    godjj = pd.read_csv("bert_1_prec_training_samples.csv")
    
    df = godjj["Category"].tolist()
    
    # df = [-1.0, -1.0, 0.0, 0.0, 1.0, 1.0]
    
    
    SENTIMENT_SCORE = mode(df)
    
    SENTIMENT_SCORE.sort()
    

    
    if(len(SENTIMENT_SCORE) > 1):
    	if(SENTIMENT_SCORE == [-1.0, 0.0]):
    		SENTIMENT_SCORE = [-1.0]
    	if(SENTIMENT_SCORE == [0.0, 1.0]):
    		SENTIMENT_SCORE = [1.0]
    	if(SENTIMENT_SCORE == [-1.0, 1.0]):
    		SENTIMENT_SCORE = [0.0]
    	if(SENTIMENT_SCORE == [-1.0, 0.0, 1.0]):
    		SENTIMENT_SCORE = [0.0]
    		

    return(SENTIMENT_SCORE)