from flask import Flask, render_template, request
from requests import post
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # 后台拿数据首先区分是GET还是POST请求，如果是GET则直接展示页面，否则则从后台拿数据
    if request.method == 'GET':
        return render_template('index.html')  # 将网页渲染
    elif request.method == 'POST':
        word = request.form.get('word')
        sizes = request.form.get('sizes')
        fonts = request.form.get('fonts')
        fontcolor = request.form.get('fontcolor')
        data = {
            'word': word,
            'sizes': sizes,
            'fonts': fonts,
            'fontcolor': fontcolor,
        }
        html = post('http://www.uustv.com/', data=data).text
        dom = BeautifulSoup(html, 'lxml')
        img_url = dom.find_all('div', 'tu')[0].img['src']
        apath = 'http://www.uustv.com/' + img_url
        return render_template('index.html', apath=apath)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
