#!/bin/bash

gunicorn app.main:app --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000