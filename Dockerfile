# 基础镜像
FROM python:3-alpine

# 维护者信息
LABEL maintainer="twoyang0917@gmail.com"

# app 所在目录
WORKDIR /usr/local/web/
ADD . /usr/local/web/

# 安装 app 所需依赖
RUN sed -i 's@http://dl-cdn.alpinelinux.org@https://mirrors.ustc.edu.cn@g' /etc/apk/repositories \
    && apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev
RUN cd /usr/local/web/ && pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN apk del build-deps && rm -rf /var/cache/apk/*

EXPOSE 8080
CMD python manage.py runserver 0.0.0.0:8080
