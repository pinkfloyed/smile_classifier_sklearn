# Use Ubuntu 20.04 as the base image
FROM ubuntu:20.04

# Install necessary dependencies and Python 3.11
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.11 python3.11-venv python3.11-dev python3-distutils curl wait-for-it && \
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3.11 get-pip.py && \
    rm get-pip.py

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install Python dependencies
RUN python3.11 -m pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Start FastAPI app
CMD ["wait-for-it", "db:3306", "--", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
