#!/bin/bash
# pint the status code
curl -LI $1 -o /dev/null -w '%{http_code}\n' -s
