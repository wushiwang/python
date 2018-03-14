from flask import render_template,Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload',methods=['GET','POST'])
def upload():
    files=request.files.get('file')
    if not files:
        return '请先上传文件'
    files.save(r'C:\Users\shiwang\PycharmProjects\wangpan\static\%s' %files.filename)

    return render_template('download.html',url='/static/%s' %files.filename)

if __name__ == '__main__':
    app.run(debug=True,port=8000)
