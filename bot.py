import sys
import getopt
import re
import pprint
import time

from googleapiclient.discovery import build

service = build("customsearch", "v1",
            developerKey="")


def main(argv):
    start_time = time.time()
    question = ''
    option = { 'A': '', 'B': '', 'C': '', 'D': '' }
    try:
        opts, args = getopt.getopt(argv, "hq:a:b:c:d:", [
                                   "quest=", "optA=", "optB=", "optC=", "optD="])
    except getopt.GetoptError:
        print(
            "bot.py -q <Question> -a <option a> -b <option b> -c <option c> -d <option d>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
                'bot.py -q <Question> -a <option a> -b <option b> -c <option c> -d <option d>')
            sys.exit()
        elif opt in ("-q", "--quest"):
            question = arg
        elif opt in ("-a", "--optA"):
            option['A'] = arg
        elif opt in ("-b", "--optB"):
            option['B'] = arg
        elif opt in ("-c", "--optC"):
            option['C'] = arg
        elif opt in ("-d", "--optD"):
            option['D'] = arg

    #snip = ['TEST test test TeSt \n', 'tesT2 dfsa \n yea']
    snip = []

    res = service.cse().list(
      q=question,
      cx='002207493689593174907:bt1hj9c-_2w',
      num='9'
    ).execute()

    for s in res['items']:
        snip.append(s['snippet'])



    for x in range(len(snip)):
        snip[x] = snip[x].replace('\n', '')
    
    occur = { 'A': 0, 'B': 0, 'C': 0, 'D': 0 }

    #pprint.pprint(res)
    #pprint.pprint(snip)

    for i in snip:
        if(option['A']):
            occur['A'] += i.upper().count(option['A'].upper())
        if(option['B']):
            occur['B'] += i.upper().count(option['B'].upper())
        if(option['C']):
            occur['C'] += i.upper().count(option['C'].upper())
        if(option['D']):
            occur['D'] += i.upper().count(option['D'].upper())

    if(option['A']):
        print(f"A Score: {occur['A']}")
    if(option['B']):
        print(f"B Score: {occur['B']}")
    if(option['C']):
        print(f"C Score: {occur['C']}")
    if(option['D']):
        print(f"D Score: {occur['D']}")

    print(f"\nBEST ANSWER: {keywithmaxval(occur)}. {option[keywithmaxval(occur)]}")

    print("\n--- Finished in %s seconds ---" % (time.time() - start_time))

def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

def getAnswer(q, a, b, c, d):
    start_time = time.time()
    question = q
    option = { 'A': a, 'B': b, 'C': c, 'D': d }

    snip = []

    res = service.cse().list(
      q=question,
      #exactTerms=question,
      cx='002207493689593174907:bt1hj9c-_2w',
      num='9'
    ).execute()

    #pprint.pprint(res)
    for s in res['items']:
        snip.append(s['snippet'])

    for x in range(len(snip)):
        snip[x] = snip[x].replace('\n', '')
    
    occur = { 'A': 0, 'B': 0, 'C': 0, 'D': 0 }

    for i in snip:
        if(option['A']):
            occur['A'] += i.upper().count(option['A'].upper())
        if(option['B']):
            occur['B'] += i.upper().count(option['B'].upper())
        if(option['C']):
            occur['C'] += i.upper().count(option['C'].upper())
        if(option['D']):
            occur['D'] += i.upper().count(option['D'].upper())

    if(option['A']):
        print(f"\nA Score: {occur['A']}")
    if(option['B']):
        print(f"B Score: {occur['B']}")
    if(option['C']):
        print(f"C Score: {occur['C']}")
    if(option['D']):
        print(f"D Score: {occur['D']}")

    print(f"\nBEST ANSWER: {keywithmaxval(occur)}. {option[keywithmaxval(occur)]}")

    print("\n--- Finished in %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main(sys.argv[1:])
