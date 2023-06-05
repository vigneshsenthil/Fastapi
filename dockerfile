FROM mysql/mysql-server

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ENV MYSQL_DATABASE=DB \
    MYSQL_ROOT_PASSWORD=password \
    MYSQL_ROOT_HOST=%

ADD schema.sql /docker-entrypoint-initdb.d

EXPOSE 3306