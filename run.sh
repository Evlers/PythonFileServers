#!/bin/bash

cd /home/evlers/PythonFileServers
nohup python3 -u ./python/main.py > ./log/python_log 2>&1 &

