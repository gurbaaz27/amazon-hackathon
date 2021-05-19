# import flask

from sklearn import preprocessing
import numpy as np
from flask import Flask, request as req
import pickle as pkl
import json

app = Flask(__name__)

campaign_encoder = preprocessing.LabelEncoder()
campaign_encoder.classes_ = np.load('campaign.npy',allow_pickle = True)

device_category_encoder = preprocessing.LabelEncoder()
device_category_encoder.classes_ = np.load('device_category.npy',allow_pickle = True)

social_network_encoder = preprocessing.LabelEncoder()
social_network_encoder.classes_ = np.load('social_network.npy',allow_pickle = True)

shopping_stage_encoder = preprocessing.LabelEncoder()
shopping_stage_encoder.classes_ = np.load('shopping_stage.npy',allow_pickle = True)



loaded_model = pkl.load(open('model.pickle.dat', "rb"))

@app.route("/predict", methods=['POST'])
def make_prediction():
        args = json.loads(req.data)
        avg_session_duration = args['avg_session_duration']
        campaign = campaign_encoder.transform([args['campaign']])[0]
        hits = args['hits']
        day_of_week = args['day_of_week']
        day = args['day']
        device_category = device_category_encoder.transform([args['device_category']])[0]
        entrances = args['entrances']
        events_per_session = args['events_per_session']
        exits = args['exits']
        hour = args['hour']
        organic_search = args['organic_search']
        page_depth = args['page_depth']
        page_views = args['page_views']
        page_views_per_session = args['page_views_per_session']
        sessions = args['sessions']
        social_network = social_network_encoder.transform([args['social_network']])[0]
        events = args['events']
        unique_events = args['unique_events']
        week = args['week']
        frequency = args['frequency']
        X = np.array([avg_session_duration,campaign,hits,day_of_week,day,device_category,entrances,events_per_session,exits,hour,organic_search,page_depth,page_views,page_views_per_session,sessions,social_network,events,unique_events,week,frequency])
        X = X.reshape(1,-1) 
        pred = loaded_model.predict(X)
        label = shopping_stage_encoder.inverse_transform([pred])[0]
        data = {'label':label}
        return data
        


    
if __name__ == '__main__':
    app.run(port = 8080,debug=True)