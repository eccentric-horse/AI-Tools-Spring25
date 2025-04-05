import json
import os
import sys

# Import our APIs
from mock_API import get_emails, schedule_meeting, process_function_call

# Change working directory so files can 
# be found when debugging
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("..")

from utilities import ChatTemplate


chat = ChatTemplate.from_file('presonal_assistant_english.json')

while True:
    prompt = input('> ')
    if prompt == 'exit':
        break

    chat.template['messages'].append({'role': 'user', 'content': prompt})

    while True:
        message = chat.completion({}).choices[0].message
        chat.template['messages'].append(
            {'role': message.role, 'content': message.content})
        
        if 'get_emails' in message.content or 'schedule_meeting' in message.content:
            function_call = json.loads(message.content)
            result = process_function_call(function_call)
            chat.template['messages'].append(
                {'role': 'user', 'name': function_call['name'], 'content': json.dumps(result)})
        else:
            break

    print(message.content)