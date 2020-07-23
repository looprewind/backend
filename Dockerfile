# Pull base image
FROM python:3.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /bluebox

# Install dependencies
COPY Pipfile Pipfile.lock /bluebox/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /bluebox/