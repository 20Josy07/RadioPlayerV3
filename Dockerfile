# Debian Based Docker
FROM debian:latest

# Update and upgrade the system
RUN apt update && apt upgrade -y

# Install required packages, including python3-venv for virtual environments
RUN apt install git curl python3 python3-pip python3-venv ffmpeg -y

# Create and activate a virtual environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Upgrade pip within the virtual environment
RUN pip install --upgrade pip

# Copy requirements file
COPY requirements.txt /requirements.txt

# Install Python dependencies from requirements.txt in the virtual environment
RUN pip install -U -r /requirements.txt

# Create working directory and copy start script
RUN mkdir /RadioPlayerV3
WORKDIR /RadioPlayerV3
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Run the Radio Player Bot
CMD ["/bin/bash", "/start.sh"]
