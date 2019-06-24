## Usage
--Build the application image  ans set up the DB
```
git clone https://github.com/bharathnoddy/helloworldapi.git
docker build -t helloworldapi .
mkdir my-db
docker-compose up

```

`Application should be up at  localhost port 80 but on time DB steps needs to be taken care of before PUT or GET `
`http://localhost`


### One time DB steps
```
--Login to the mysql docker instance and fire the following commands
mysql -u admin -p       (get the password for the docker-compose file)
create table username
CREATE TABLE username (username VARCHAR(20) PRIMARY KEY, dob DATE);
```



##  Adding or updating entry
`POST /localhost/hello/<username> { "dob" : "1985-01-20" }`

## Getting username info
`GET /localhost/hello/<username>`


## Architecture
The architecture .jpg answers question no. 2 and which shows the basic AWS design of the components and the kubernetes architecture


## Deployment config:
This answers question no. 2 The chart folder and the Jenkins file defines how the Jenkins will make use of helm chart to deploy this application. It will be Rolling update so no downtime expected
