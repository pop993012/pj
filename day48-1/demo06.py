from flask import Flask,render_template


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('attact.html')




if __name__ == '__main__':
    app.run(debug=True,port=1000)