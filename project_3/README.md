
# Classifying posts into the different threads based on titles on Reddit (Natural language processing - NLP)

## Problem Statement:
Social media landscape in the world today are filled with consumer feedbacks within their own social media pages
or forums. If brands wish to take consumer sentiments outside of their own brand page or to deep dive into
their competitors brand "health" from the eyes of the consumer, this tool (while still in it's prototype phase) will help you to segregate these posts into the respective brands.

## Objective:
We will be investigating two supermarket chains in the US, Kroger and Publix to see if our model is able to
classify the posts accurately into the respective brands based on the text in their titles.


## Methodology:
We are focused on Reddit as our practice API this round but in reality, with some minor tweaks, it should work on most
platforms. Due to Reddit constraints, we will only collect up to 1000 unique titles from Reddit as our database to
work with.

We have used two different language processing methods to trial (1 with """SpaCy""" and another with TFIDF vectorizer),
in addition, we also used two different models in this classification project (NaiveBayes and LogisticRegression)

## Constrains:
Within Reddit, some posts are pictorial based (such as gif or memes) and hence a pure text classification will not be 
completely useful.
           
We were also not able to get the location of the post which will help us determine which supermarket is within the city
or neighborhood
           
As with any NLP, the challenge is to decode abbreviations or potential spelling errors.

## Materials: 

   ### 1. Data:
   The raw csv files are within this folder.
   
|File name | Description                                     |
|----------|-------------------------------------------------|
|df_k.csv  | Raw Data from Reddit Kroger                     |
|df_p.csv  | Raw Data from Reddit Publix                     |
|final.csv | Combined and cleaned data from Kroger and Publix|
    
   ### 2. Notebooks
   The project details and codes are within this folder where we store the codes for
   scraping, pre-processing, modelling and analysis 
   
|File name    |   Description                                                                                       |
|-------------|-----------------------------------------------------------------------------------------------------|
|Project 3.1  | Data scraping from Reddit                                                                           |
|Project 3.2  |Pre-processing, modelling and analysis, method 1 SpaCy(pre-processing), NaiveBayes and LogisticRegression (modelling)|
|Project 3.3  | Pre-processing, modelling and analysis, method 2 TFDIF vectoriser(pre-processing), NaiveBayes and   LogisticRegression (modelling)|
|Project 3.4  | Pre-processing, modelling and analysis, method 3 TFDIF vectoriser(pre-processing), NaiveBayes and   RandomForest (modelling)|
|Project 3.5  | Pre-processing, modelling and analysis, method 4 feature engineering, TFIDF vectoriser, NavieBayes and Adaboost(modelling)|

   ### 3. Presentation slides
   Short presentation will be uploaded once the projected is submitted (here)
      
References:<br>
https://www.reddit.com/r/kroger/ <br>
https://www.reddit.com/r/publix/ <br>
https://www.youtube.com/watch?v=5Y3ZE26Ciuk


```python

```
