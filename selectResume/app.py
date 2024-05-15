from flask import Flask, render_template, request
import json
from backend import count_word_occurrences_in_directory

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        directoryPath = 'static/Azure Devops/'
        directoryPath = 'static/sampleResumes/'
        words_input = data.get('inputString')
        words = [word.strip() for word in words_input.split(',')]
        jsonData = count_word_occurrences_in_directory(directoryPath, words)
        jsonFilePath = 'resumeResult.json'
        with open(jsonFilePath, 'w') as json_file:
            json.dump(jsonData, json_file)
        print(f"Sorted data saved to {jsonFilePath}")
        print("Form String Data:", words_input)

    with open('resumeResult.json', 'r') as json_file:
        data = json.load(json_file)

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
