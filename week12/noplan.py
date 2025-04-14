import sys
sys.path.append('../')

from utilities import ChatTemplate

chat = ChatTemplate({
    'messages': [{'role': 'user', 'content': 'Write a short 3 chapter sci-fi novella on the theme of AI ethics.'}]})

print(chat.completion({}).choices[0].message.content)