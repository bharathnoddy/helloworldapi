##Usage
--Build the application image
`docker build -t helloworldapi .`

--Create DB directory
`mkdir my-db`

--Bring up the application
`docker compose up`

--one time DB set up
--log into the mysql DB and use the following commands to create tables:
```
create table username
CREATE TABLE username (username VARCHAR(20) PRIMARY KEY, dob DATE);
```

`Application should be up at  localhost port 80`

##Adding or updating entry
`POST /localhost/hello/<username> { "dob" : "1985-01-20" }`

##Getting username info
`GET /localhost/hello/<username>`
