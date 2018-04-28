import io
import os
import bot
import re

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ''

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'resources/question.png')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
#response = client.label_detection(image=image)
#labels = response.label_annotations

#text detection
res = client.document_text_detection(image=image)
text = res.text_annotations

'''
print('Labels:')
for label in labels:
    print(label.description)
'''
question = ''
options = {
    'A': '',
    'B': '',
    'C': '',
    'D': ''
}

print("QUESTION:")

question = text[0].description.replace('"', '')
re.escape(question)
question = re.split(r'[?:]+', question)
#question = text[0].description.replace('"', '').split(':')[0]
#question = text[0].description.replace('"', '').split('?')[0]


question = question[0].replace("\n", '')
print(question)

'''
print('\n')
print(text[0].description)
print('\n')
'''

option = text[0].description.replace('"', '').replace('D Play\n', '').replace('Play\n', '')
option = re.split(r'[O+]+', option)

print(option)

if len(option) > 1:
    options['A'] = option[1]
if len(option) > 2:
    options['B'] = option[2]
if len(option) > 3:
    options['C'] = option[3]
if len(option) > 4:
    options['D'] = option[4]

print("\nOPTIONS:")

options['A'] = options['A'].replace('\n', '').replace('O ', '')
options['B'] = options['B'].replace('\n', '').replace('O ', '')
options['C'] = options['C'].replace('\n', '').replace('O ', '')
options['D'] = options['D'].replace('\n', '').replace('O ', '')

for o in options:
    options[o] = options[o].replace('Answer', '')
    if options[o]:
        print(f"{o}.{options[o]}")


bot.getAnswer(question, options['A'], options['B'], options['C'], options['D'])