# REST API server
## Description

This project implements a python based REST API server. It uses Cassandra as db-backend and REDIS for key-value storage. This is intended for big data queries.

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

`/user`
`/users`
`/counts`
`/activity`
`/subscribe`
`/summary`

## API documentation
REST APIs are documented in the code

## Examples

Find User by Id

`POST 'http://localhost:8081/user' -d { 'id': 2 }`

Find User By Email

`POST 'http://localhost:8081/user'  -d { 'email': 'test@gmail.com'}`

`POST 'http://localhost:8081/users' -d { 'city' : 'Seattle', company: 'Amazon' }`

`POST 'http://localhost:8081/counts' -d { 'domain' : 'mail.ru', 'city': 'San Francisco' }`

`POST 'http://localhost:8081/activity' -d {'date': '2017/03/02', company: 'Google' }`

`POST 'http://localhost:8081/subscribe' -d {'date': '2017/03/02', 'domain': 'spotify.com', 'event': 'subscribe' }`

`POST 'http://localhost:8081/summary' -d {'date' : '2017/03/02', 'company': 'Apple' }`



