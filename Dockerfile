FROM ubuntu:20.04

ENV LANGUAGE=en_US.UTF-8 LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 DEBIAN_FRONTEND=noninteractive LC_CTYPE=en_US.UTF-8
RUN echo en_US.UTF-8 UTF-8 > /etc/locale.gen

RUN apt-get update \
    && apt-get install -qq -y \
        apt-utils \
        locales \
        lsb-release \
        curl \
        gnupg2 \
        runit \
        software-properties-common \
        libpq-dev \
        build-essential \
    && apt-get clean

RUN set -x \
    && apt-get update -qq && apt-get upgrade -qq \
    && locale-gen en_US.UTF-8 ru_RU.UTF-8 \
    && apt-get install -qq \
        bash-completion \
        gettext \
        htop \
        mc \
        nginx \
        openssl \
        postfix \
        python3.9 \
        python3-dev \
        python3-pip \
        postgresql-client-12 \
        screen \
        time \
    \
    && pip3 install --upgrade pip>=20 \
    && pip3 install poetry \
    && apt-get autoremove -qq


WORKDIR /opt/app
COPY . /opt/app

EXPOSE 80

RUN poetry install

RUN set -x \
    && find . -name '*.pyc' -delete \
    && find . -name '__pycache__' -type d | xargs rm -fr

CMD ["poetry", "run", "python3", "manage.py", "runserver"]
