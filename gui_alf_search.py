import requests
from requests.auth import HTTPBasicAuth

# Configuration Alfresco
alfresco_url = "http://localhost:8080/alfresco/api/-default-/public/search/versions/1/search"
username = "admin"
password = "admin"  # Remplacez par votre mot de passe

# Fonction pour rechercher des documents
def search_documents(keyword):
    headers = {
        "Content-Type": "application/json"
    }

    # Requête de recherche : utilisez CMIS pour rechercher par texte ou métadonnées
    query = {
        "query": {
            "query": f"cm:name:*{keyword}* OR cm:title:*{keyword}*"
        },
        "include": ["properties"]
    }

    # Envoi de la requête POST pour la recherche
    response = requests.post(alfresco_url, auth=HTTPBasicAuth(username, password), headers=headers, json=query)

    # Traitement de la réponse
    if response.status_code == 200:
        data = response.json()
        print(f"Résultats de recherche pour '{keyword}':")
        for entry in data['list']['entries']:
            doc_name = entry['entry']['name']
            doc_title = entry['entry'].get('title', 'Sans titre')
            doc_id = entry['entry']['id']
            print(f"Nom : {doc_name}, Titre : {doc_title}, ID : {doc_id}")
    else:
        print(f"Erreur {response.status_code}: {response.text}")

# Exemple d'utilisation
keyword = input("Entrez un mot-clé pour la recherche : ")
search_documents(keyword)
