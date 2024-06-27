FROM python:3.12.2

WORKDIR /app

# Instalar Rust y Cargo

# Copiar los archivos de la aplicación y los requisitos
COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./app ./app

EXPOSE 8000

# Comando para correr la aplicación
CMD ["sh", "-c", "python app/services/train_model.py && uvicorn app.main:app --host 0.0.0.0 --port 8000"]