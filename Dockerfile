FROM python:slim
LABEL version="1.0"
LABEL description="Demo App Kubernetes for Scaleway"
LABEL com.example.vendor="Scaleway"
LABEL org.opencontainers.image.authors="jbriard@scaleway.com"


WORKDIR /usr/src/svb

COPY svb/ . 

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD [ "python", "./run.py" ]
