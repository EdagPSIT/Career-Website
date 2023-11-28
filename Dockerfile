FROM python:3.9

# Install build essentials
RUN apt-get update && apt-get install -y build-essential && apt-get clean

WORKDIR /src/careerapp

# Copy the Flask app code into the container
COPY . .

RUN pip install --upgrade pip

# Install Flask
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]