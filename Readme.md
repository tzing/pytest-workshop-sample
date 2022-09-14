# Demo

A sample project for PyTest workshop


Prepare environment:

```bash
brew install postgresql
poetry install

cd docker/
docker build . -t pytest-workshop-db
docker run -itd --rm -p 15432:5432 pytest-workshop-db
```
