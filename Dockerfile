FROM python:3-alpine as build
WORKDIR /opt
COPY . .

RUN pip install pyorcid
RUN python generate-papers-page.py

RUN apk add --no-cache hugo
RUN hugo



FROM nginx
COPY --from=build /opt/public/ /usr/share/nginx/html
