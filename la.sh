#!/bin/bash
export PATH=$PATH:$(pwd)
rm littlealch.log
touch littlealch.log
python3 littlealch.py &> littlealch.log
echo "Done"
