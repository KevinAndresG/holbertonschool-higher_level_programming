#!/bin/bash
# pint the status code
curl --write-out %{http_code} -s --no-keepalive --output /dev/null  $1
