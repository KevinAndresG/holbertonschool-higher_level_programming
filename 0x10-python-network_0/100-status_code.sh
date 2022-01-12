#!/bin/bash
# pint the status code
curl -L -I -s -o /dev/null $1 -w '%{http_code}\n'
