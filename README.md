# HSTS Header Injection

## What is this?

## Install

```
git clone git@github.com:KwnyPwny/hsts-header-injection.git
cd hsts-header-injection
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Setup

### Certificates

* Create a directory for certificates:
```
mkdir certs && cd certs
```

* Create a certificate authority
```
openssl genrsa -aes256 -out my-ca.key 4096
openssl req -x509 -new -nodes -key my-ca.key -sha256 -days 1826 -out my-ca.crt
```

* Create a certificate signing request
```
openssl req -new -nodes -out poc.local.csr -newkey rsa:4096 -keyout poc.local.key

Country Name (2 letter code) [AU]:
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:hsts.local
Email Address []:
```

* Create the web server certificate

```
openssl x509 -req -in poc.local.csr -CA my-ca.crt -CAkey my-ca.key -CAcreateserial -out hsts.local.crt -days 365 -sha256
```

## Use

* Start both web servers:
```
sudo env "PATH=$PATH" python http-server.py
sudo env "PATH=$PATH" python https-server.py
```