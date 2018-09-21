
from flask import Flask,render_template,request,session
app=Flask(__name__)
app.config['SECRET_KEY']='123'
# csrf=CSRFProtect(app)
@app.route('/')
def index():
    return render_template('login.html')
@app.route('/cc/')
def index4():
    return render_template('conc.html')

@app.route('/login/',methods=['post'])
def index2():
    username=request.values.get('username')
    password=request.values.get('password')
    print(username,password)
    session['username']=username
    # a=request.values.get('csrf_token')
    # if a is None :
    #     return '拒绝攻击'
    # else:
    return render_template('conc.html')
@app.route('/con/',methods=['post'])
def index3():
    username = request.values.get('username')
    password = request.values.get('password')
    print(username,password)
    # a = request.values.get('csrf_token')
    # if a is None:
    #     return '拒绝攻击'
    # else:
    return '给'+username+'成功转账'+password

if __name__ == '__main__':
    app.run(debug=True,port=4000)