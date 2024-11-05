# Stage 1: Build the Node.js application
FROM node:14 AS node-build

# Set the working directory
WORKDIR /usr/src/app

# Stage 2: Build the Python application
FROM python:3.9 AS python-build

# Set the working directory
WORKDIR /usr/src/app

# Copy requirements.txt
COPY requirements.txt ./

# Install Python dependencies
#RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Stage 3: Create the final image
FROM python:3.9

# Set the working directory
WORKDIR /usr/src/app

# Copy the Python application from the second stage
COPY --from=python-build /usr/src/app .

# Install Node.js
RUN apt-get update && apt-get install -y nodejs npm

# Install TypeScript globally
RUN npm install -g typescript

# Define the command to run the app
CMD ["/bin/bash"]