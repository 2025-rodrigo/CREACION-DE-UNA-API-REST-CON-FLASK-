# CREACION-DE-UNA-API-REST-CON-FLASK-
El presente proyecto consiste en la creación de una API REST utilizando el framework Flask y una base de datos SQLite. el objetivo principal es demostrar el uso práctico de los métodos —GET, POST, PUT y DELETE— para realizar operaciones CRUD sobre una colección de registros almacenados en una tabla. La API está diseñada siguiendo una estructura modular que separa la lógica del servidor (app.py), las operaciones de base de datos (db.py), el archivo SQL de creación de tablas (structureDB.sql) y el script opcional para generar la base de datos (create_db.py).

Durante el desarrollo del proyecto se implementaron endpoints capaces de responder en formato JSON, que sean capaces de manejar de la manera correcta diferentes escenarios como la creación de nuevos registros, la actualización de datos existentes, etc. Asimismo, se incluyeron mecanismos básicos de manejo de errores, como la validación de campos obligatorios, detección de identificadores duplicados y respuestas claras ante solicitudes incorrectas.

Para verificar el correcto funcionamiento de la API, se utilizaron pruebas realizadas con la herramienta Postman. Las capturas de estas pruebas se encuentran organizadas en carpetas individuales por cada tipo de método. de manera general, este proyecto permite comprender el flujo completo de desarrollo y prueba de una API REST sencilla, así como fortalecer el uso de Flask como herramienta para construir servicios web modernos y funcionales.

1. Método GET — Obtener información

el método GET permite recuperar todos los registros almacenados en la base de datos. cuando el cliente realiza una solicitud a la ruta:
GET /users

el servidor ejecuta una función que consulta la tabla correspondiente y devuelve una lista en formato JSON con todos los elementos registrados. En caso de no existir registros, se retorna una lista vacía. 

2. Método POST — Crear un nuevo registro

el método POST se utiliza para agregar un nuevo registro a la base de datos. El cliente envía datos en formato JSON a la ruta:
POST /users

incluyendo los campos requeridos (por ejemplo: id, name, email). La API valida que los datos estén completos y que el identificador no exista previamente. Si las condiciones se cumplen, el registro es insertado en la base de datos.

3. Método PUT — Actualizar un registro existente

el método PUT permite modificar los datos de un registro ya existente. La solicitud se envía a una ruta con el ID del recurso:
PUT /users/<id>

El cliente envía en el cuerpo JSON los campos a actualizar. La API verifica primero que el registro exista; si es así, procede a actualizar los datos indicados. Si el ID no se encuentra en la base de datos, se devuelve un error.

4. Método DELETE — Eliminar un registro

el método DELETE elimina un registro de la base de datos según su ID. La solicitud se realiza mediante:
DELETE /users/<id>

La API verifica que el registro exista y, de ser así, procede a eliminarlo permanentemente. Este método no requiere un cuerpo JSON, pues toda la información necesaria está contenida en la ruta.
