FROM python:3-alpine as publications
WORKDIR /opt
RUN mkdir /opt/content
RUN pip install pyorcid
COPY generate-papers-page.py .
RUN python generate-papers-page.py



FROM alpine:latest as build
WORKDIR /opt
RUN apk add --no-cache hugo

COPY . .
COPY --from=publications /opt/content/publications.md /opt/content/publications.md
RUN hugo



FROM nginx
COPY --from=build /opt/public/ /usr/share/nginx/html
