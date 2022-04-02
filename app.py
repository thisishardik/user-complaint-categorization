import nltk
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import yake
import logging

from flask import Flask, request, jsonify
# from flask_cors import CORS

from helpers.category import fetch_categories_map
from helpers.yake import keyword_extraction_yake, sentence_tokenizer, generate_kw_info_from_kw_snt

nltk.download('punkt')

app = Flask(__name__)
# cors = CORS(app)

# app.config['CORS_HEADERS'] = 'Content-Type'


def cos_sim_vectors(vec1, vec2):
    vec1 = vec1.reshape(1, -1)
    vec2 = vec2.reshape(1, -1)
    return cosine_similarity(vec1, vec2)[0][0]


def cos_similarity(category_info):
    max_sim_category = ""
    sim = 0
    max_sim = 0

    categories_map = fetch_categories_map()
    similarity_vector = []

    for key, value in categories_map.items():
        text = [value, category_info]
        vectorizer = CountVectorizer().fit_transform(text)
        vectors = vectorizer.toarray()

        sim = cos_sim_vectors(vectors[0], vectors[1]) * 100
        similarity_vector.append(sim)

        if sim > max_sim:
            max_sim = sim
            max_sim_category = key

    return max_sim, max_sim_category


@app.route("/classify", methods=["GET"])
def classify():

    args = request.args
    query = args.get("query")

    kw_sent, kw_lst = keyword_extraction_yake(query)
    kw_sent = sentence_tokenizer(kw_lst)
    category_info = generate_kw_info_from_kw_snt(kw_sent)

    max_sim, max_sim_category = cos_similarity(category_info)

    return {
        "category": f"{max_sim_category}",
        "similarity_value": f"{max_sim}",
        "status": 200,
    }


if __name__ == "__main__":
    app.run()
