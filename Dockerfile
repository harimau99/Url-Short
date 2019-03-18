FROM python:2.7

RUN pip install -r requirements.txt

EXPOSE 8000

CMD  python shrinkul/manage.py runserver 8000
