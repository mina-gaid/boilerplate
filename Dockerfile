# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the required packages
RUN pip install -r boilerplate-backend/requirements.txt

# Copy the backend source code into the container
COPY boilerplate-backend /app/boilerplate-backend/

# Set the environment variable for the Django settings module
# ENV DJANGO_SETTINGS_MODULE=boilerplate-backend.settings.production

# Collect static files
RUN python boilerplate-backend/manage.py collectstatic --noinput

# Make Database migrations
RUN python boilerplate-backend/manage.py migrate

# Copy the frontend source code into the container
COPY boilerplate-frontend /app/boilerplate-frontend/

# Install the Aurelia CLI globally
RUN npm install -g aurelia-cli

# Install the frontend dependencies
RUN cd boilerplate-frontend && npm install

# Build the frontend assets
RUN cd boilerplate-frontend && au build --env prod

# Expose the ports that the apps are running on
EXPOSE 8000
EXPOSE 8080

# Start the backend and frontend apps using supervisor
RUN apt-get update && apt-get install -y supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]
