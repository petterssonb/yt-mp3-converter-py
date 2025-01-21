FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    ffmpeg \
    libxcb-xinerama0 \
    libx11-xcb-dev \
    python3-tk

RUN apt-get install -y build-essential libssl-dev libffi-dev

RUN pip install --upgrade pip setuptools wheel

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8888


CMD ["python3", "main.py"]