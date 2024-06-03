FROM klakegg/hugo:ext as build
WORKDIR /opt

COPY . .
RUN git submodule init && git submodule update
RUN hugo



FROM nginx
COPY --from=build /opt/public/ /usr/share/nginx/html
