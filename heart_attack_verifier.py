import pickle
import numpy as np
import xgboost as xgb

from flask import Flask, request, jsonify


model_file = 'model_xgb.bin'

with open(model_file, 'rb') as f_in:
    model, dv = pickle.load(f_in)

app = Flask('heart')


@app.route('/heart_attack_verifier', methods=['POST'])

def heart_attack():
    
    patient = request.get_json() 
    
    X_patient = dv.transform([patient]) 
  
    dpatient = xgb.DMatrix(X_patient, feature_names=dv.get_feature_names_out())
    y_pred = model.predict(dpatient)[0].round(2)

    #print(y_pred)
    
    heart_attack = y_pred >= 0.5    
    
    result = {
        'heart_attack_probability': float(y_pred),
        'heart_attack : ': bool(heart_attack),
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
