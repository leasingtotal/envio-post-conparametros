from flask import Flask, render_template, redirect,json,jsonify,request
from flask_cors import CORS,cross_origin

app=Flask(__name__)
app.config['SECRET_KEY']='adsadsasad123123asdads'


@app.route("/",methods=['GET','POST'])
@cross_origin()
def index():
    return render_template('index.html')


@app.route("/usuarios",methods=['POST'])
@cross_origin()
def usuarios():

    if request.method=='POST':
        user=request.form['usuario']
        password=request.form['clave']
    
    return render_template('principal.html', nombre=user, contra=password)



if __name__=='__main__':
    app.run(host='10.50.1.137',port=8989,debug=True)
