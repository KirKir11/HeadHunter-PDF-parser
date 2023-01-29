from urllib import request

from HeadHunterParserClass import HeadHunterParser
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
async def main_function():
    if 'cv' in request.files:
        cv = request.files['cv']
        hh = HeadHunterParser(cv)
        return hh.get_fields()


if __name__ == '__main__':
    app.run()
