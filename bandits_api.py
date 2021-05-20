from vowpalwabbit import pyvw
from sklearn import preprocessing
import numpy as np
from flask import Flask,request as req
import json

action_encoder = preprocessing.LabelEncoder()
action_encoder.classes_ = np.load('action_encoder.npy',allow_pickle = True)

vw = pyvw.vw("--cb 135567 -i cb.model")

app = Flask(__name__)

@app.route("/predict")
def index():
    args = json.loads(req.data)
    feat1 = args['Location']
    feat2 = args['Age']
    feat3 = args['Country']
    feat4 = args['Book_Author']
    feat5 = args['Year_Of_Publication']

    test = "| " + str(feat1) + " " + str(feat2) + " " + str(feat3)+ " " + str(feat4) + " " + str(feat5)
    preds = vw.predict(test)
    print(preds)
    label = action_encoder.inverse_transform([preds])[0]
    data = {'label':label}
    return data


if __name__ == '__main__':
    app.run(port = 8080,debug=True)