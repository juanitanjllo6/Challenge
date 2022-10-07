1.Clonar el repositorio https://github.com/juanitanjllo6/Challenge.git en la maquina local con git clone

2.En la terminal ingresar a la ruta Challenge
Es necesario activar el entorno virtual creado, para lo cual desde una terminal, se debe ejecutar source venvflask/bin/activate 

3.Es necesario instalar las librerías necesarias para que nuestro desarrollo funcione, para esto, en la termial ejecutar pip install requirements.txt

4.En una terminal en la ruta challenge se tiene el archivo main.py, allí es necesario ejecutarlo python3 main.py
Se tienen 4 clases creadas:

    1. Se debe crear inicialmente la tabla en la base de datos a partir del endpoint publico que se consumirá, para esto, en el navegador, se debe ejecutar : http://localhost:5000/create

    2. Se debe poblar la base de datos a partir del endpoint consumido, para esto, en el navegador, se debe ejecutar : 
    http://localhost:5000/insert

    3. Si se quieren listar todos los datos de la base de datos, se debe poner en un navegador: http://localhost:5000/tasks
    
    4. Si se quieren filtrar solo los datos de un id especifico, se debe poner en un navegador: http://localhost:5000/tasks/<id>, donde <id> se reemplaza por el id que quiero buscar, ejm     http://localhost:5000/tasks/1

