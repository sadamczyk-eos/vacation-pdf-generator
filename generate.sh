#!/bin/sh

docker run -it --rm -v $PWD/out:/usr/src/app/out vacation-pdf-generator ./main.py "$@"
