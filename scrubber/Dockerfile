FROM python:3.10.6

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /app

ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ADD ./ /app/

CMD ["python", "scrubbedy.py"]