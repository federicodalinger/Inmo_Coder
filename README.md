Readme del Proyecto Inmo.Coder:

Curso: Python
Comision: 31100 

Integrantes: Federico La Volpe | Federico Walter Dalinger | Felipe Goicoechea

Landing page: http://127.0.0.1:8000/

Motivo del proyecto: 

Se trata de una pagina de administracion de una inmobiliaria. Podria tener caracter publico o privado, aunque eso queda a criterio del poseedor del sitio. Los datos de cada propiedad y clientes son los tipicos que se encuentran en operaciones inmobilirarias, indicados en los modelos (models.py), y ahi mismo las caracteristicas de c/u.

Acceder a la base de datos:

Superusuario: Nombre --> admin | Password --> admin
Ahi mismo se pueden ver los modelos mencionados, con las propiedades y clientes cargados.
Extra: usamos un def "str" para mejor visual de los datos en la base de datos.

    1. En la parte superior (head) se encuentran los botones desplegables que llevan a las diversas .html.
        1.1. CARGA: Hay 4 botones de carga con formulario para ingresar informacion segun los modelos (clases) en models.py. Esto requiere estar logueado para poder realizarse.
            1.1.1. Para la carga de fechas, se debe respetar el formato YYYY-MM-DD (por defecto seteado la fecha actual, como "initial=datetime.date.today" dentro de los modelos en models.py).
        1.2. BUSQUEDA: Asi mismo, hay 4 botones para buscar esta informacion (tambien por formulario).
            1.2.1. Si bien en la clase se explico que para la busqueda y el resultado de busqueda se utilizaran dos HTML independientes, utilizando "jinja" reutilizamos el mismo html, para ambas funciones. Estos son: "casas_buscar.html", "clientes_buscar.html", "cocheras_buscar.html" y "departamentos_buscar.html".
        1.3. LISTADO: Por último, hay también 4 botones que listan una información preliminar de los casos cargados en la base de datos por modelo (esto es, en el listado de departamentos se visualizan todos los departamentos cargados en la base de datos). Pegado a cada valor, se encuentran 3 botones que permiten visualizar más detalles de cada caso y, con los permisos correspondientes, se encuntran los botones para eliminar y editar cada caso. Además, en el listado de cada modelo se incorpora también un botón que permite agregar un nuevo caso del modelo seleccionado.
    
    2.El botón de "Usuarios" permite acceder al sitio con usuario y contraseña ya logueados o registrar un usuario nuevo. Una vez clie, se despliegan las opciones para editar perfil, editar avatar, enviar un mensaje a otro usuario y realizar el logout de la web.

    3. Si se aprieta sobre el boton "Acerca de mi" se muestra una imagen y el nombre de cada uno de los creadores de la página.
    
    4. Queda para completar en la siguiente entrega:
        3.1. Contenido en pagina de inicio (landing page) --> AGREGAR DESCRIPCION 
        3.2. Contenido de paginas de carga --> Buscar la forma para que se puedan cargar imagenes. -->
        3.3. Contenido de paginas de busqueda --> Buscar la forma para que se puedan ver las imagenes.

    5. Github (repositorio online) --> https://github.com/federicodalinger/Inmo_Coder.git
    
