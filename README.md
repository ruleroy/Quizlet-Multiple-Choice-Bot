# Quizlet-Multiple-Choice-Bot
Answers multiple choice questions built in Python using Google Custom Search API. Specifically made for my Music Appreciation course for research purposes. :)

### How it works:
Script takes in three possible ways of input:
1. Command line arguments
2. OCR
3. Clipboard

It reads and formats the input data to perform a google search for the question on Quizlet using Google Custom Search API. bot.py grabs the snippet output from each API result and does a word count for each multiple choice options. The option with the highest word count is chosen as the best answer. With this method, I was able to obtain 100% scores on my quizes. 

## Command line Arguments
```
python bot.py -q "Question" -a "Option A" -b "Option B" -c "Option C" -d "Option D"
```

## OCR
Reads a screenshot image of the question and possible solutions then converts it into a legible format to feed into bot.py script for analysis.
Works but is unreliable and has issues formatting different types of screenshots sometimes.
```
python vision.py
```

## Clipboard
Most reliable method to grab data for formatting. Highlight and copy the question and answers with CTRL+C and it will automatically read your clipboard to feed parameters into bot.py.
```
python text.py
```

### Small Demo:
![alt text](https://i.gyazo.com/00c4104477619efeb28a7efe0749bbce.gif)
