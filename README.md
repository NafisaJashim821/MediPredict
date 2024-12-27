
# MediPredict
Your Smart Symptom-Based Disease Prediction System

# Overview
MediPredict is an intelligent system that predicts potential diseases based on user-provided symptoms using advanced machine learning algorithms. Built with the Django framework, it features an intuitive web interface for seamless user interaction.




## Features

- User Input: A simple and interactive interface for entering symptoms.
- Accurate Predictions:
Utilizes machine learning models, including:
K-Nearest Neighbors (KNN)
Random Forest
Decision Tree
- Web Interface:
A modern and responsive web application developed using Django



## Technologies and Libraries Used
- Machine Learning
    - scikit-learn (DecisionTreeClassifier, SVC, RandomForestClassifier, GaussianNB, KNeighborsClassifier)
    - joblib

- Data Handling:
   - pandas
Web Development:
- Django

## Usage/Examples


1 . Access the Application:
Open the web interface in your browser by navigating to the provided URL.

2 . Input Symptoms:
Enter your symptoms in the input fields (up to five).

3 . Choose an Algorithm:
Select from the available options, including Decision Tree, Random Forest, or KNN.
4 . Get Predictions:
Click on the "Predict" button to view:
 - The predicted disease
 - Its probability
 


## Installation

To set up MediPredict locally:
 - 1 . Clone the Repository:

```bash
  git clone <repository-link>  
  cd medipredict  

```
  Start the Development Server:
  ```bash
 python manage.py runserver  
 

``` 
Access the Application:
```bash
http://127.0.0.1:8000/  

```

## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

