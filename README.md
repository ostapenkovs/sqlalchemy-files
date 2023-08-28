## Dockerized Flask web application with PostgreSQL to demo binary file upload and download.

### A user is able to upload as many files as they wish, see a list of all files in the database, and download a chosen file.

*app.py*
- Contains all back-end code and logic.

*templates*
- Contains front-end HTML / CSS / Jinja.

*Docker-related*
- Dockerfile and docker-compose.yml are the recipies specifying what our Docker container will have and do.

*Getting started*
1. "make build" builds the Docker image;
2. "make run" runs the web application and database;
3. "make clean" removes containers and locally-stored files related to containers.
