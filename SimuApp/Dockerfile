FROM python:3.10.6

LABEL MAINTAINER="User"

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www/

RUN apt-get update \
 && apt-get install unixodbc -y \
 && apt-get install unixodbc-dev -y \
 && apt-get install freetds-dev -y \
 && apt-get install freetds-bin -y \
 && apt-get install tdsodbc -y \
 && apt-get install --reinstall build-essential -y

ADD ./requirements.txt /var/www/requirements.txt
RUN pip install -r requirements.txt
ADD ./ /var/www/
RUN pip install gunicorn


RUN groupadd -g $GROUP_ID www && \
    useradd -r -u $USER_ID -g www www -s /bin/sh

USER www

EXPOSE 5000

CMD [ "gunicorn", "-w", "1", "--bind", "0.0.0.0:5000", "run"]
