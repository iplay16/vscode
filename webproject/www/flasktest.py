from flask import Flask
from flask import request
import json
import sys
# sys.path.append("E:\code\vsworkspace\webproject\www")
from model.person import person

app = Flask(__name__)

@app.route('/person',methods=['GET'])
def getperson():
    p1=person("lxw",12)
    return json.dumps(p1,default=lambda obj: obj.__dict__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return app.send_static_file('index.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

@app.route('/heropage', methods=['GET'])
def heropage():
    return app.send_static_file('heropage.html')

if __name__ == '__main__':
    app.run()