
# Use an official Python runtime as a parent image
FROM dockerhub.timeweb.cloud/library/python:3.11-slim

# Set the working directory inside the container
WORKDIR /project

# Copy the requirements file into the container at /project
COPY requirements.txt /project/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Map /root/project to /project
VOLUME ["/root/project:/project"]

# Set the working directory to /project
WORKDIR /project

# Run app.py when the container launches
CMD ["python3", "app.py", "prod"]
