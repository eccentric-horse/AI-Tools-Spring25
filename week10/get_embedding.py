import openai

def get_embedding(text):
    return openai.embeddings.create(
        input=[text.replace('\n', ' ')],
        model='text-embedding-3-small').data[0].embedding
    
print(get_embedding("cat"))