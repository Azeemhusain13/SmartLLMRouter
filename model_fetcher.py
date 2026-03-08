import requests

OPENROUTER_MODELS_URL = "https://openrouter.ai/api/v1/models"


def get_free_models():

    response = requests.get(OPENROUTER_MODELS_URL)

    data = response.json()

    free_models = []

    for model in data["data"]:

        model_id = model["id"]

        if ":free" in model_id:
            free_models.append(model_id)

    return free_models