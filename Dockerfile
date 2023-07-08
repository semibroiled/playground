# syntax=docker/dockerfile:1


# Set base image as python
FROM python:3.11-alpine3.18

# Set working directory as default path
WORKDIR /app

# Copy requirements.txt into image and install dependencies
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# Copy all files into image now
COPY . .

# Run commands for when image is executed in container
# Specify host to make app visible
CMD [ "python", "-m", "main", '--upto', '10000']

