# ip

## installation on centos 7

### install, enable and start mongodb
```
echo "[mongodb-org-4.2]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/7/mongodb-org/4.2/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-4.2.asc" > /etc/yum.repos.d/mongodb-org-4.2.repo

yum install mongodb-org
systemctl enable mongod
systemctl start mongod
```

### install epel-release, python36 and pip; upgrade pip3.6
```
yum install epel-release
yum install python36
yum install python36-pip
pip3.6 install --upgrade pip
```

### virtualenv install, create and activate
```
pip3.6 install virtualenv
virtualenv ip
cd ip
source bin/activate
```

### git clone ip
```
git clone https://github.com/odrolit/ip
```

### install requirements
```
pip3.6 install -r ip/requirements.txt
```
