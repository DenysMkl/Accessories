#!/usr/bin/env sh

cd accessories

uvicorn accessories_api:app --host 0.0.0.0