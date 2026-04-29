# Usamos una imagen ligera de Python
FROM python:3.11-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de dependencias e instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de los archivos (app.py y respuestas.json)
COPY . .

# Exponemos el puerto donde corre Flask
EXPOSE 5000

# Comando para arrancar la app
CMD ["python", "app.py"]
