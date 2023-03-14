from flask import Flask,render_template,redirect,url_for
from flask import request,abort,send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

#HTTP测试
@app.route('/', methods = ['GET', 'POST'])
def home():
    print(f"headers:\r\n{request.headers}\r\nbody:\r\n{request.data.decode()}")
    return f"headers:\r\n{request.headers}\r\nbody:\r\n{request.data.decode()}"

#headers测试
@app.route('/headers', methods = ['GET', 'POST'])
def headers():
    return str(request.headers)

#body测试
@app.route('/body', methods = ['POST'])
def body():
    return request.data

#文件下载
@app.route('/file/<filename>', methods = ['GET'])
def file(filename):
	return send_from_directory('../file/', filename, as_attachment = True)

#文件上传
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath, '../file/',secure_filename(f.filename))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        return redirect(url_for('upload'))
    return render_template('upload.html')

if __name__ == '__main__':
	#app.debug = True # 设置调试模式，生产模式的时候要关掉debug
	app.run(host='0.0.0.0', port = 6443,)
