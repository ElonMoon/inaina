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

