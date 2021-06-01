import csv


def getIdFromCSVText(text):
    return text[2:-1]


def readCSVAsList(fileName):
    rows = []

    with open(fileName, "r") as fileObject:
        csvReader = csv.reader(fileObject)

        for row in csvReader:
            rows.append(row)

    return removeBlankRows(rows)


def writeListAsCSV(list, fileName):
    with open(fileName, "w") as fileObject:
        csvWriter = csv.writer(fileObject)

        for row in list:
            csvWriter.writerow(row)


def removeBlankRows(list):
    return [r for r in list if len(r) > 0]


def printList(list):
    for r in list:
        print (r)
