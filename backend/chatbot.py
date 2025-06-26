import os
import requests
from dotenv import load_dotenv

load_dotenv()

openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
def ask_openai(question):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {openrouter_api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "Tu es un assistant intelligent qui répond en français."},
            {"role": "user", "content": question}
        ],
        "max_tokens": 1500,
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        data = response.json()

        # debug
        #print("Réponse API complète:", data)

        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"].strip()
        else:
            return "Réponse inattendue de l'API OpenRouter."
    except Exception as e:
        print(f"Erreur OpenRouter: {e}")
        return "Désolé, je n'arrive pas à répondre pour le moment."


def main():
    print("Assistant OpenRouter prêt. Tape 'exit' pour quitter.")
    while True:
        user_input = input("Vous: ").strip()
        if user_input.lower() in ["exit", "quit", "stop"]:
            print("Assistant arrêté.")
            break
        response = ask_openai(user_input)
        print("Assistant:", response)

if __name__ == "__main__":
    main()
