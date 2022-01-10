#!/bin/bash
# Bash script that sends a GET request to the URL
grep -i HTTP/ | awk '{if ($2 == 200) print "Route 2"}' | curl -s $1
