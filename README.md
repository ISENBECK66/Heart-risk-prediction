# Machine Learning Zoomcamp 2023 - Midterm project 
![Screenshot](anatomy-of-heart.webp)
## GOAL : Predict heart attack 

This is my first ML project and I want to train a model to predic the heart attack probability.

I find a dataset in kaggle for this purpose :

#### Dataset description: https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset/data

---

#### Data :
You can follow this [link](https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset/data) to better understand the data.
I uploaded the entire dataset in the repository. File: *heart_attack_prediction_dataset.csv*

---

#### Notebook :
The file *notebook.ipynb* contains all the code that I written during data preparation and data cleaning process and it contains also
EDA, feature importance analysis, model parameter tuning and model selection process.

Unfortunatly, in this phase I discovered that the data in the choosen dataset were poorly correlated.

This condition didn't help our model to reach great performance.

---

#### Save final model :
The script *train.py* it is been used to train the final model. It has been saved in the file *model_xgb.bin* using *pickle*.

---

#### Loading final model in web service:

1. #### pipenv

   The script *heart_attack_verifier.py* load our model : *model_xgb.bin* and it can run in a separate environment thrugh its dependencies files *Pipenv* e *Pipenv.lock*.
   *flask* was used for web deployment in *heart_attack_verifier.py* script.

   Install pipenv :
   ```
   pip install pipenv
   ```
   Get a copy of project and dependencies, or clone the repository :

   ```
   git clone [https://github.com/ISENBECK66/Heart-risk-prediction]
   ```

   from the project's folder, run :

   ``` 
   pipenv install
   ```

   all the dependencies should be soddisfied, run the web service using gunicorn inside the virtual environment:

   ```
   pipenv run gunicorn --bind 0.0.0.0:9696 heart_attack_verifier:app
   ```

   In another terminal run the test script :
   ```
   python heart_attack_patient_alpha.py
   ```

   Edit the patient information to generate customized prediction about your healt, changing the parameters in this file :
   ```
   vi heart_attack_patient_alpha.py
   ```
   

2.There is also the file: *Dockerfile* in the repository, for running the web service in a completely separate container instead.




---

#### Test the web service :
The script *heart_attack_patient_alpha.py* send the data of one patient and can be used to test the service.

---

#### Video of the web service running :
I loaded a small video where you can see how the web service works : *web_service_running.webm* 

The video show the web service starting in Docker, and how it is evaluating data coming from different patients.

The data to evaluate are sent through the network by the script *heart_attack_patient_alpha.py* , that is living outside of the Docker container.
Patient's data into the script are static, and are manually modified for every iteration only to see the heart healt evaluation coming back from the web service. 

I suggest to view it using VLC player.

---
