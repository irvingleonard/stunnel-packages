FROM centos:7

RUN yum -y upgrade
RUN yum -y install rpmdevtools yum-utils

WORKDIR /root
RUN rpmdev-setuptree
VOLUME ["/root/rpmbuild/SRPMS", "/root/rpmbuild/RPMS"]

WORKDIR /root/rpmbuild/SPECS/
COPY stunnel.spec ./

RUN yum-builddep -y stunnel.spec
RUN spectool -g -R stunnel.spec

ENTRYPOINT ["rpmbuild", "-ba", "stunnel.spec"]
