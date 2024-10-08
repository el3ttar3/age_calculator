from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    age = None
    if request.method == 'POST':
        birthdate_str = request.form['birthdate']
        birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return render_template("/index.html", age=age)

if __name__ == '__main__':
    app.run(debug=True)
