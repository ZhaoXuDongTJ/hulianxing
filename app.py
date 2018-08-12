from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def hello_world():
    return '欢迎来到 互联新 API 中心；欢迎开发者 二次开发'


if __name__ == '__main__':
    app.run()
