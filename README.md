# REST API server
## Description

This project provides python based REST API server to host certain queries for the database. It uses Cassandra as db-backend and REDIS for key-value storage. This is intended for big data queries.

This project is under progress and APIs provided are work in progress and subject to changes.

## Install
To install python dependencies, please run:
```
  pip install -r requirements.txt
```

Make sure you run Cassandra and redis in background.

## Usage
###Load the data
Run the following command to load the data
```
python sync.db
```
This commands load the data presented in data folder into cassandra db. It creates 7 tables as mentioned in the report. Tables are then used for queries.

### Run API server
Run the following command to run the server
```
python main.py
```

This hosts an API server on port 8081.

## API Endpoints
> /user
> /users
> /counts
> /activity
> /subscribe
> /summary



