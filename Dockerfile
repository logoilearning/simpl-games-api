From gladiatr72/just-tini:latest as tini

FROM revolutionsystems/python:3.6.5-wee-optimized-lto


ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=true

RUN pip install -U pip

COPY ./requirements.txt ./code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY --from=tini /tini /tini

ADD . /code/
WORKDIR /code

ENV PYTHONPATH /code:$PYTHONPATH

EXPOSE 8000

ENTRYPOINT ["/tini", "--"]

CMD ["gunicorn", "-c", "/code/gunicorn.conf", "config.wsgi"]


LABEL Description="Image for simpl-games-api" Vendor="Wharton" Version="0.7.20"
