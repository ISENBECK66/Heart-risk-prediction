FROM python:3.10-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock" , "./"]

RUN pipenv install --system --deploy

COPY ["heart_attack_verifier.py" , "model_xgb.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "heart_attack_verifier:app"]
