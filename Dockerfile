# Use NVIDIA's official CUDA base image with Ubuntu 22.04
FROM nvidia/cuda:12.2.0-base-ubuntu22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Fix potential `_apt` permission issues
RUN chmod -R 755 /var/lib/apt/lists && chmod 755 /etc/apt/sources.list.d

# Install CUDA toolkit
RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-toolkit-12-2 \
    libnccl2=2.19.3-1+cuda12.2 \
    libnccl-dev=2.19.3-1+cuda12.2 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python and dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    gnupg2 \
    software-properties-common \
    build-essential \
    libssl-dev \
    libffi-dev \
    libbz2-dev \
    zlib1g-dev \
    libreadline-dev \
    libsqlite3-dev \
    python3.10 \
    python3.10-venv \
    python3-pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set Python 3.10 as default
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1 && \
    update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

# Install Python libraries
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Install Hugging Face CLI and authenticate
RUN pip install --no-cache-dir huggingface-hub transformers torch
ARG HUGGINGFACE_TOKEN
RUN huggingface-cli login --token "$HUGGINGFACE_TOKEN"

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Expose the FastAPI port
EXPOSE 8001

# Command to run the FastAPI server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001", "--workers", "1"]

