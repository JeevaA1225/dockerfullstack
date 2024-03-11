# Use the official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements file
COPY ./requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose port
EXPOSE 5000

# Command to run the service
CMD ["python", "app.py"]



# # Use the official Python image
# FROM python:3.9

# # Set the working directory inside the container
# WORKDIR /app

# # Copy the requirements file into the container
# COPY ./backend/requirements.txt .

# # Install Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the Flask application code into the container
# COPY ./backend/app.py .

# # Copy the templates directory into the container
# COPY ./backend/templates ./templates

# # Expose port 5000 for the Flask application
# EXPOSE 5000

# # Command to run the Flask application
# CMD ["python", "app.py"]
