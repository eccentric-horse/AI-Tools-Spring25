import openai
import os

import sys
sys.path.append('../')

from utilities import ChatTemplate

guide = '''
You are a large language model trained on vast amounts of data.
You respond to questions based on the data you were trained on.
When you do not have enough information to provide an accurate answer, you will say so.
'''

question = 'Tell me about the habitat and behavior of the flying blizzard fish.'

chat = ChatTemplate({
    'messages': [{'role': 'user', 'content': guide + question}]})

print(chat.completion({}).choices[0].message.content)