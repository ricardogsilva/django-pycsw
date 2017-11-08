FROM geopython/pycsw

USER root

WORKDIR /home/pycsw/pycsw-frontend

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

RUN pip3 install . \
  && cd extra \
  && pip3 install .

WORKDIR /home/pycsw

RUN rm -rf pycsw-frontend

ENV DJANGO_SETTINGS_MODULE=config.settings.base

EXPOSE 8000

ENTRYPOINT ["gunicorn", "--access-logfile", "-", "--error-logfile", "-", "--bind=0.0.0.0:8000", "config.wsgi"]
