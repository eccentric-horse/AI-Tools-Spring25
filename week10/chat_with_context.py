import sys
sys.path.append('../')

from utilities import ChatTemplate, count_tokens

chat = ChatTemplate(
    {'messages': [{'role': 'system', 'content': 'You are an AI chat program.'},
                  {'role': 'user', 'content': '{{prompt}}'}]})

TOKEN_LIMIT = 500

while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    # store the user prompt to memory as history / context
    chat.template['messages'].append({'role': 'user', 'content': prompt})
    
    print(count_tokens(chat.template['messages']))
    while count_tokens(chat.template['messages']) > TOKEN_LIMIT:
       chat.template['messages'].pop(0)

    # call the model with the user prompt
    #   note that the model is already pre-loaded with our chat template
    message = chat.completion({'prompt': prompt}).choices[0].message

    print(f'{message.role}: {message.content}')
    # store the model response to memory as history / context
    chat.template['messages'].append({'role': message.role, 'content': message.content})