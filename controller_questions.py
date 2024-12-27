import db_repository
from flask import Flask,jsonify 
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
def convert_data_to_json(questions):
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
    data=db_repository.takeData()
    jsonData=convert_data_to_json(data)
    return jsonify(jsonData)
    
if __name__=='__main__':
    app.run(debug=True)



