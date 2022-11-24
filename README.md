# Churn Prediction for Fintech Data

<b> **Brief** </b> : The main idea of the project is to predict churn and which parameters is more relevant during analysis using classic supervised techniques like LR, DT, SVM, RF, KNN with the help of GridSearchCV.
<!--more-->

## Objective
Predict user churn of fintech app using clasical supervised models.

## Project Overview
- Get dataset from fintech app, anderstand the key features.
- Explore and Analyze the behaviour of data related to null values, duplicated indexes, balancing data, outliers, categorical and numerical analysis, get some insights with compared analysis between churn and key features.
- As result of exploration phase, pre-process the dataset for being accurate to train, test and later use it in the prediction.
- Model and evaluate 5 models with GridSearchCV for hyperparameter tunning and compare metrics to find the best model.
- Save the model with pickle package in order to use later for prediction test. 
- Create an app where we can use the model.(**Currently, it is under process**)
- **Note:** For more details {{< link name = "HERE" path = "https://github.com/yonkeenn/projectChurnRate">}}


## 1. Dataset <a id="section1"></a>

### 1.1. Dataset Understanding

The bussines challenge: A subscription model on a fintech have users who use the app which it can bring some information about customer behavior. Normaly companies try to minimize the churn which it means cancel subscription. The object is to predict when customer is trying to churn and which feature is the most relevant.

Here some of the fearures:

- userid - userid
- churn - Active = No	Suspended < 30 = No Else Churn = Yes
- age - age of the customer
- zodiac_sign - zodiac sign of the customer
- housing - rent_or_own - Does the customer rents or owns a house
- withdrawn_application - has the customer withdrawn the loan applicaiton
- used_ios- Has the user used an iphone
- used_android - Has the user used a android based phone
- has_used_web - Has the user used MoneyLion Web app
- has_used_mobile - as the user used MoneyLion app
- has_reffered- Has the user referred
- credit_score - Customer’s credit score

## 2. Exploration and Analysis <a id="section2"></a>

For exploration, we will focus on check how is the behavior of data related to the following topics:

1. Checking Null and na values 
2. Check if index is duplicated
3. Verify balance data on dataset 
4. Dataframe data type analysis -> Categorical and numerical for separated
5. Check outliers
6. Analysis of Churn over features
7. Conclusions after exploration and analysis


## 3. Pre-Processing <a id="section3"></a>

As found in exploration phase, we will pre-process the dataset for being accurate for modelling. All of these steps we will save in a pipeline list for next pre-processing steps. Below the list of task:

1. Remove Null/Nan values
2. Remove duplicated indexes
3. Remove not useful features: app_web_user, deposit, ios_user, cc_recommended, cancelled_loan', 'received_loan', 'rejected_loan', 'waiting_4_loan' columns
4. Update numerical and categorical values list for modeling
5. Remove outliers
6. Num-Val: Standarize data for training(without binary features)
7. Cat-Val: One hot encoding
8. Create pre-process pipeline function for next preprocesing for test data.

## 4. Model and Evaluation

For modeling, we faced the following faces:

1. Separate dataset
+ For X and y classes. 
+ Split dataset for training and testing.
2. Feature Selection
+ Use linear regression model
+ Use other techniques like: RFE,Random Forest and Mutual Information
- Then sum up and choose the most important features 
3. Modeling for finding the best:
- Hyperparameter Tunning using GridSearchCV for finding the best hyperparameters of each model
- Fitting and Evaluation using the next models: Logistic Regresion, Decision Tree, Support Vector Machine, Random Forest, Nearest Neighbor.
- Choose the best model according metrics
- Save the model to used with new values
    
For evaluation, we are using the following metrics:

- Confusion matrix
- Accuracy as classification metric
- Precision, Recall, F1-score
- Some graphs like ROC, Precision vs Recall, KS Statistic Test, Cummulative Gain, Lift Curve.

## 5. Prediction <a id="section5"></a>

We will test the model with new dataset. At the begging, we split the data in two: one for train/test and two for prediction. So we will use this prediction data.
