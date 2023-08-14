from python:3.8

# Change work directory
WORKDIR /app

# Install the application requirements
COPY ./requirements.txt .
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r ./requirements.txt

COPY . .

WORKDIR /app

# Run flask directly
CMD flask run --host="0.0.0.0"