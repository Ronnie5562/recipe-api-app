#!/usr/bin/env bash

# Automate the process of running the tests
docker-compose run --rm app sh -c "python manage.py test"