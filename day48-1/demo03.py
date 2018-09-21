from flask import Flask
from flask import g


app = Flask(__name__)


# 保存一些临时的数据, 配合钩子函数使用
@app.route("/")
def index():
    print(g.isvip)
    g.name = 'zhangsan'
    print(g.name)
    return 'ok'


@app.before_request # 在每一次请求之前执行
def request_before():
    vip = True # 从数据库查，需要很多代码实现
    g.isvip = vip

@app.before_first_request
def request_first_before():
    print("第一个请求之前执行，后面不执行")

@app.errorhandler(404)
def request_404(code):
    from flask import render_template
    return render_template('404.html')


# @app.teardown_appcontext
# def request_teardown():
#     # 不管代码有没有出错，这个钩子请求完成之后都执行
#     pass

# @app.after_request
# def request_after():
#     pass

#
# @app.add_template_filter('myfilter') # 注册过滤器
# def myfilter(value):
#     pass
#     return ""




if __name__ == '__main__':
    app.run(debug=True,port=7000)

