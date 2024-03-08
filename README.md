# Test: Crear una API Básica con Flask y subirla a GitHub

## **EVALUACIÓN**
ESTE TEST SE EVALUARÁ DE DOS (2) MANERAS:
1. Se ejecutará el codigo en mi laptop oso jajajajaja
2. Se hará un test verbal para comprobar que entendió lo que hizo (en algun nivel)
 
## **DESCRIPCIÓN DEL TEST**

En este test, crearás una API básica utilizando Flask, un framework de Python, que permitirá manejar una lista de tareas pendientes (ToDo List). La API tendrá los siguientes endpoints:

1. **GET /tasks**: Devuelve una lista con todas las tareas pendientes.
2. **POST /tasks**: Crea una nueva tarea pendiente.
3. **PUT /tasks/<int:task_id>**: Actualiza una tarea pendiente específica.
4. **DELETE /tasks/<int:task_id>**: Elimina una tarea pendiente específica.

**Requisitos**

1. Tener Python instalado en tu sistema (versión 3.6 o superior).
2. Tener una cuenta de GitHub y acceso a un repositorio existente donde subirás el código.

**Pasos a Seguir**

1. **Instalación de Flask**
  - Abre tu terminal o línea de comandos.
  - Ejecuta el siguiente comando para instalar Flask: `pip install flask`

2. **Crear el Proyecto**
  - Crea una nueva carpeta para el proyecto, por ejemplo, `todo-api`.
  - Dentro de esa carpeta, crea un nuevo archivo llamado `app.py`.

3. **Configurar Flask**
  - Abre el archivo `app.py` en un editor de texto.
  - Importa Flask y crea una instancia de la aplicación Flask:

    ```python
    from flask import Flask, jsonify, request

    app = Flask(__name__)
    ```

4. **Definir las Tareas Pendientes**
  - Crea una lista vacía para almacenar las tareas pendientes:

    ```python
    tasks = []
    ```

5. **Implementar los Endpoints**
  - Implementa los endpoints utilizando las rutas y métodos HTTP correspondientes:

    ```python
    @app.route('/tasks', methods=['GET'])
    def get_tasks():
        return jsonify(tasks)

    @app.route('/tasks', methods=['POST'])
    def create_task():
        task = request.get_json()
        tasks.append(task)
        return jsonify(task), 201

    @app.route('/tasks/<int:task_id>', methods=['PUT'])
    def update_task(task_id):
        task = [task for task in tasks if task.get('id') == task_id]
        if not task:
            return jsonify({'message': 'Task not found'}), 404
        task[0].update(request.get_json())
        return jsonify(task[0])

    @app.route('/tasks/<int:task_id>', methods=['DELETE'])
    def delete_task(task_id):
        task = [task for task in tasks if task.get('id') == task_id]
        if not task:
            return jsonify({'message': 'Task not found'}), 404
        tasks.remove(task[0])
        return jsonify({'message': 'Task deleted'})
    ```

6. **Ejecutar la API**
  - Agrega el siguiente código al final del archivo `app.py` para ejecutar la API:

    ```python
    if __name__ == '__main__':
        app.run(debug=True)
    ```

7. **Probar la API**
  - Ejecuta el archivo `app.py` en tu terminal: `python app.py`
  - Verifica que la API esté funcionando correctamente utilizando una herramienta como Postman o curl.

8. **Subir el Código a GitHub**
  - Inicializa un nuevo repositorio Git en la carpeta del proyecto: `git init`
  - Agrega los archivos al área de preparación: `git add .`
  - Realiza el primer commit: `git commit -m "Inicial commit"`
  - Agrega el remoto del repositorio de GitHub existente: `git remote add origin <URL_DEL_REPOSITORIO>`
  - Sube los cambios al repositorio remoto: `git push -u origin master`

¡Felicitaciones! Has completado el test y creado una API básica con Flask, además de subirla a un repositorio de GitHub existente.