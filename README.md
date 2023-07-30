## Ejecución local
- Declarar la base de datos: DATABASE_URL = 'DATABASE_URL'
- Ejecutar la aplicación: `python application.py`

## Ejecución con Docker
- Crear imagen = docker build -t apicafeteria .
- Ejecutar contenedor = docker run -d -e DATABASE_URL='DATABASE_URL' apicafeteria
