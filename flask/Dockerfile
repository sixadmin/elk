FROM python

COPY . .

RUN pip install flask

EXPOSE 5000

CMD ["python","-m","flask","run","--host=0.0.0.0"]