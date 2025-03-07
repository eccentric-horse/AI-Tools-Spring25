import openai
from dotenv import load_dotenv

load_dotenv()

model_name = 'ft:gpt-4o-2024-08-06:personal::B8FSnK8v'

template = '''You are a Q&A bot. You provide short answers to questions.
For example:
Question: What does ASL stand for? American Sign Language.
Provide the answer to the following question:
Question: '''

while True:
    prompt = input('user: ')
    if prompt == 'exit':
        break

    message = [{'role': 'user', 'content': template + prompt}]

    response = openai.chat.completions.create(
        model = model_name,
        temperature = 0,
        stop = ['\n'],
        messages = message)

    print("assistant: " + response.choices[0].message.content)