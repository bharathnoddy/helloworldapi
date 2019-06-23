## Usage
--Build the application image  ans set up the DB
```
git clone https://github.com/bharathnoddy/helloworldapi.git
docker build -t helloworldapi .
mkdir my-db
docker-compose up

```


### One time DB steps
```
create table username
CREATE TABLE username (username VARCHAR(20) PRIMARY KEY, dob DATE);
```

`Application should be up at  localhost port 80`

##  Adding or updating entry
`POST /localhost/hello/<username> { "dob" : "1985-01-20" }`

## Getting username info
`GET /localhost/hello/<username>`
