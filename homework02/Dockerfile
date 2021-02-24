FROM centos:7.7.1908u

ENV LC_CTYPE=en_US.UTF-8
ENV LANG=en_US.UTF-8

RUN yum update -y
RUN yum install -y python3
RUN pip3 install petname==2.6

COPY generate_animals.py /code/generate_animals.py
COPY read_animals.py /code/read_animals.py

RUN chmod +rx /code/generate_animals.py && \
    chmod +rx /code/read_animals.py

ENV PATH "/code:$PATH"