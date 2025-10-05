# Simple development environment for algorithms and data structures
FROM python:3.11-slim

# Install basic system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js (simple approach)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs

# Set working directory
WORKDIR /usr/src/app

# Install only essential Python packages for algorithms/data structures
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir \
        numpy \
        jupyter \
        ipykernel

# Install essential Node.js tools
RUN npm install -g typescript ts-node @types/node tsx tsconfig-paths

# Set environment variables
ENV PYTHONPATH=/usr/src/app
ENV NODE_ENV=development

# Default command
CMD ["/bin/bash"]