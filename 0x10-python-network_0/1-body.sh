#!/bin/bash
# Bash script that sends a GET request to the URL
curl -s -I GET $1 | grep -i HTTP/ | awk '{if ($2 == 200) curl -s $1}'
