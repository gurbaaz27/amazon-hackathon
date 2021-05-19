# import flask

from sklearn import preprocessing
import numpy as np
from flask import Flask, request as req
import pickle as pkl


app = Flask(__name__)

campaign_encoder = preprocessing.LabelEncoder()
campaign_encoder.classes_ = np.load('./campaign.npy',allow_pickle = True)

device_category_encoder = preprocessing.LabelEncoder()
device_category_encoder.classes_ = np.load('./device_category.npy',allow_pickle = True)

social_network_encoder = preprocessing.LabelEncoder()
social_network_encoder.classes_ = np.load('./social_network.npy',allow_pickle = True)

shopping_stage_encoder = preprocessing.LabelEncoder()
shopping_stage_encoder.classes_ = np.load('./shopping_stage.npy',allow_pickle = True)



loaded_model = pkl.load(open('./model.pickle.dat', "rb"))

@app.route("/predict", methods=['POST'])
def make_prediction():
        
        avg_session_duration = req.args['avg_session_duration']
        campaign = campaign_encoder.transform([req.args['campaign']])[0]
        hits = req.args['hits']
        day_of_week = req.args['day_of_week']
        day = req.args['day']
        device_category = device_category_encoder.transform([req.args['device_category']])[0]
        entrances = req.args['entrances']
        events_per_session = req.args['events_per_session']
        exits = req.args['exits']
        hour = req.args['hour']
        organic_search = req.args['organic_search']
        page_depth = req.args['page_depth']
        page_views = req.args['page_views']
        page_views_per_session = req.args['page_views_per_session']
        sessions = req.args['sessions']
        social_network = social_network_encoder.transform([req.args['social_network']])[0]
        events = req.args['events']
        unique_events = req.args['unique_events']
        week = req.args['week']
        frequency = req.args['frequency']
        X = np.array([avg_session_duration,campaign,hits,day_of_week,day,device_category,entrances,events_per_session,exits,hour,organic_search,page_depth,page_views,page_views_per_session,sessions,social_network,events,unique_events,week,frequency])
        X = X.reshape(1,-1) 
        pred = loaded_model.predict(X)
        label = shopping_stage_encoder.inverse_transform([pred])[0]
        return label
        


