# personal_planner

## Requirements

The following packages need to be installed before running the project:

1. Python(3)
2. Docker

## Setting up .env

Before running the docker container, the user needs to set up their .env file:

```
# Django settings
SECRET_KEY=  ###################################### Secret key you need to set up 
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

# MySQL settings
MYSQL_ROOT_PASSWORD= ########### Your root password
MYSQL_DATABASE=personal_planner_mariadb
MYSQL_USER= ############# a db user name
MYSQL_PASSWORD= ####### a dn user password
```

## Running the docker container

To run the docker container you need to run the following commands:

```
docker-compose build
docker-compose up

# OR
docker-compose up --build

# To run it quietly
docker-compose up -d

```

Note that if the user and password don't work when trying to run the container you need to give the privilege:

```
# First start the docker container quietly
docker-compose up -d

# Then search for the id of the mysql db container
docker ps

# Then run the mysql command
docker exec -it <container_id> mysql -u root -p

# Grand privileges to the user
CREATE USER 'MYSQL_USER'@'%' IDENTIFIED BY 'MYSQL_PASSWORD!';
GRANT ALL PRIVILEGES ON project_name_mariadb.* TO 'MYSQL_USER'@'%';
FLUSH PRIVILEGES;

# You need to replace MYSQL_USER and MYSQL_PASSWORD to the ones in your .env file

# If the USER already exists but doesn't have privileget, run the following command before
DROP USER 'MYSQL_USER'@'%'
```

To check out the result go to http://localhost:8000/