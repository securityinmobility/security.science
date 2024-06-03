FROM klakegg/hugo:latest as build
WORKDIR /opt

COPY . .

RUN hugo



FROM nginx
COPY --from=build /opt/public/ /usr/share/nginx/html
