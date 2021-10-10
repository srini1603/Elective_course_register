from flask import Flask
from flask import render_template
import file

app = Flask(__name__)


@app.route('/')
def script_output():
    output = file.df
    return render_template('index.html', output=output)


if __name__ == '__main__':
    app.run(debug=True)