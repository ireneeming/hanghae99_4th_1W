from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# HTML 화면 보여주기
@app.route('/')
def home():
    # DB에서 저장된 전시 찾아서 HTML에 나타내기
    exhibitions = list(db.exhibition.find({}, {'_id': False}))
    return render_template('index.html', exhibitions=exhibitions)

@app.route('/detail', methods=['GET'])
def detail():

    all_exhibit = list(db.exhibition.find({}, {'_id': False}))
    return render_template('detail.html', exhibitlist=all_exhibit)


# API 역할을 하는 부분
@app.route('/exhibition', methods=['GET'])
def show_stars():
    all_exhibit = list(db.exhibition.find({}, {'_id': False}))
    return jsonify({'all_exhibit': all_exhibit})


@app.route('/exhibition', methods=['POST'])
def like_star():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'like 연결되었습니다!'})


@app.route('/exhibition', methods=['POST'])
def delete_star():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'delete 연결되었습니다!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)