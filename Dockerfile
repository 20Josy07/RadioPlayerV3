# Debian Based Docker
FROM debian:latest

# Update and upgrade the system
RUN apt update && apt upgrade -y

# Install required packages
RUN apt install git curl python3 python3-pip ffmpeg -y

# Ensure pip is installed and upgraded using the correct Python version
RUN python3 -m pip install --upgrade pip

# Copy requirements file
COPY requirements.txt /requirements.txt

# Install Python dependencies from requirements.txt
RUN pip3 install -U -r /requirements.txt

# Create working directory and copy start script
RUN mkdir /RadioPlayerV3
WORKDIR /RadioPlayerV3
COPY start.sh /start.sh

# Run the Radio Player Bot
CMD ["/bin/bash", "/start.sh"]
