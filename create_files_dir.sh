#!/bin/bash

# Define the roles directories
roles=("base" "centservers" "dbservers" "rhelservers" "webservers")

# Loop through each role and create the files directory
for role in "${roles[@]}"; do
  mkdir -p "roles/$role/files"
done

