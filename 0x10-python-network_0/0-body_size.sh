#!/bin/bash

# Check if URL is provided as argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request using curl and get the size of the response body in bytes
response=$(curl -s -o /dev/null -w "%{size_download}" "$1")

# Display the size of the response body
echo "Size of the response body: $response bytes"

