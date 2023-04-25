# Description

Chambers Full-stack Boilerplate

## Features

- Stores files of any type and name
- Stores files at any URL
- Does not allow interaction by non-authenticated users
- Allows users to store multiple revisions of the same file at the same URL
- Allows users to fetch any revisions of any file

---

# Development

Developed using Python / Django and JavaScript / Aurelia

# Setup

There are two methods of running both the front-backend and front-end apps.

## Method 1 (Recommended)

Follow the instructions found in the relevant README.md files in each app on how to setup and run.

## Method 2 (Not Recommended)

Run both apps using Docker.

Step 1: Ensure you have the latest Docker desktop client installed and running in the background.

Step 2: Open the terminal & cd into the main project directory root folder that contains both apps -

```
cd /path/to/project
```

Step 2: Run the following command to setup and run the applications within Docker -

```
docker-compose up
```

This will build the images and start the containers for the backend and frontend services. Building the images take a while so please be patient.

Step 3: Once the containers are up and running, you can access the Boilerplate (frontend) web application by opening a web browser and navigating to http://localhost:8080.

Note that the backend API is running on port 8000, which is exposed by the backend service and mapped to port 8000 on the host machine. The frontend is running on port 8080, which is exposed by the frontend service and mapped to port 8080 on the host machine.

Step 4: To stop the containers, you can use the following command:

```
docker-compose down
```

This will stop and remove the containers, but it will not remove the images or volumes. If you want to remove everything, you can use the '--volumes' and '--rmi' options, like this:

```
docker-compose down --volumes --rmi all
```