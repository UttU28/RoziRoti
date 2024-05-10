import os
import glob
import PyPDF2
from docx import Document

def count_word_occurrences_in_file(file_path, words):
    word_count = {word: 0 for word in words}
    file_extension = os.path.splitext(file_path)[1]

    if file_extension == '.pdf':
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page in pdf_reader.pages:
                text = page.extract_text()
                for word in words:
                    word_count[word] += text.lower().count(word.lower())

    elif file_extension == '.docx':
        doc = Document(file_path)
        for paragraph in doc.paragraphs:
            for word in words:
                word_count[word] += paragraph.text.lower().count(word.lower())

    return word_count

def count_word_occurrences_in_directory(directory_path, words):
    files = glob.glob(os.path.join(directory_path, '*'))
    totalFiles = len(files)
    thisData = {}
    for file_path in files:
        if os.path.isfile(file_path):
            # print(f"File: {file_path}")
            word_count = count_word_occurrences_in_file(file_path, words)
            matchCount = 0
            tempSum = 0
            currentTexts = []
            for word, count in word_count.items():
                if count > 0:
                    currentText = f"Word: {word}, Count: \033[1;32m{count}\033[0m"
                    tempSum+=count
                    matchCount+=1
                    currentTexts.append(currentText)
                else:
                    currentText = f"Word: {word}, Count: {count}"
                    currentTexts.append(currentText)
                # print(currentText)
            tempSumS = str(tempSum)
            if tempSumS in thisData: thisData[tempSumS][file_path.split("\\")[-1]] = currentTexts
            else: thisData[tempSumS] = {file_path.split("\\")[-1]: currentTexts}
            # print("Temp Sum:", f"\033[1;32m{tempSum}\033[0m" if tempSum > 0 else "N/A")
    sorted_data = dict(sorted(thisData.items(), key=lambda x: int(x[0]), reverse=True))
    print(sorted_data)


if __name__ == "__main__":
    directory_path = 'C:/Users/midhdesk1/Desktop/RoziRoti/devopsResume/'
    # words_input = input("Enter comma-separated words: ")
    words_input = "azure, devops, pipeline, devops pipeline"
    words = [word.strip() for word in words_input.split(',')]
    count_word_occurrences_in_directory(directory_path, words)
