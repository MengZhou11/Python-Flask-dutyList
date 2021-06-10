from flask import Flask,render_template
import datetime

app = Flask(__name__)


#路由解析，通过用户访问的路径 匹配相应的函数
#以下路由的路径不能重复
@app.route('/index')  #可以当作固定格式
def hello():
    return "hello"

@app.route("/user/<name>") #string类型
def wecome(name):
    return "hi, %s"%name

@app.route("/user/<int:id>") #int类型 还可以是float类
def wecome2(id):
    return "hi user%d"%id

@app.route("/")
def index2():
    time = datetime.date.today()
    name = ["Tom","Amy","Mary"]
    task = {"Task":"Submit report","Deadline":"6pm"} #字典
    return render_template("index.html", var=time, list = name, task=task)



if __name__ == '__main__':
    app.run()
