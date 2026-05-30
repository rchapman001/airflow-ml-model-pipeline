FROM apache/airflow:3.0.3

USER airflow

# Copy the requirements file into the container
COPY requirements.txt /tmp/requirements.txt
# Install the packages
RUN pip install --no-cache-dir -r /tmp/requirements.txt