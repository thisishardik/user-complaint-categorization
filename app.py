import nltk
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import yake

from flask import Flask, request, jsonify

from helpers.category import fetch_categories_map
from helpers.yake import keyword_extraction_yake, sentence_tokenizer, generate_kw_info_from_kw_snt

nltk.download('punkt')

app = Flask(__name__)


def cos_similarity(Y):
    l1 = []
    l2 = []

    max_sim_category = ""
    max_sim = 0

    categories_map = fetch_categories_map()

    for key, value in categories_map.items():
        X = value
        X = {x for x in X}
        Y = {y for y in Y}
        rvector = X.union(Y)
        for w in rvector:
            if w in X:
                l1.append(1)
            else:
                l1.append(0)
            if w in Y:
                l2.append(1)
            else:
                l2.append(0)
        c = 0

        for i in range(len(rvector)):
            c += l1[i]*l2[i]
        cosine = c / float((sum(l1)*sum(l2))**0.5)

        if cosine > max_sim:
            max_sim = cosine
            max_sim_category = key

    return max_sim, max_sim_category


@app.route("/classify", methods=["GET"])
def classify():

    args = request.args
    query = args.get("query")

    kw_sent, kw_lst = keyword_extraction_yake(query)
    kw_sent = sentence_tokenizer(kw_sent)

    max_sim, max_sim_category = cos_similarity(query)

    return {
        "category": f"{max_sim_category}",
        "similarity_value": f"{max_sim}",
        "status": 200,
    }


if __name__ == "__main__":
    app.run()
