# Back-end application test

# Installation

## Using docker

```
docker build -t joyjet-cli .
```

## Using virtualenv

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Run application by command line

## Using docker

```
docker run --rm joyjet-cli python main.py --level 3
```

## Using virtualenv

```
python main.py --level 3
```


# Run tests

## Using docker

```
docker run --rm joyjet-cli python -m pytest tests
```

## Using virtualenv

```
pytest .
```

# Run lint

## Using docker

```
docker run --rm joyjet-cli flake8 /code
docker run --rm joyjet-cli pylint /code
```

## Using virtualenv

```
flake8 ../python-test
pylint ../python-test
```