import sys
sys.path.append('../')

from utilities import ChatTemplate

sample = '''
To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them. To die—to sleep,
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to: 'tis a consummation
Devoutly to be wish'd. To die, to sleep;
To sleep, perchance to dream—ay, there's the rub:
For in that sleep of death what dreams may come,
When we have shuffled off this mortal coil,
Must give us pause—there's the respect
That makes calamity of so long life.'''

text = "Gallaudet University, federally chartered in 1864, is a bilingual, diverse, multicultural institution of higher education that ensures the intellectual and professional advancement of deaf and hard of hearing individuals through American Sign Language (ASL) and English."

response = ChatTemplate.from_file('rewrite.json').completion({'sample': sample, 'text': text})

print(response.choices[0].message.content)