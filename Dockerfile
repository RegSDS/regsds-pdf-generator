FROM surnet/alpine-python-wkhtmltopdf:3.11.4-0.12.6-small

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "api.py"]