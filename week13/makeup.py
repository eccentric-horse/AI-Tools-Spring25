import sys
sys.path.append('../')

from utilities import ChatTemplate

chat = ChatTemplate({
    'messages': [{'role': 'user', 'content': 'Tell me about the habitat and behavior of the flying blizzard fish.'}]})

print(chat.completion({}).choices[0].message.content)