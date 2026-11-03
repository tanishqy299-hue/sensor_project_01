# The Docker File defines the environment , dependencies and config when needed to run your project 

FROM python: 3.14-slim-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ['python3','app.py']