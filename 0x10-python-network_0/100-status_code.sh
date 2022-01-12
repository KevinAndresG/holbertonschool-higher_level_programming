#!/bin/bash
# pint the status code
curl --write-out "%{http_code}\n" -s --output /dev/null $1
