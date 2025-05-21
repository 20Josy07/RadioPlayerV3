# Debian Based Docker
FROM debian:latest

# Update and install necessary system packages, including python3-venv
RUN apt update && apt upgrade -y && apt install -y git curl python3 python3-pip python3-venv ffmpeg

# Create and activate a virtual environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Upgrade pip in the virtual environment
RUN pip install --upgrade pip

# Copy requirements file
COPY requirements.txt /requirements.txt

# Install Python dependencies in the virtual environment
RUN pip install -U -r /requirements.txt

# Copy all application files to the working directory
COPY . /RadioPlayerV3/

# Set up working directory
WORKDIR /RadioPlayerV3
RUN chmod +x /RadioPlayerV3/start.sh

# Run the Radio Player Bot
CMD ["/RadioPlayerV3/start.sh"]
