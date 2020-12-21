from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def get_index():
    return render_template('index.html')

@app.route('/login.html')
def get_login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()