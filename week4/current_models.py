from openai import OpenAI
import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

models = client.models.list().data
for model in models:
    print(model.id)