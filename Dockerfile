FROM python:3.10.2

WORKDIR /python_flask_plusss_postgres

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
ENV FLASK_APP=main.py

ENTRYPOINT [ "flask"]
CMD [ "run", "--host", "0.0.0.0" ]
