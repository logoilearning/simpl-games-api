# Python 3.6 base
FROM python:3.6
RUN pip install --upgrade pip

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

ADD . /code/

ENV PYTHONPATH /code:$PYTHONPATH
ENV PYTHONUNBUFFERED 1

# Start and listen on 8100
EXPOSE 8100
CMD ["/bin/bash", "start.sh"]
