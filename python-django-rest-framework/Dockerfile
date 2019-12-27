FROM python:3.8

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN rm -rf /tmp/*

WORKDIR /app
ADD ./butcher_box_backend .

EXPOSE 5123

CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:5123"]
