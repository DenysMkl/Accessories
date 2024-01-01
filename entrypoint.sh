#!/usr/bin/env sh

if [ "$1" = "parse" ]; then
  cd parse
  python3 parse.py
else
  cd accessories
  uvicorn accessories_api:app --host 0.0.0.0 --port 8000
fi

