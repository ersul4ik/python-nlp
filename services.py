from nltk.tokenize import RegexpTokenizer


def get_words(text: str):
    tokenizer = RegexpTokenizer(r'\w+')
    return tokenizer.tokenize(text)


def company_helper(company) -> dict:
    return {
        "id": str(company["_id"]),
        "fullname": company["company_name"],
        "key_points": company["description_key_words"],
    }
