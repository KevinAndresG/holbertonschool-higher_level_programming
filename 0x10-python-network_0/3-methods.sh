#!/bin/bash
# display the server methods
curl -s -I -X OPTIONS $1 | grep -i allow: | cut -d " " -f 2-
