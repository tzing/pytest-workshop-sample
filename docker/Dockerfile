FROM postgres:14-alpine

ENV POSTGRES_DB=db
ENV POSTGRES_PASSWORD=P@ssw0rd

COPY init.sql /docker-entrypoint-initdb.d/
