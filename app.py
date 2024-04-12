from flask import Flask, render_template
import json

app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=["GET", "POST"])
def i():
    return render_template('welcome.html')


@app.route("/welcome2", methods=["GET", "POST"])
def welcome2():
    return render_template('welcome2.html')



@app.route('/network')
def index():
    with open('new_data.json', 'r') as json_file:
        data = json.load(json_file)
    return render_template('network.html', data=data)



@app.route('/dashboard')
def dashboard():
    with open('conver1.json', 'r') as json_file:
        data = json.load(json_file)
    return render_template('dashboard.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)