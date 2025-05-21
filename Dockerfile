# Debian Based Docker
FROM debian:latest

# Update and install necessary system packages
RUN apt update && apt upgrade -y && apt install -y git curl python3 python3-pip python3-venv ffmpeg

# Create and activate a virtual environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Upgrade pip and install wheel in the virtual environment
RUN pip install --upgrade pip wheel

# Copy requirements file
COPY requirements.txt /requirements.txt

# Install Python dependencies in the virtual environment
RUN pip install -U -r /requirements.txt

# Set up working directory and copy start script
RUN mkdir /RadioPlayerV3
WORKDIR /RadioPlayerV3
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Run the Radio Player Bot
CMD ["/bin/bash", "/start.sh"]
