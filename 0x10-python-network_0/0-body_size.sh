#!/bin/bash
# sends a request to an url
curl -s "$1" | wc -c
