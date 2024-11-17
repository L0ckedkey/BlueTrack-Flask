FROM python:3.10-slim

WORKDIR /app

# COPY new_requirements.txt .
COPY requirements.txt .

RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir \
    numpy \
    scikit-learn \
    joblib \
    tensorflow
RUN pip install --no-cache-dir -r requirements.txt

COPY backend_flask_project/ .

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
