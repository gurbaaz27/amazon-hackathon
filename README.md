# HackOn with Amazon - Ml_EnThUsIaSts

## General Information

### Theme - Shopping Experience (Offline and Online)
### Team Members :

- [Parth Srivastava](https://www.linkedin.com/in/parth-srivastava-5a10211a2/), UG Sophomore, IIT Kanpur
- Gurbaaz Singh Nandra, UG Sophomore, IIT Kanpur
- Shubh Agarwal, UG Sophomore, IIT Kanpur

## Problem Overview

The persuit of personalization has long been carried out in shopping websites. From personal dashboards to recommender systems, we've come a long way to give the user more personalized experience. In this hackathon, we've developed the following functionalities and integrated them into our demo website.

- Personalized Discount Coupon Generator
- Personalized Product Recommendation using Multi-Armed Contextual Bandits

The **Personalized Discount Coupon Generator** gives **unique discounts** to the users, based on the **user's activitites like time duration, page views, etc.** The **Product Recommndation System** using **Multi-Armed Contextual Bandits** is a unique approach to recommedation. As opposed to **Collaborative Filtering**, this approach **improves over time**, and hence provides **more utility** as compared to the older approach. Furthur details regarding the 2 functionalities can be found below.

## Directory Overview

- **Bandits** : Contains the model, encoders and the training code for the Multi-Armed Contextual Bandits.
- **Classifier** : Contains the data, model and the encoders for the Personalized Discount Coupons.
- **Frontend** : Contains the HTML, JS and CSS files for the frontend of our project.
- **Heroku-APIs** : Contains the code of the APIs for both the functionalitites, and the deployment code for Heroku.

## Deployment

We deployed our project using **Firebase Hosting**. The deployed verion of the website is available [HERE](https://hackon.web.app)

## Deep into the Implementation

### Personalized Discount Coupon Generator

#### Data Description (Used for Training)

We used an open source dataset for the training of the model.The data can be found [here](https://drive.google.com/file/d/1QGqnZwcX6o4i7KgmSMlmDdokoMS3Hzk1/view?usp=sharing) The dataset contained **24 unique features** like **avg_session_duration**, **hits**,etc. and contained 3 labels - **'buyer','window' and 'hesitant'.** The description of the labels is given below : 

- **Buyer** - The customers who often purchase products from the website fall in this category.
- **Window** - This category includes customers who need a *little push over the edge* to buy the products.
- **Hesitant** - This category includes customers who seldom buy products from our website, and therefore need a large incentive to get them over the edge.

#### Model Used 

We used an **lgbm classifier** for the problem. We used a total of **20 features** for our model, with a **80:20** train/dev split. The model gave an accuracy of **99.345%** on the dev set.

#### DevOps and Integration

We deployed the model using **Flask API** and **Heroku**. For every user that opens our website, we use javascript to generate dummy values for the features that we use in our model ( In actual use case, this can simply be done by pulling the values of the user from the database). We then post those values(after encoding the non-numerical values using the respective encoders) to the */predict* endpoint of our model, and fetch the classification result from our model. Based on the result, we provide the user with a personalized discount coupon, a coupon which can help us (a shopping firm) maximize our utility.

### Product Recommendation using Multi-Armed Contextual Bandits

#### Data Description (Used for Training)

We used an open source dataset from Kaggle for this task. The dataset can be found [here](https://www.kaggle.com/arashnic/book-recommendation-dataset). One can clearly see that the dataset has many outliers, null values, etc, and hence required some good amount of pre-processing. Also, in order to train the bandits on the dataset, we had to combine the 3 files into one. Our pre-processing code can be found in **pre-processing.ipynb**. The dataset obtained after the final pre-processing can be found [here](https://drive.google.com/file/d/15bbcRdSOe7AAH_xy9lTqfk_TWAAeaLtg/view?usp=sharing)

The finally prepared dataset contains fields like **location**, **country**, **age**, **book title**, etc, with a total of **383,842** data points.

#### Model Used

We used **[Vowpal Wabbit](https://vowpalwabbit.org/)** to train our Multi-Armed Contextual Bandits. It is simple to use and easily integrable with python. We use **cb_explore** algorithm, with an **epsilon value of 0.2**, so as to focus on both, **exploration** as well as **exploitation**. Since our final dataset had a total of **135567** unique books, therefore, our final algorithm for training was - `cb_explore 135567 --epsilon 0.2`. We used `10 - book_rating` as the cost of choosing the particular datapoint, as cost is the opposite of reward. We used `book_rating/10.0` as the probability of choosing the datapoint. We use the clicks as the reward function in the model.

#### DevOps and Integration

We again used **Flask API** and **Heroku** for deploying our model. For every user that visits our website, we generate dummy features like **location**,**age**, etc, and push them to the */predict* endpoint of our API, which in turn provides us with the top 6 recommendations for the user. These 6 recommendations are then displayed on our homepage in the recommendations section. Once a user selects a particular option, the values previously generated, along with the book_name, are pushed to the */learn* endpoint of the API, which learns from the pushed datapoint, and again generates 6 new recommendations after learning. As we know, from the basics of Reinforcement Learning, that by learning, the model tries to maximise its utility by minimising the error, and hence generates perfect recommendations after some learning iterations.

 
## Resource Links

- [Proposal Doc](https://docs.google.com/document/d/1h5Fmb2_B-71QAZVFZParN5ByFkh3D7Si6o4j_CZ4Ol8/edit)
- [A Contextual-Bandit Approach to Personalized News Article Recommendation](https://arxiv.org/pdf/1003.0146.pdf)
- [Recommendation Dataset](https://www.kaggle.com/arashnic/book-recommendation-dataset)
- [Classification Dataset](https://drive.google.com/file/d/1QGqnZwcX6o4i7KgmSMlmDdokoMS3Hzk1/view?usp=sharing)
