# inaina

## Requirements

- Python >= 3.8
- Poetry
- pre-commit
- PostgreSQL

## Installation

### DB

```shell
brew install postgresql
createuser inaina -s -P
createdb inaina --owner=inaina template=template0 --lc-collate='C'
```

### Others

```
poetry install
pre-commit install
```



## Server Settings (Oracle Cloud)

### DB

**Install PostgreSQL (https://www.postgresql.org/download/linux/ubuntu/)**

```shell
# Create the file repository configuration:
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists:
sudo apt-get update

# Install the latest version of PostgreSQL.
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
sudo apt-get -y install postgresql
```

**Create superuser, database**

```shell
sudo -i -u postgres
createuser -s -P <username>
createdb <db_name> --owner <username> --template template0 --lc-collate 'C';
```

**DB Settings**

```
# sudo vi /etc/postgresql/13/main/postgresql.conf
listen_addresses = '*'
port = <change port>

# sudo vi /etc/postgresql/13/main/pg_hba.conf
host    all             all             0.0.0.0/0               password
```

**Allow Port**

```
sudo iptables -I INPUT 1 -p all --dport <changed_port> -j ACCEPT
```

