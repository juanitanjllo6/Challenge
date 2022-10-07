1.Clonar el repositorio en la maquina local con " git clone https://github.com/juanitanjllo6/Challenge"
 
2.En la terminal ingresar a la ruta Challenge
Es necesario activar el entorno virtual creado, para lo cual desde una terminal, se debe ejecutar " source venvflask/bin/activate "

3.Es necesario instalar las librerías necesarias para que nuestro desarrollo funcione, para esto, en la termial ejecutar 
 " pip install requirements.txt "

4.En una terminal en la ruta challenge se tiene el archivo init.py, es necesario ejecutarlo " python3 ./init.py " para establecer la conexion a la base de datos, crear la tabla e ingestar la data consumida desde el endpoint de terceros.

5.En la misma ruta challenge se tiene el archivo main.py, allí es necesario ejecutarlo " python3 ./init.py " con el fin de observar los endpoint creados para que sean consumidos por los servicios internos de nuestra compañía

    Se tienen 2 endpoints, se recomienda usar google chroome e instalar la extension JSON Formatter:

            1. Si se quieren listar todos los datos de la base de datos, se debe poner en un navegador: http://localhost:8080/data
    
            2. Si se quieren filtrar solo los datos de un id especifico, se debe poner en un navegador: 
            http://localhost:8080/data/<id>, donde <id> se reemplaza por el id que quiero buscar, ejm:   
            http://localhost:8080/data/1

