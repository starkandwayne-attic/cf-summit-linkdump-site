from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os

port = int(os.getenv("PORT", 5000))

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/monitoring')
def monitoring():
    return render_template('monitoring.html')

@app.route('/pr')
def pr():
    return render_template('pr.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)