FROM python:3-alpine as publications
WORKDIR /opt
RUN mkdir /opt/content
RUN pip install pyorcid
COPY generate-papers-page.py .
RUN python generate-papers-page.py



FROM klakegg/hugo:ext as build
WORKDIR /opt

COPY . .
COPY --from=publications /opt/content/publications.md /opt/content/publications.md
RUN git submodule init && git submodule update
RUN hugo



FROM nginx
COPY --from=build /opt/public/ /usr/share/nginx/html
