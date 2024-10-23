import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Configurer la clé API OpenAI
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialiser le modèle de langage
llm = ChatOpenAI(api_key=openai_api_key, model="gpt-4", temperature=0)

# Fonction pour interroger GPT
def ask_gpt(question):
    response = llm.invoke(question)
    return response.content

# Demander à GPT "Salut, ça va ?"
question = "Salut, ça va ?"
gpt_response = ask_gpt(question)

# Afficher la réponse
print("Réponse de GPT :", gpt_response)
