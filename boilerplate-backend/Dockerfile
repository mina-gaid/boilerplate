# Use Python 3.9 as base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a directory for our code
RUN mkdir /code
WORKDIR /code

# Upgrade pip and copy requirements file
RUN pip install --upgrade pip
COPY requirements.txt /code/

# Install dependencies from requirements file
RUN pip install -r requirements.txt

# Copy project code to container
COPY . /code/

# Change directory to boilerplate and collect static files
RUN cd boilerplate && \
    python manage.py collectstatic --noinput

# Make Database migrations
RUN python manage.py migrate

# Expose port 8000 to the host
EXPOSE 8000

# Run the Django server on container startup
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
