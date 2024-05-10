import os
import glob
import PyPDF2
from docx import Document
import json

def count_word_occurrences_in_file(filePath, words):
    wordCount = {word: 0 for word in words}
    file_extension = os.path.splitext(filePath)[1]

    if file_extension == '.pdf':
        with open(filePath, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page in pdf_reader.pages:
                text = page.extract_text()
                for word in words:
                    wordCount[word] += text.lower().count(word.lower())

    elif file_extension == '.docx':
        doc = Document(filePath)
        for paragraph in doc.paragraphs:
            for word in words:
                wordCount[word] += paragraph.text.lower().count(word.lower())

    return wordCount

def count_word_occurrences_in_directory(directoryPath, words):
    files = glob.glob(os.path.join(directoryPath, '*'))
    totalFiles = len(files)
    thisData = {}
    for filePath in files:
        if os.path.isfile(filePath):
            # print(f"File: {filePath}")
            wordCount = count_word_occurrences_in_file(filePath, words)
            matchCount = 0
            tempSum = 0
            currentText = {}
            for word, count in wordCount.items():
                tempSum+=count
                if count > 0: matchCount+=1
                currentText[word] = {"Count": count}
            if tempSum in thisData: thisData[tempSum][filePath] = currentText
            else: thisData[tempSum] = {filePath: currentText}
            thisData[tempSum]["MatchCount"] = matchCount
    sortedData = dict(sorted(thisData.items(), key=lambda x: int(x[0]), reverse=True))
    return sortedData


if __name__ == "__main__":
    directoryPath = 'C:/Users/midhdesk1/Desktop/RoziRoti/devopsResume/'
    # words_input = input("Enter comma-separated words: ")
    words_input = "azure, devops, pipeline, devops pipeline"
    words = [word.strip() for word in words_input.split(',')]
    jsonData = count_word_occurrences_in_directory(directoryPath, words)
    jsonFilePath = 'resumeResult.json'
    with open(jsonFilePath, 'w') as json_file:
        json.dump(jsonData, json_file)
    print(f"Sorted data saved to {jsonFilePath}")
