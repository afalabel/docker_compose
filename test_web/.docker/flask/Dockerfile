FROM centos:7
RUN yum update -y && \
    yum install -y epel-release

RUN yum install -y centos-release-scl

RUN yum install yum install sudo python-pip python-devel gcc pcre-devel openssl-devel zlib-devel -y

RUN pip install --upgrade pip

RUN pip install virtualenv

RUN adduser flask

CMD ["su","-","flask","-c","mkdir -p /home/flask/myproject"]
CMD ["su","-","flask","-c","cd /home/flask/myproject"]

CMD ["su","-","flask","-c","virtualenv myprojectenv"]

CMD ["su","-","flask","-c","source /home/flask/myprojectenv/bin/activate"]

RUN pip install uwsgi flask

COPY ./flask_project_code/myproject.py /home/flask/myproject/myproject.py
COPY ./flask_project_code/wsgi.py /home/flask/myproject/myproject.py
COPY ./flask_project_code/myproject.ini /home/flask/myproject/myproject.ini


#CMD ["su","-","flask","/bin/uwsgi --ini /home/flask/myproject/myproject.ini"]

#ENTRYPOINT ["su","-","flask","/bin/uwsgi --ini /home/flask/myproject/myproject.ini"]



ENTRYPOINT [ "sh", "-c","while true; do sleep 12; done"]
