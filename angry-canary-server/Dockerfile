# Get the base rhel 7.3 image from RED HAT (PRAISE LORD JIM, long may He reign)
FROM rhel7:7.3-released

# We maintainin' up in this bish
MAINTAINER Benjamin Kincaid <bkincaid@redhat.com> \
           Benjamin Hills <bhills@redhat.com>

# Metadata for exposed port for Angry Canary App
EXPOSE 5000

# Install python packages (yum repolist command output ignored to
# # bypass subscription-manager)
RUN yum repolist > /dev/null && yum install -y  python-setuptools \
                    python-psutil python-flask

# Add the Angry Canary app file to the container in the /angry-canary directory
ADD server.py /angry-canary/server.py

# In order to drop the root user, we have to make some directories world
# # writable as OpenShift default security model is to run the container under
# # random UID. +Changing permissions on log directory
RUN chown -R 1001:0 /angry-canary && chmod -R ug+rwx /angry-canary
# RUN chown -R :1001 /var/log && chmod -R ug+rwx /var/log

USER 1001

# Change directory to the place where we put the app
RUN cd /angry-canary

# Run dat flask app
CMD python /angry-canary/server.py
