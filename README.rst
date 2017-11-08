django-pycsw
============

A django app to integrate pycsw into django projects. Under construction...


Development with docker
-----------------------

Build the image and then launch it with the appropriate bind mounts

.. code:: bash

   docker build -t pycsw-frontend .

   docker run \
       --rm \
       --name pycsw-frontend \
       -p 8000:8000 \
       -v $PWD/src/djangopycsw:/usr/lib/python3.5/site-packages/djangopycsw:ro \
       -v $PWD/extra/pycsw_frontend/config:/usr/lib/python3.5/site-packages/config:ro \
       pycsw-frontend
