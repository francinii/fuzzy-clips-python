# Usa una imagen base de Python (puedes ajustar la versión según tus necesidades)
FROM python:3.10-slim

# Actualiza los paquetes
# e instala libgomp && apt-get install -y libgomp1
RUN apt-get update

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . .

# Instala las dependencias de Python desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Ejecuta el script de Python cuando se inicie el contenedor
CMD ["python","main.py"]
