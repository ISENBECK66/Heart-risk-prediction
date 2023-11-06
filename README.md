# Machine Learning Zoomcamp 2023 - Midterm project 
![Screenshot](anatomy-of-heart.webp)
## GOAL : Predict heart attack 

This is my first ML project and I want to train a model to predic the probability to have an heart attack.

I find a dataset in kaggle for this purpose:

#### Dataset description: https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset/data

---

#### Data :
You can follow this [link](https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset/data) to better understand the data.
I uploaded the entire dataset in the repository. File: *heart_attack_prediction_dataset.csv*

---

#### Notebook :
The file *notebook.ipynb* contains all the code that I wrote during data preparation and data cleaning process and it contains also
EDA, feature importance analysis, model parameter tuning and model selection process.

Unfortunatly, in this phase I discovered that the data in the choosen dataset were poorly correlated.

This condition didn't help our model to reach great performance.

---

#### Save the final model :
The script *train.py* it's been used to train the final model. It was saved in the file *model_xgb.bin* using *pickle*.

---

#### Load the final model in a local web service, and run it using PIPENV or DOCKER:

1. #### pipenv : run the project in a virtual environment :

The script *heart_attack_verifier.py* load our model : *model_xgb.bin* and it can run in a separate virtual environment across its dependency files *Pipenv* and *Pipenv.lock*.
*flask* was used for the web deployment in *heart_attack_verifier.py* script.

- Install pipenv :
```
pip install pipenv
```
- Get a copy of the project and its dependencies, or clone the repository :
```
git clone https://github.com/ISENBECK66/Heart-risk-prediction
```
- Enter the project directory and install the dependencies:
```
cd Heart-risk-prediction/
```
``` 
pipenv install
```
- Run the web service using gunicorn inside the virtual environment:
```
pipenv run gunicorn --bind 0.0.0.0:9696 heart_attack_verifier:app
```

2. #### Docker : run the project in a complete and separate virtual machine :
- Get a copy of the project and its dependencies, or clone the repository :
```
git clone https://github.com/ISENBECK66/Heart-risk-prediction
```
- Enter the project directory and build the docker environment:
```
cd Heart-risk-prediction/
```
```
docker build -t heart_attack .
```
- Run the docker image:
```
docker run -it --rm -p 9696:9696 heart_attack
```

#### Test the local web service :

- To test the web service, in another terminal you can run the test script :
```
python heart_attack_patient_alpha.py
```
- Edit the patient information to generate customized prediction about your healt, changing the parameters in the file :
```
vi heart_attack_patient_alpha.py
```

---

#### Video of the web service running :
In the repository you can find a small video : *web_service_running.webm* , where you can see the local web service at work

The video show the local web service starting in Docker, and how it evaluate different patients.

The patient's data are sent to our app through the network by the script *heart_attack_patient_alpha.py* , that is living outside of the Docker container.
The video show the patient's evaluations for different input data. 

I suggest to use VLC player to view it.

---
