#!/bin/bash
export FLASK_ENV=development
export FLASK_APP=src/app.py
flask run --host=0.0.0.0 --port=5000 