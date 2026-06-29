FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chmod -R g=u /app
EXPOSE 8080
USER 1001
CMD ["python", "app.py"]
