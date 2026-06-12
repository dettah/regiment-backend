import requests

NLP_API_URL = "https://thetaom-regment-bot.hf.space/chat"

def ask_nlp(message):

    try:

        response = requests.post(
            NLP_API_URL,
            json={
                "message": message
            },
            timeout=20
        )

        response.raise_for_status()

        return response.json()

    except Exception as e:

        return {
            "response": "AI service unavailable.",
            "error": str(e)
        }