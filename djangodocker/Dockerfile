# Use an official Python runtime as a parent image
FROM python:3.12

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container at /code/
COPY ./requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /code/
COPY . .

# Expose the port that the application will run on
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]


# Create and activate a virtual environment
RUN python -m venv /venv

