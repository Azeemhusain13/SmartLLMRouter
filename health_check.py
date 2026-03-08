import time
from openai import OpenAI
import os
import streamlit as st

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENROUTER_API_KEY"]
)


def check_model_health(model):

    try:

        start = time.time()

        client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": "hello"}
            ],
            max_tokens=5
        )

        latency = time.time() - start

        return {
            "model": model,
            "healthy": True,
            "latency": latency
        }

    except Exception as e:

        print(f"{model} unhealthy:", e)

        return {
            "model": model,
            "healthy": False,
            "latency": 999
        }
