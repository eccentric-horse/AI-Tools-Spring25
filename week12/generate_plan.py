import sys
sys.path.append('../')

from utilities import ChatTemplate

chat = ChatTemplate({
    'messages': [{'role': 'system', 'content': 'Your goal is to write a short 3 chapter sci-fi novella on the theme of AI ethics. Come up with 7 steps that will help you achieve the goal. Output these steps as a JSON array of large language model prompts. Note: you need to come up with 7 steps, and each step should start with "Step number". For example, "Step 1: Brainstorm ideas for the plot and characters of the science fiction novella focusing on AI ethics."'}]})

print(chat.completion({}).choices[0].message.content)