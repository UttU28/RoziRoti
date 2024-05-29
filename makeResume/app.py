from flask import Flask, render_template
from flask_weasyprint import HTML
import json
import os


allData = 'utsavChaudhary.json'
app = Flask(__name__)

@app.route('/')
def index_pdf():
    with open(allData, 'r') as json_file:
        data = json.load(json_file)
    html = render_template('index.html', data=data)
    pdf = HTML(string=html).write_pdf()

    pdf_path = os.path.join('static', 'Utsav_Chaudhary_Resume.pdf')
    with open(pdf_path, 'wb') as f:
        f.write(pdf)

    return html
    # return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
