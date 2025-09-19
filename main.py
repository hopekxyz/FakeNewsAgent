import requests
from env_variables import OPENAI_API_KEY, GOOGLE_API_KEY
import os

ENDPOINT = "https://factchecktools.googleapis.com/v1alpha1/claims:search"

pesquisa = input("Digite o que deseja buscar: ")

params = {
    "query": pesquisa,   # termo que você quer checar
    "languageCode": "pt-BR",
    "pageSize": 5,
    "key": GOOGLE_API_KEY
}

response = requests.get(ENDPOINT, params = params)
data = response.json()
for claim in data.get("claims"):
    print("-----------------------------------")
    print(f'Afirmação: {claim.get("text")}')
    print(f'Fonte: {claim.get("claimReview")[0].get("url")}')
    print(f'Avaliação: {claim.get("claimReview")[0].get("textualRating")}')
    print("-----------------------------------\n")

