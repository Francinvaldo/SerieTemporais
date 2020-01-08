from flask import Flask
from flask import render_template


app = Flask(__name__)

teste = 554

@app.route('/')
def index():
    return render_template("index.html",message="testa a message rtrete",contatos=['c1','c2','c3']
    ,teste=teste)



if __name__ ==  '__main__':
    app.run(debug=True,host='0.0.0.0')