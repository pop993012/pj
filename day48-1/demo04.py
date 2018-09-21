from  flask import Flask
from blinker import  Namespace
app=Flask(__name__)

#订阅消息
pj=Namespace()
pjkj=pj.signal('pojian')
def aa(sender):
    print('OK')

pjkj.connect(aa)





#发布消息
pjkj.send()




if __name__ == '__main__':
    app.run(debug=True)