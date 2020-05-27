FROM alpine:3.8
MAINTAINER Gavaskar Rathnam, gavaskar.rathnam@genesys.com
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache
	
ADD . /code
WORKDIR /code

RUN pip install gunicorn
RUN pip install -r requirements.txt

ENV FLASK_APP=todolist.py
ENV FLASK_ENV=development
ENV SECRET_KEY="this should not be checked into git"

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "todolist:app"]
