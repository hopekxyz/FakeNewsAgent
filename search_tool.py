import requests
from env_variables import OPENAI_API_KEY, GOOGLE_API_KEY
from langchain.agents import tool
import os


ENDPOINT = "https://factchecktools.googleapis.com/v1alpha1/claims:search"

@tool
def search(topic: str) -> dict:
    """Recebe uma busca como entrada e retorna um dicionário com o status da requisição com os dados, incluindo uma Afirmação,
    Fonte e Avaliação, a partir da API da Google usando FactCheck."""
    try:
        params = {
            "query": topic,
            "languageCode": "pt-BR",
            "pageSize": 5,
            "key": GOOGLE_API_KEY
        }
        response = requests.get(ENDPOINT, params = params)
        data = response.json()

    except Exception as error:
        return f'Error: {error}'
    
    return {
        'status' : 'success',
        'data' : data
        }

