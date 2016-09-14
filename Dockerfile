FROM ubuntu:16.06
MAINTAINER zekna <zsharpsquared@gmail.com>

RUN apt-get update && apt-get install -yq \
      python3 \
      python3-setuptools

RUN apt-get clean && rm -rf /var/lib/apt/lists* /tmp/* /var/tmp/*
RUN easy_install3 pip
RUN pip3 install -U setuptools
ADD . /app
RUN cd /app; pip3 install -r requirements.txt

EXPOSE 80
CMD ["/usr/local/bin/gunicorn", "server:app"]
