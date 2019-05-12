# dockerMongoDB
Template of how to integrate mongodb with docker and store/backup/restore some dummy data.

## What is the purpose of these scripts?
To show how to run a mongodb instance in a docker container and how to access it from another container using python.

## Requirements
For these scripts to work you will need the following on your system:
* docker
* docker-compose

## To run the script you need to make them executable running the following command for each of them:
```
chmod +x <SCRIPT-NAME>
```

## Instructions
1. First thing you should do is to start, create and run the 2 containers from the 'docker-compose' file. You can do it manually using:
  
  ```
  docker-compose up
  ```
  Or you can run the 'docker-compose-script' (which I used for quicker debugging) by using:
  ```
  ./docker-compose-script
  ```

2. Right now you database container is up and running and has been populated with fake data (db:fake-data, collection:fake) by running a python script in the client container 
which then exited.

3. To backup all the data from db 'fake-data' we will use mongodump with the --gzip parameter which will compress the data before storing it. To do 
that you will need to run the following command:
```
./backup-script fake-data
```
After the process is complete you will get the backup files saved in the 'clientScript/fake-data' folder on your local system.
