#!/bin/bash

echo "Using pip version:"
pip --version

INSTALL_DIR="local_lib"
LOG_FILE="install.log"

echo "Installing path.py in $INSTALL_DIR"
pip install --upgrade --target="$INSTALL_DIR" path.py > "$LOG_FILE" 2>&1

if [ $? -eq 0 ]; then
    echo "Installation successful!"
    echo "Running Python program"
    PYTHONPATH="$INSTALL_DIR" python3 my_program.py
else
    echo "Installation failed. See $LOG_FILE for details."
    exit 1
fi
