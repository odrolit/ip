# ip

## installation on centos 7

### install mongodb
```
echo "[mongodb-org-4.2]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/4.2/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-4.2.asc" > /etc/yum.repos.d/mongodb-org-4.2.repo

yum install mongodb-org pip3
```

### start and enable mongodb
systemctl enable mongod

systemctl start mongod

### install python36
yum install python36

### install pip
yum install pip3

### install virtualenv
pip3 install virtualenv

### create virtualenv
virtualenv ip

### activate virtualenv (default 
cd ip

source bin/activate

### git clone ip
git clone https://github.com/odrolit/ip

### install requirements
pip3 install -r ip/requirements.txt
