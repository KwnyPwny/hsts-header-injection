# HSTS Header Injection

## What is this?
The HTTP Strict Transport Security header is meant to secure browsing, by forcing the browser to use HTTPS instead of HTTP.
Browsers cache the *freshest* HSTS policy information on behalf of an HSTS host (see RFC6797 Section 5.3)[https://www.rfc-editor.org/rfc/rfc6797#section-5.3].
The header `Strict-Transport-Security: max-age=0` deletes the HSTS policy for the given host.
This can be exploited when a web application has an HTTP header injection vulnerability, by deleting the HSTS policy and redirecting the victim to HTTP.
A cookie without the secure-flag or other sensitive data, like the authorization header, will be transmitted without encryption.

This repository demonstrates the attack by supplying a vulnerable web server.

## Install

Clone the repository and install the requirements.

```
git clone git@github.com:KwnyPwny/hsts-header-injection.git
cd hsts-header-injection
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Setup

Modern browsers only obey HSTS headers when the web servers deliver valid certificates.
Self-signed certificates do not seem to be enough in some cases.
Thus we need to create a certificate authority (CA) first, create a certificate signing request for hsts.local, sign the certificate as CA and trust the CA in our browser.

### Certificates

Create a directory for certificates:
```
mkdir certs && cd certs
```

Create a CA:
```
openssl genrsa -aes256 -out my-ca.key 4096
openssl req -x509 -new -nodes -key my-ca.key -sha256 -days 1826 -out my-ca.crt
```

Create a certificate signing request:
```
openssl req -new -nodes -out hsts.local.csr -newkey rsa:4096 -keyout hsts.local.key

Country Name (2 letter code) [AU]:
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:hsts.local
Email Address []:
```

Sign the certificate:
```
openssl x509 -req -in hsts.local.csr -CA my-ca.crt -CAkey my-ca.key -CAcreateserial -out hsts.local.crt -days 365 -sha256
```

### Import CA into browser

Search the browser's settings for `cert` or follow these instructions:

* Firefox (v111): Settings -> Privacy & Security -> Certificates -> View Certificates... -> Authorities -> Import... -> hsts-header-injection/certs/my-ca.crt

* Chromium (v111): Settings -> Privacy & Security -> Security -> Manage certificates -> Authorities -> Import -> hsts-header-injection/certs/my-ca.crt

## Use

Start both web servers:
```
sudo env "PATH=$PATH" python http-server.py
sudo env "PATH=$PATH" python https-server.py
```

----

*Copyright 2023, Konstantin.*