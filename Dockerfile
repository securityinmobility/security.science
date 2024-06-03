FROM klakegg/hugo:alpine as build
WORKDIR /opt

COPY . .
RUN apk add git && git submodule init && git submodule update
RUN hugo



FROM nginx
COPY --from=build /opt/public/ /usr/share/nginx/html
