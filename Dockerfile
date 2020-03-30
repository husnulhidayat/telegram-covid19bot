# BASE NODE
FROM centos:centos7 as base
MAINTAINER husnul_hidayat@outlook.com
RUN yum -y update && yum clean all
RUN mkdir -p ~/BOT_home
COPY . ~/BOT_home





FROM centos:centos7
MAINTAINER husnul_hidayat@outlook.com
RUN yum -y update && yum clean all

CMD ./ngrok authtoken 1ZfUdue1780pknaDflV2AZe144Z_6TVtnitrfh9UjCLXiyUoo
CMD ./ngrok http 5000



EXPOSE 5000/TCP

CMD ["sleep", "infinity"]

