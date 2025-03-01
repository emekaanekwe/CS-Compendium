#!/bin/bash

# Default path for the command file
default_commands_file="./ml_ai.sh"

# Use the specified file if provided as an argument; otherwise, use the default
commands_file="${1:-$default_commands_file}"

# Error check if the command file does not exist
if [ ! -f "$commands_file" ]; then
  echo "Error: Command file '$commands_file' not found."
  exit 1
fi

# Read commands from the text file line by line
while IFS= read -r cmd; do
  echo "activating python ml_ai venv"
  eval "source ~/ml_ai/bin/activate"   # Execute the command
  sleep 1       # Wait for 1 second
done < "$commands_file"#!/bin/bash
