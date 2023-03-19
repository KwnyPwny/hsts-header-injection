# CA

openssl genrsa -aes256 -out my-ca.key 4096
openssl req -x509 -new -nodes -key my-ca.key -sha256 -days 1826 -out my-ca.crt

# CSR
openssl req -new -nodes -out poc.local.csr -newkey rsa:4096 -keyout poc.local.key

Country Name (2 letter code) [AU]:
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:hsts.local
Email Address []:

# Cert
openssl x509 -req -in poc.local.csr -CA ../ca/my-ca.crt -CAkey ../ca/my-ca.key -CAcreateserial -out poc.local.crt -days 730 -sha256

# hsts-header-injection
