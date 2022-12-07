FROM python:3.8.9-slim-buster
EXPOSE 5000
WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN export EMAIL_USERNAME="adam.marzec@gmail.com"
RUN export EMAIL_PASS="Sakerhet@Gmail!"
CMD [ "python", "./run.py"]