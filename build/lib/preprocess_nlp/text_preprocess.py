import spacy 
import os 
import json 

fpath=os.path.join(os.path.dirname(__file__),'data/contractions.json')
contractions=json.load(open(fpath))

def word_count(text):
    return len(text.split())
    