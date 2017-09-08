# Welcome to the Angry Canary Project
This project was originally a Red Hat internal project, but I'm open-sourcing
as much as I can to share with the greater community as a whole.

## Required Packages/Tools

- oc
- I originally used an internal build system, so building the container image
  is an exercise left to the reader.

## Main files in repo (inside angry-canary-server subdir)
- Dockerfile
Dockerfile for building the container

- server.py
Source code for the Flask app running on the server pod

## Extra stuff

- angry-canary-work.yml
This is a preliminary format for Jenkins Jobs definitions to be updated on the
Angry Canary Jenkins Master

- delete_jnlp_slaves_oc.py
Script for deleting runaway slave pods on OpenShift

- delete_base_pods_oc.py
Script for deleting runaway base pods on OpenShift

- postgresql-imagestream.yml
This is the image stream for the version of Postgres we are using for the
database pod.

### Inside angry-canary-server subdir. . .

- db_test_script.py
Adds a few example rows into each table inside the database.
