import sys
sys.path.append('../')

from utilities import ChatTemplate, get_embedding, cosine_distance
import json

embeddings = json.load(open('embeddings.json', 'r'))

# Given an embedding, iterates over the embeddings in our dataset and returns the nearest key. 
# In this case, the key is the path to the file.
def nearest_embedding(embedding):
    # Initialize variables to store the nearest embedding's path and its distance.
    # Start with `None` for the nearest path and set the nearest distance to 1, assuming 
    # the distance is normalized between 0 and 1, where 1 means completely dissimilar.
    nearest, nearest_distance = None, 1

    # Iterate over each path and embedding vector in the global 'embeddings' dictionary.
    for path, embedding2 in embeddings.items():
        # Calculate the cosine distance between the current embedding and 
        # the embedding from the dictionary.
        distance = cosine_distance(embedding, embedding2)
        
        # If this distance is the smallest so far, update 'nearest' and 'nearest_distance'
        # with the current path and distance. This means we found a closer embedding.
        if distance < nearest_distance:
            nearest, nearest_distance = path, distance

    # After checking all embeddings, return the path to the nearest one.
    return nearest


chat = ChatTemplate(
    {'messages': [{'role': 'system', 'content': 'You are a Q&A AI.'},
                  {'role': 'system', 'content': 'Here are some facts that can help you answer the following question: {{data}}'},
                  {'role': 'user', 'content': '{{prompt}}'}]})


while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    # 1. We take an input question from the user as prompt, 
    # 2. We call get_embedding() to get the embedding of the question, and 
    # 3. find the nearest embedding in our memory. 
    #       That is the data that’s most closely related to the question. 
    # 4. nearest_embedding() gives us the path to the file, so we open the file and read it into data.
    context = nearest_embedding(get_embedding(prompt))
    data = open(context, 'r').read()

    message = chat.completion(
        {'data': data, 'prompt': prompt}).choices[0].message

    print(f'{message.role}: {message.content}')