FROM python:latest


#Labels as key value pair
LABEL Maintainer="roushan.me17"

RUN pip install requests
# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
ADD . /app
WORKDIR /app

#to COPY the remote file at working directory in container
COPY main.py ./
# Now the structure looks like this '/usr/app/src/test.py'

EXPOSE 5000


CMD [ "python", "./main.py"]