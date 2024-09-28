# Security Policy

## Supported Versions

Any Python version after 3.11.1

python3 -m pip install oracledb --upgrade --user

## Password do access DB

To avoid the need to expose passwords, the script has been adapted to find the password from an OS env. Use it like the following:

export PYTHON_DB_PASSWORD="Senha de acesso" ; pyhton3-healthcheck_sgad.py

## Reporting a Vulnerability

You can submit a vunerability issue by creating in Issues tab.
