from flask import Flask, render_template, request
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

#表单提交
@app.route("/test/register")
def register():
    return render_template("test/register.html")

#接收表单的网页需要写上methods
@app.route("/result", methods=['POST', 'GET'])
def result():
    if request.method=='POST':
        result = request.form
        return render_template("test/result.html", result=result)



if __name__ == '__main__':
    app.run()
