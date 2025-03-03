import sys
sys.path.append('../')

from utilities import ChatTemplate

#.from_file(prompt template)
#.completion(user input prompt)
response = ChatTemplate.from_file(
    'translate.json').completion({'text': "Live long and prosper!"})

print(response.choices[0].message.content)