import win32clipboard
import pprint
import bot
import keyboard #Using module keyboard
import sys

import pyperclip

recent_value = ""
print('Waiting for CTRL+C...')
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.CloseClipboard()

def runText():
    # get clipboard data
    win32clipboard.OpenClipboard()
    clipdata = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    clipdata = clipdata.strip()
    #clipdata = clipdata.rstrip()

    clipdata = clipdata.splitlines()
    clipdata = list(filter(None, clipdata))
    #print(clipdata)
    #pprint.pprint(clipdata)

    question = ''
    options = {
        'A': '',
        'B': '',
        'C': '',
        'D': ''
    }

    #print(clipdata)

    if any("A. play Play" in s for s in clipdata):
        clipdata.remove('A. play Play')
        clipdata.remove('Discover Music player')
    if any("B. play Play" in s for s in clipdata):
        clipdata.remove('B. play Play')
        clipdata.remove('Discover Music player')
    if any("C. play Play" in s for s in clipdata):
        clipdata.remove('C. play Play')
        clipdata.remove('Discover Music player')
    if any("D. play Play" in s for s in clipdata):
        clipdata.remove('D. play Play')
        clipdata.remove('Discover Music player')
    if any("play Play" in s for s in clipdata):
        clipdata.remove('play Play')
        clipdata.remove('Discover Music player')

    question = clipdata[0]

    print("\nQUESTION:")
    print(question)

    if len(clipdata) > 1:
        options['A'] = clipdata[1]
    if len(clipdata) > 2:
        options['B'] = clipdata[2]
    if len(clipdata) > 3:
        options['C'] = clipdata[3]
    if len(clipdata) > 4:
        options['D'] = clipdata[4]

    print("\nOPTIONS:")
    for o in options:
        options[o] = options[o].replace('Answer', '')
        if options[o]:
            print(f"{o}.{options[o]}")

    bot.getAnswer(question, options['A'], options['B'], options['C'], options['D'])

while True:
    try: 
        tmp_value = pyperclip.paste()
        if keyboard.is_pressed('ctrl+c'):
            if tmp_value != recent_value:
                recent_value = tmp_value
                runText()
        if keyboard.is_pressed('ctrl+q'):
            print('Exiting...')
            sys.exit()
        else:
            pass
    except:
        break 