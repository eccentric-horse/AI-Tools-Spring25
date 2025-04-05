import chromadb
from chromadb.utils import embedding_functions
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

# Create a new database client
# We want the data to be persisted
client = chromadb.PersistentClient(path="dailymothdb_backup")

collection = client.create_collection(
    'dailymoth',
    embedding_function=embedding_functions.OpenAIEmbeddingFunction(
        api_key=os.environ.get("OPENAI_API_KEY"),
        model_name="text-embedding-3-small"
    ))

filepath = '../dailymoth'

# Load the signlanguages files to the database we just initiated
for f in os.listdir(filepath):
    path = os.path.join(filepath, f)
    with open(path, 'r', encoding="utf8", errors='ignore') as f:
        text = f.read()

    text = text.replace('\n', ' ')

    collection.add(documents=[text], ids=[path])