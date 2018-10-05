FROM python:3.7

WORKDIR /usr/src/pipenv-example

COPY . .
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

CMD [ "python", "./sample_script.py" ]
