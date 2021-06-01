from csvtools import *
import requests 
import re 

rows = readCSVAsList("data.csv")
rows = rows[2:]
rows = [[row[0]] + row[48:58] for row in rows]

total = 0
total2 = 0
total3 = 0

for row in rows:
    lessonId = row[0]
    questionIds = row[1:]

    print("Lesson Id: {}".format(lessonId))

    if questionIds[0] == "":
        print("No ids chosen.")
        continue 

    response = requests.get("http://www.nagwa.com/en/lessons/{}".format(lessonId))

    m = re.search(r"\/worksheets\/([0-9]{12})", response.text)

    if m == None:
        print ("No worksheet found.")
        continue 

    worksheetId = m.group(1)

    print("Worksheet Id: {}".format(worksheetId))

    response = requests.get("http://www.nagwa.com/en/worksheets/{}".format(worksheetId))

    ms = re.findall(r"data\-questionId=\"([0-9]{12})\"", response.text)

    liveQuestionIds = [m for m in ms]

    print(", ".join(sorted(questionIds)))
    print(", ".join(sorted(liveQuestionIds)))
    numberLive = len(set(questionIds).intersection(set(liveQuestionIds)))
    total += numberLive 
    total2 += 10
    total3 += 1 if numberLive == 10 else 0
    print("{}/{}".format(numberLive, len(questionIds)))

print ("Total live that should be: {}/{}".format(total, total2))
print ("Number of lessons with all questions live: {}".format(total3))