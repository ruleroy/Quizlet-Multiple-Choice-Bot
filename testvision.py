import io
import os
import bot
import re
import multiprocessing

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = './My Project-d4d2015265d9.json'

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
#print(res)

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

question = text[0].description.replace('"', '').replace("'", '')
re.escape(question)
question = question.split("\n")

index = 0
for q in question:
    if(q.find("Prize for this question:") != -1):
        break
    index += 1

option = question[index:-1]
question = question[0:index]

question = " ".join(question)
print(question)

if len(option) > 1:
    options['A'] = option[1]
if len(option) > 2:
    options['B'] = option[2]
if len(option) > 3:
    options['C'] = option[3]
if len(option) > 4:
    options['D'] = option[4]

print("\nOPTIONS:")

options['A'] = options['A'].replace('\n', '').replace("BC", "B.C.").replace("AD", "A.D.")
options['B'] = options['B'].replace('\n', '').replace("BC", "B.C.").replace("AD", "A.D.")
options['C'] = options['C'].replace('\n', '').replace("BC", "B.C.").replace("AD", "A.D.")
options['D'] = options['D'].replace('\n', '').replace("BC", "B.C.").replace("AD", "A.D.")

for o in options:
    options[o] = options[o]
    if options[o]:
        print(f"{o}.{options[o]}")

if __name__ == "__main__":
    bot.getAnswer(question, options['A'], options['B'], options['C'], options['D'])