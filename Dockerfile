# syntax = docker/dockerfile:experimental
FROM        python:3.9-slim

# Language, Timezone
ENV         LANG C.UTF-8
ENV         TZ Asia/Seoul
RUN         ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY        .deploy/pgdg.list /tmp/
ADD         https://www.postgresql.org/media/keys/ACCC4CF8.asc /tmp/

RUN         --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt \
            apt -y update &&\
            apt -y install gnupg &&\
            apt-key add /tmp/ACCC4CF8.asc &&\
            apt -y remove gnupg &&\
            apt -y autoremove

RUN         cp /tmp/pgdg.list /etc/apt/sources.list.d/ &&\
            apt -y update &&\
            apt -y dist-upgrade &&\
            apt -y install postgresql-client-14 &&\
            apt -y autoremove

# requirements
ARG         requirements
COPY        $requirements /tmp/$requirements
RUN         --mount=type=cache,target=/root/.cache/pip \
            pip install -r /tmp/$requirements

# Log폴더 생성
RUN         mkdir /var/log/gunicorn &&\
            mkdir /var/log/celery

COPY        .   /srv/
WORKDIR     /srv/app

EXPOSE      8000
CMD         python manage.py shell_plus --ipython
