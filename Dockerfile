# Stage 1: Builder
FROM python:3.12-slim AS builder

# Set the working directory
WORKDIR /src

# Copy the pyproject.toml and other necessary files to the container
COPY pyproject.toml README.md LICENSE /src/

# Copy the rest of the application code to the container
COPY . /src

# Install build system dependencies and build the project
RUN pip install --upgrade pip
RUN pip install hatch hatchling
RUN hatch build -t wheel

# Stage 2: Runtime
FROM python:3.12-slim

# Set the working directory
WORKDIR /src

# Copy the built wheel from the builder stage
COPY --from=builder /src/dist/*.whl /src/

# Install the built wheel
RUN pip install /src/*.whl

# Set the entrypoint for the container
ENTRYPOINT ["bept"]
