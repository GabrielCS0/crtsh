# CrtSh

This is a tool to automate the search for subdomains on the website [crt.sh](https://crt.sh/).

See it in action:

```
$ python3 crtsh.py -d hackerone.com   

[*] Searching crt.sh for subdomains of hackerone.com.
[*] Found 12 unique subdomains of hackerone.com.

links.hackerone.com
api.hackerone.com
managed.hackerone.com
sts.hackerone.com
forwarding.hackerone.com
go.hackerone.com
support.hackerone.com
events.hackerone.com
docs.hackerone.com
gslink.hackerone.com
www.hackerone.com
info.hackerone.com
```

## Setup

1) Clone the repository

```
git clone https://github.com/GabrielCordeiroDev/crtsh.git
```

2) Install the dependencies in a virtualenv

```
cd crtsh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

More features will be added soon.
