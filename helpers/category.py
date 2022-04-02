from helpers.yake import keyword_extraction_yake, sentence_tokenizer, generate_kw_info_from_kw_snt
from .config import CATEGORIES, CATEGORIES_MAP


def fetch_categories_map():

    categories = CATEGORIES

    categories_map = CATEGORIES_MAP

    category_info = ""

    for key, value in categories_map.items():
        category_info = ""
        _, kw_lst = keyword_extraction_yake(value)
        kw_sent = sentence_tokenizer(kw_lst)
        category_info = generate_kw_info_from_kw_snt(kw_sent)
        categories_map[key] = category_info

    return categories_map
