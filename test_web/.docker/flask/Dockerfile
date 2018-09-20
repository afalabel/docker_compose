FROM centos:7
RUN yum update -y && \
    yum install -y epel-release

RUN yum install -y centos-release-scl

RUN yum install yum install python-pip python-devel gcc -y

RUN pip install --upgrade pip

RUN pip install virtualenv

RUN adduser flask

CMD ["mkdir -p /root/flask/myproject"]
CMD ["cd /root/flask/myproject"]

RUN pip install uwsgi flask

COPY ./flask_project_code/myproject.py /root/flask/myproject/myproject.py
COPY ./flask_project_code/wsgi.py /root/flask/myproject/wsgi.py
COPY ./flask_project_code/myproject.ini /root/flask/myproject/myproject.ini


CMD uwsgi --ini /root/flask/myproject/myproject.ini


#COPY ./flask_project_code/run.sh /tmp/run.sh
#CMD chmod +x /tmp/run.sh
#CMD source /tmp/run.sh
