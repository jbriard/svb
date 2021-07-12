docker build -t svb .

docker tag svb justinbriard/svb:latest

docker push justinbriard/svb:latest

docker run -d --name svb -p 8080:8080 svb

