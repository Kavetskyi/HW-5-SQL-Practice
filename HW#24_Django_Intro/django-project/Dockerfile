FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /django-project
WORKDIR /django-project
ADD . /django-project/
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install mysqlclient
COPY . /django-project/