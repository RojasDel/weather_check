#!/bin/bash

#Activar el entorno virtual
echo "Activando el entorno virtual..."
source venv/bin/activate

#Instalar dependencias
echo "Instalando dependencias..."
pip install -r requirements.txt 

#Ejecutar la aplicación CLI
echo "Ejecutando la aplicacion CLI..."
python cli_argp.py Roma json

#Mensaje final
echo "Ejecución completada con éxito."