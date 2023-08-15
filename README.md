# Backend of the Notes app (Python + Flask + Docker + Supabase)
Make sure you have [Docker](https://www.docker.com/) installed and running

Create a .env file with the following variables
```bash
SUPABASE_URL=https://zdpbgrpmnmefompwoznp.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpkcGJncnBtbm1lZm9tcHdvem5wIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5MjAxNDA0MSwiZXhwIjoyMDA3NTkwMDQxfQ.GczgvzVgVJZZwS6YYdsvOMJY5y8IpfQvrm0uVWVjiEg
```
I know this is not good practice, but I will be deleting the project afterwards.

```bash
# Build the docker image
docker build -t flask .

# Run the container associated with that image
docker run --name flask -dp 5000:5000 flask

# To stop the container
docker stop flask

# To remove the container from your machine
docker rm flask
```

