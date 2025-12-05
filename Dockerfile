# 1️⃣ Use a lightweight Python image
FROM python:3.12-slim

# 2️⃣ Set the working directory inside the container
WORKDIR /app

# 3️⃣ Copy project files into the container
COPY . .

# 4️⃣ Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Command to start the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

