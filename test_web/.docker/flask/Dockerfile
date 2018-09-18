FROM centos:7
RUN yum update -y && \
    yum install -y epel-release

RUN yum install -y centos-release-scl

RUN yum install yum install python-pip python-devel gcc -y

RUN pip install --upgrade pip

RUN pip install virtualenv

RUN mkdir -p /opt/app/myproject
RUN cd /opt/app/myproject

RUN virtualenv myprojectenv

RUN source myprojectenv/bin/activate

RUN pip install uwsgi flask

COPY ./flask_project_code/myproject.py /opt/app/myproject/myproject.py
COPY ./flask_project_code/wsgi.py /opt/app/myproject/myproject.py
COPY ./flask_project_code/myproject.ini /opt/app/myproject/myproject.ini

#CMD uwsgi --ini /opt/app/myproject/myproject.ini
