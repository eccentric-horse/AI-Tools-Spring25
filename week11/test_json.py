import json
import os
import sys

# Change working directory so files can 
# be found when debugging
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("..")

from utilities import ChatTemplate


def get_emails(names):
    print(f'* Getting emails for {names}')

    address_book = {
        'Spock': 'spock@example.com',
        'Picard': 'picard@example.com',
        'Kirk': 'kirk@example.com',
        'Sisko': 'sisko@example.com'
    }
    emails = {}

    for name in names:
        emails[name] = address_book[name]

    return emails


def schedule_meeting(subject, recipients, time):
    print(f"* Meeting '{subject}' scheduled for {time} with {recipients}")
    return {'success': True}


# Note: when using JSON for function calls, use this API
def process_function_call(function_call):
    name = function_call.name
    args = json.loads(function_call.arguments)

    functions = {
        'get_emails': get_emails,
        'schedule_meeting': schedule_meeting,
    }

    return functions[name](**args)

# ---------------------- END OF API -------------------------

chat = ChatTemplate.from_file('personal_assistant_json.json')

while True:
    prompt = input('> ')
    if prompt == 'exit':
        break

    chat.template['messages'].append({'role': 'user', 'content': prompt})

    while True:
        message = chat.completion({}).choices[0].message

        if message.function_call != None:
            result = process_function_call(message.function_call)
            chat.template['messages'].append(
                {'role': 'function', 'name': message.function_call.name, 'content': json.dumps(result)})
        else:
            break

    print(message.content)
    chat.template['messages'].append(
        {'role': message.role, 'content': message.content})