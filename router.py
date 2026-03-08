import streamlit as st
from openai import OpenAI

from model_fetcher import get_free_models
from health_check import check_model_health


class SmartLLMRouter:

    def __init__(self):

        models = get_free_models()[:1]

        self.available_models = []

        for m in models:

            try:

                result = check_model_health(m)

                if result["healthy"]:

                    self.available_models.append(m)

            except Exception as e:

                print(e)
                break


    # -------------------------
    # SMART ROUTING
    # -------------------------

    def ask(self, prompt):

        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=st.secrets["OPENROUTER_API_KEY"]
        )

        for model in self.available_models:

            try:

                print("Trying", model)

                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=300
                )

                return response.choices[0].message.content

            except Exception as e:

                print(e)
                continue

        return "All models failed."


    # -------------------------
    # SPECIFIC MODEL CALL
    # -------------------------

    def ask_with_specific_model(self, prompt, model):

        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=st.secrets["OPENROUTER_API_KEY"]
        )

        print(f"Using selected model → {model}")

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )

        return response.choices[0].message.content
