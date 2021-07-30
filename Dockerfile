FROM ubuntu:20.04

ENV LANGUAGE=en_US.UTF-8 LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -qq -y \
        apt-utils \
        locales \
        lsb-release \
        curl \
        gnupg2 \
        runit \
        software-properties-common \
#        build-essential \
#    && echo deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -sc`-pgdg main >> /etc/apt/sources.list.d/pgdg.list \
#    && curl https://www.postgresql.org/media/keys/ACCC4CF8.asc|apt-key add - \
#    && echo deb http://nginx.org/packages/mainline/ubuntu/ `lsb_release -sc` nginx > /etc/apt/sources.list.d/nginx-mainline.list \
#    && echo deb-src http://nginx.org/packages/mainline/ubuntu/ `lsb_release -sc` nginx >> /etc/apt/sources.list.d/nginx-mainline.list \
#    && curl https://nginx.org/keys/nginx_signing.key|apt-key add - \
    && apt-get clean

RUN add-apt-repository ppa:deadsnakes/ppa


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
        python3.9-dev \
        python3-dev \
        build-essential \
        python3-pip \
        screen \
        time \
    \
    && pip3 install --upgrade pip>=20 \
    && pip3 install poetry \
#    && BUILD_DEPS='build-essential python3-dev' \
#    && apt-get install --no-install-recommends -qq ${BUILD_DEPS} \
#    && apt-get purge -qq ${BUILD_DEPS} \

    && apt-get autoremove -qq


WORKDIR /opt/app
COPY . /opt/app

EXPOSE 80

RUN poetry install

RUN set -x \
    && find . -name '*.pyc' -delete \
    && find . -name '__pycache__' -type d | xargs rm -fr

CMD ["poetry", "run", "python3", "manage.py", "runserver"]