FROM python:3.10.0-alpine3.13

WORKDIR /app
ADD . /app
RUN  python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN  pip install -r requirements.txt
EXPOSE 5000
COPY . .
RUN cd todoapp
CMD ["python"," manage.py", "runserver", "0.0.0.0:5000"] 