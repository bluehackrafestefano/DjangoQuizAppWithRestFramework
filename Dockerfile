# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.10.5-alpine3.16

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
# # This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

# # This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# create root directory for our project in the container
RUN mkdir /flight

# Set the working directory to /flight
WORKDIR /flight

# Copy the current directory contents into the container at /flight
ADD . /flight/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt