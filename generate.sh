#!/bin/zsh

docker run -it --rm --user 1000 -v $PWD/out:/usr/src/app/out vacation-pdf-generator ./main.py "$@"
