# 上下文对象 和 请求对象     使用栈


# 应用上下文处理多个应用的情况
# 请求上下文 处理多个请求


from flask import Flask
from flask import current_app,url_for

app = Flask(__name__)
app.config["DB"] = '123123'

app1 = Flask(__name__)


app2 = Flask(__name__)


# ctx = app.app_context() # 应用上下文
# ctx.push()  # 压入栈中
# print(current_app.name)
# ctx.pop() # 出栈

with app.app_context():
    print(app.config['DB'])



@app.route("/")
def index():
    print(current_app.name)
    return "ok"


# 请求上下文 : 先把应用程序上下文压入到栈中， 然后把请求上下文压入到占中
with app.test_request_context() :
   print(url_for("index"))



if __name__ == '__main__':
    app.run(debug=True)


# 为什么使用栈管理应用上下文
# 因为flask里面可以有多个应用程序。为了方便管理

# 应用上下文 可以为测试创建一个应用程序的环境
# 请求上下文在压入栈之前，会把把当前请求的应用上下文压入到栈中
