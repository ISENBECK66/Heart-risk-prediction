# Machine Learning Zoomcamp 2023 - Midterm project 
![Screenshot](anatomy-of-heart.webp)
## GOAL : Predict heart attack 

This is my first ML project and I want to train a model to predic the probability of a stroke.

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

#### Save final model :
The script *train.py* it's been used to train the final model. It was saved in the file *model_xgb.bin* using *pickle*.

---

#### Loading final model in web service:

1. #### pipenv

The script *heart_attack_verifier.py* load our model : *model_xgb.bin* and it can run in a separate virtual environment across its dependency files *Pipenv* and *Pipenv.lock*.
*flask* was used for the web deployment in *heart_attack_verifier.py* script.

- Install pipenv :
```
pip install pipenv
```
- Get a copy of project and dependencies, or clone the repository :
```
git clone [https://github.com/ISENBECK66/Heart-risk-prediction]
```
- From the project's folder, run :
``` 
pipenv install
```
- All the dependencies should be automatically soddisfied, just verify.
- Run the web service using gunicorn inside the virtual environment:
```
pipenv run gunicorn --bind 0.0.0.0:9696 heart_attack_verifier:app
```

2. #### Docker
There is also the file: *Dockerfile* in the repository, through this you can run the web service in a completely separate container :
- From the project directory, create the docker image :
```
docker build -t heart_attack .
```
- Run the docker image created:
```
docker run -it --rm -p 9696:9696 heart_attack
```

#### Test the web service :

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
I loaded a small video where you can see how the web service works : *web_service_running.webm* 

The video show the local web service starting in Docker, and how it works, evaluating different patients with different data.

The input data are sent to our app through the network by the script *heart_attack_patient_alpha.py* , that is living outside of the Docker container.
Patient's data are static into it, and is necessary to manually modify them to have different answer from our local web service. 

I suggest to view it using VLC player.

---
