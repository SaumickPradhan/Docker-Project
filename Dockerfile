# Use a lightweight base image
FROM python:alpine

# Set working directory
WORKDIR /app

# Copy the Python script and input files into the container
COPY ReadingFiles.py /app/ReadingFiles.py
COPY TextFiles/IF.txt /home/data/IF.txt
COPY TextFiles/Limerick-1.txt /home/data/Limerick-1.txt

# Run the Python script when the container launches
CMD ["python", "ReadingFiles.py"]
