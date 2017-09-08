# Welcome to the Angry Canary Project

This project is an RCM internal project to test the UpShift environment for
stability and uptime.


## Required Packages/Tools

- oc
- rhpkg

## Main files in repo (inside angry-canary-server subdir)
- Dockerfile
Dockerfile for building in dist-git, also stored in the
angry-canary-server-docker repo in dist-git

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

- server-imagestream.yml
Configuration for pulling server container image from OSBS

- db_test_script.py
Adds a few example rows into each table inside the database.
