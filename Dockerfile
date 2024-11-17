# Gunakan image Python sebagai base
FROM python:3.10-slim

# Set lingkungan kerja di dalam container
WORKDIR /app

# Salin requirements.txt ke dalam container
COPY new_requirements.txt .

# Install dependencies dari requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r new_requirements.txt

# Salin seluruh proyek ke dalam container
COPY backend_flask_project/ .

# Tentukan environment variable untuk Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=development  
# Atau 'production' jika sudah di produksi

# Expose port yang akan digunakan oleh Flask
EXPOSE 5000

# Jalankan aplikasi Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
