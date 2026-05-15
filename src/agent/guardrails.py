FORBIDDEN_TERMS = [
    "garantia de lucro",
    "retorno garantido"
]


def validate_response(response):

    for term in FORBIDDEN_TERMS:
        if term in response.lower():
            return "Não posso fornecer esse tipo de recomendação."

    return response