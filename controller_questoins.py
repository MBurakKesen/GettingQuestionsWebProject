import db
from flask import Flask,jsonify 
# from fastapi.middleware.cors import CORSMiddleware
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

datamiz=db.veriGetir()
def convert_data_to_json(questions):
    # Her bir tuple'ı bir sözlüğe dönüştürerek JSON uyumlu hale getiriyoruz
    formatted_data = [
        {
            "soru": soru,
            "cevapA": cevapA,
            "cevapB": cevapB,
            "cevapC": cevapC,
            "cevapD": cevapD,
            "dogruCevap": dogruCevap
        }
        for soru, cevapA, cevapB, cevapC, cevapD, dogruCevap in questions
    ]
    return formatted_data

    
@app.route("/api",methods=['GET'])
def get_data():
    datamiz=db.veriGetir()
    jsonData=convert_data_to_json(datamiz)
    return jsonify(jsonData)


if __name__=='__main__':
    app.run(debug=True)



