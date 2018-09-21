# 上下文对象
# threadlocal
    # 在同一线程中传递值，线程隔离的，保证变量的线程安全
import threading
# flask = werkzeug(接受请求) + jinja2(模板) + sqlalchemy(数据库)
from werkzeug.local import Local
local = threading.local()
local.a = 10
l = Local()
def aa(i) :
    # 子线程
    #local.a = 20
    l.request = i
    bb()
def bb() :
    print(l.request)
    #print("子线程" +  str(local.a))
if __name__ == '__main__':
    for item in range(10):
        t = threading.Thread(target=aa,args=(item,))
        t.start()
        t.join() # 阻塞当前线程，让t执行完继续执行

