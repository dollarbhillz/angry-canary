# Get the base rhel 7.3 image from RED HAT (PRAISE LORD JIM, long may He reign)
FROM registry.access.redhat.com/rhel7.3

# We maintainin' up in this bish
MAINTAINER Benjamin Kincaid <bkincaid@redhat.com> Benjamin Hills <bhills@redhat.com>

# Metadata for exposed port for Flask App
EXPOSE 5000

# Add the epel 7 repo key and config and authenticate packages using key from www.getfedora.org; Add rhel 7 internal repo and extras internal repo
ADD epel.repo.key /etc/yum.repos.d/epel.repo.key
ADD epel-7.repo /etc/yum.repos.d/epel-7.repo
ADD rhel-7.repo /etc/yum.repos.d/rhel-7.repo
ADD rhel-7-extras.repo /etc/yum.repos.d/rhel-7-extras.repo

# Install python packages
RUN yum repolist > /dev/null && yum install -y  python-setuptools python-psutil python-flask

# Upgrade pip
# RUN pip install --upgrade pip

# Install Flask and psutil
# RUN pip install flask

# Set the Flask app environment variable to the name of the flask app
ENV FLASK_APP "/usr/bin/server.py"

# Add the flask app file to the container in the /usr/bin directory
ADD server.py /angry-canary/server.py

# Run dat flask app
CMD python /angry-canary/server.py
