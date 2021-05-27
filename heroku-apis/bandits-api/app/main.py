from vowpalwabbit import pyvw
from sklearn import preprocessing
import numpy as np
from flask import Flask,request as req
import json

action_encoder = preprocessing.LabelEncoder()
action_encoder.classes_ = np.load('app/action_encoder.npy',allow_pickle = True)

vw = pyvw.vw("--cb_explore  135567 --epsilon 0.2 -i app/cb.model")

app = Flask(__name__)

@app.route("/")
def home():
    return 'Hello World!'

@app.route("/predict", methods=['POST'])
def index():
    args = json.loads(req.data)
    feat1 = args['Location']
    feat2 = args['Age']
    feat3 = args['Country']
    feat4 = args['Book_Author']
    feat5 = args['Year_Of_Publication']

    test = "| " + str(feat1) + " " + str(feat2) + " " + str(feat3)+ " " + str(feat4) + " " + str(feat5)
    preds = np.array(vw.predict(test))
    indices = (-preds).argsort()[:6]
    books = []
    for ind in indices :
        books.append(action_encoder.inverse_transform([int(ind)])[0])
    data = {'labels':books}
    return data

@app.route("/learn", methods=['POST'])
def learn():
    args = json.loads(req.data)
    feat1 = args['Location']
    feat2 = args['Age']
    feat3 = args['Country']
    feat4 = args['Book_Author']
    feat5 = args['Year_Of_Publication']
    action = args['Book_Title']
    cost = args['cost']
    probability = args['probability']
    action = action_encoder.transform([action])
    learn_example = str(action) + ":" + str(cost) + ":" + str(probability) + " | " + str(feat1) + " " + str(feat2) + " " + str(feat3) +" " + str(feat4) + " " + str(feat5)
    vw.learn(learn_example)
    vw.save('app/cb.model')  
    test = "| " + str(feat1) + " " + str(feat2) + " " + str(feat3)+ " " + str(feat4) + " " + str(feat5)
    preds = np.array(vw.predict(test))
    indices = (-preds).argsort()[:6]
    books = []
    for ind in indices :
        books.append(action_encoder.inverse_transform([int(ind)])[0])
    data = {'labels':books}
    return data

