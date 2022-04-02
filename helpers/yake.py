import nltk
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import yake

# print(ENGLISH_STOP_WORDS)

def keyword_extraction_yake(sentence):
    kw_extractor = yake.KeywordExtractor(lan='en')
    keywords = kw_extractor.extract_keywords(sentence)
    kw_sent = ""
    kw_lst = []

    for word, acc in keywords:
        kw_sent += word + " "
        kw_lst.append(word)

    return kw_sent, kw_lst

def sentence_tokenizer(sentence):
    tokenizer = RegexpTokenizer('\w+')
    temp = []
    tokenized_data = []
    
    for i in sentence:
        temp = tokenizer.tokenize(i)
        snt_wo_stpwords = [w for w in temp if w not in ENGLISH_STOP_WORDS]
        tokens = [w.lower() for w in snt_wo_stpwords]
        tokenized_data.append(tokens)

    return tokenized_data

def generate_kw_info_from_kw_snt(kw_sent):
    '''
    Generating categories info using only keywords
    '''
    category_info = ""

    for lst_of_keywords in kw_sent:
        for word in lst_of_keywords:
            if word not in category_info:
                category_info += word + " "
    return category_info