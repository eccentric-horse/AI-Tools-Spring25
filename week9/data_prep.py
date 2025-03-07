import sys
sys.path.append('../')

from utilities import ChatTemplate
import os

folder_name = '../dailymoth'
output_file = 'dailymoth_output.jsonl'

template = ChatTemplate.from_file('jsonl.json')
jsonl = ''

for f in os.listdir(folder_name):
    # Open each file in read mode with utf-8 encoding, ignoring errors
    with open(os.path.join(folder_name, f), 'r', encoding="utf-8", errors="ignore") as f:
        # Read the content of the file and store it in the variable `text`
        text = f.read()

    # Pass the text content to a template for processing and store the response
    #   each completion makes 20 prompts
    response = template.completion({'info': text, 'n': '20'})
    # Extract the processed text from the response, 
    #   remove leading/trailing whitespace, and append it to a JSONL string
    jsonl += response.choices[0].message.content.strip() + '\n'

with open(output_file, 'w+') as f:
    f.write(jsonl)