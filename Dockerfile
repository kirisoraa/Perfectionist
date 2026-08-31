FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY perfectionist/ perfectionist/

EXPOSE 26279
ENV GRADIO_SERVER_NAME=0.0.0.0
ENV GRADIO_SERVER_PORT=26279

CMD ["python", "-m", "perfectionist.main"]