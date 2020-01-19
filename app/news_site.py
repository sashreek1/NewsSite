from flask import Flask
from flask import render_template
from get_news import get_news


app = Flask(__name__)

data = get_news(["linux", "android", "open-source"])


@app.route("/", methods=['GET'])
def hello():
    return render_template('index.html', len=len(data), data=data)


if __name__ == "__main__":
    app.run()