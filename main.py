import csv
import json



csvFilePath = "\sample.csv"
jsonFilePath = "csvToJSON\myJsons\Test"
jsonExtension = ".json"


# read data from the CSV file
count = 1
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        newJsonPath = jsonFilePath + str(count) + jsonExtension
        jsonFile = open(newJsonPath, "w", encoding='utf-8')  # write data in JSON file with Greek charachters in different JSON files
        jsonFile.write(json.dumps(csvRow, indent=4, ensure_ascii=False))  # indent=4 to make it human readable
        jsonFile.close()
        count += 1


