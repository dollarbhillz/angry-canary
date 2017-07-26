# Get the base rhel 7.3 image from RED HAT (PRAISE LORD JIM, long may He reign)
FROM rhel7:7.3-released

# We maintainin' up in this bish
MAINTAINER Benjamin Kincaid <bkincaid@redhat.com> \
           Benjamin Hills <bhills@redhat.com>

LABEL com.redhat.component="angry-canary-worker-docker"
LABEL name="angry-canary-worker-docker"
LABEL version="0.1"
LABEL io.k8s.description="Project UpShift Angry Canary worker container image"
LABEL summary="Worker container image for Project UpShift Angry Canary"
LABEL io.k8s.display-name="Angry Canary Worker"
LABEL description="Project UpShift Angry Canary worker container image"


# Install python packages (yum repolist command output ignored to
# # bypass subscription-manager)
RUN yum repolist > /dev/null && yum install -y python-setuptools \
                    python-psutil stress

# Upgrade pip
# RUN pip install --upgrade pip

# Install python sys package
# RUN pip install sys

# Add the flask app file to the container in the /usr/bin directory
ADD busy_work.py /angry-canary/busy_work.py

# In order to drop the root user, we have to make some directories world
# # writable as OpenShift default security model is to run the container under
# # random UID. +Changing permissions on log directory
RUN chown -R 1001:0 /angry-canary && chmod -R ug+rwx /angry-canary
# RUN chown -R :1001 /var/log && chmod -R ug+rwx /var/log

USER 1001

# Change directory to the place where we put the worker
RUN cd /angry-canary

# Run dat worker
CMD python /angry-canary/busy_work.py
