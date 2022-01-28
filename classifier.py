import pandas as pd
import numpy as np

from pathlib import Path
import matplotlib.pyplot as plt
import os
import json

def pre_process(fid=None):
    fid = Path(fid)
    df = pd.read_csv('gender-classifier-DFE-791531.csv',  encoding='latin-1')
    girls_tweets = df[df['gender']=='female'][['text','gender']]
    boys_tweets =  df[df['gender']=='male'][['text','gender']]
    df = pd.concat([girls_tweets,boys_tweets])
    df['binary'] = pd.get_dummies(df.gender, prefix='gender')['gender_female']
    df = df[['text','gender']]
    plt.bar(['women','men'],height=np.bincount(df['binary']))

    train = df.sample(frac=0.8,random_state=43)
    test = df.drop(train.index)
    valid = train.sample(frac=0.1, random_state=43)
    train = train.drop(valid.index)

    train.to_csv('gender_text_train.csv', mode='w', index=False)
    test.to_csv('gender_text_test.csv', mode='w', index=False)
    valid.to_csv('gender_text_valid.csv', mode='w', index=False)
    
def train_hf_api(args):

    if args.login:
        sub_args = ('autonlp login --api-key  ')
        os.system(sub_args+args.api_key)
    
    if args.send:
        sub_args = f'autonlp upload '
        sub_args+= f' --project {args.project}'
        sub_args+= f' --split {args.split}'
        sub_args+= f' --col_mapping {args.col_mapping}'
        sub_args+= f' --files {args.files}'
        os.system(sub_args)
        
        
    if args.make:
        sub_args = f'autonlp create_project '
        sub_args+= f' --name {args.name}'
        sub_args+= f' --language {args.language}'
        sub_args+= f' --task {args.task}'
        sub_args+= f' --max_models {args.max_models}'
        os.system(sub_args)

    if args.train:
        sub_args = f'autonlp train '
        sub_args+= f' --project {args.project}'
        os.system(sub_args)

def inference(json_fid=None):
    with open(json_fid,'r') as fid:
        text_dict = json.load(json_fid)
        
    # load some model eg. model = torch.loadstatedict(model.pth)
    # for key in text_dict:
    #    prediction = model.predict(text_dict[key])
    #    text_dict[pred_gender]=prediction
    # json.dump(text_dict)
    # 
        
