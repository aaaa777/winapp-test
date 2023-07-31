# winapp-test

# requirements
python3.10
python-venv


# setup

```
python3.10 -m venv env
python ./utils --setup
```

# build

```
python ./utils --build --production
```

# sign exe

```
*** create certification and private key files under /cert dir ***
openssl pkcs12 -export -inkey cert/code.key -in cert/code.csr -out cert/code.pfx
signtool sign /f cert/code.pfx /t http://timestamp.digicert.com /fd SHA256 /p exampleexampleexample dist/app3.exe
```