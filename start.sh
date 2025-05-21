#!/bin/bash
echo "Cloning Repo, Please Wait..."
git clone https://github.com/AsmSafone/RadioPlayerV3.git /RadioPlayerV3
cd /RadioPlayerV3

echo "Starting Bot, Please Wait..."
/venv/bin/python main.py
