Readme del Proyecto Inmo.Coder:

Curso: Python
Comision: 31100 

Integrantes: Federico La Volpe | Federico Walter Dalinger | Felipe Goicoechea

Motivo del proyecto: 

Se trata de una pagina de administracion de una inmobiliaria como asi, un portal donde poder publicar blogs, y que los usuarios puedan verlos. Los datos de cada propiedad son los tipicos que se encuentran en operaciones inmobilirarias, indicados en los modelos (models.py), y ahi mismo las caracteristicas de c/u.

Acceder a la base de datos:

Superusuarios:  Nombre --> admin  | Password --> admin
                Nombre --> admin2 | Password --> administrador
                Nombre --> admin3 | Password --> administrador1234

Tareas Efectuadas:
    - Federico Dalinger:
        - Maquetado general del sitio (html, css y bootstrap)
        - Armado del CRUD del blog, implementado CKEditor, y pages.html.
        - Creacion de la pagina "acerca de mi"
        - Agregado un listado de lo ya entregado en primer entrega del proyecto, para modificar si es usuario registrado.
        - Agregado de notificaciones cuando ya no hay mas propiedades, y blogs en la base de datos.
        - Armado de CRUD de propiedades ya existentes en entrega previa.
        - Conversion de vistas basadas en clase (generadas por Felipe Goicoechea) a vistas basadas en funciones para mejor control.
        - Seteo para ocultar y mostrar botones segun si se esta logueado.
        - Solucion del error ante la modificacion de la contraseña de cada usuario.
        - Finalizacion de la app de mensajeria, incluyendo boton de borrado y de respuesta rapida (al emisor).
        - Generacion de casos de prueba, con su resolucion en su mayoria.
        - Grabacion del video explicativo.
        - Generacion de este readme con la descripcion del rol de cada integrante.
    
    - Federico La Volpe:
        - Inicio de App de mensajeria, tanto para enviar como para ver lo ya recibido.
        - Generacion de registro de usuarios.
        - Generacion de links para poder setear el avatar en cada uno de ellos.
        - Generacion del login y registro de cada usuario.
        - Apartado para modificacion de datos de cada usuario registrado.
        - Discretizacion de usuarios registrados como de publico general.
        - Definicion de cartel verde y rojo para distinguir si hay mensajes en bandeja de entrada.

    - Felipe Goicoechea:
        - Inicio de CRUD de propiedades con vistas basadas en clase (luego no es usado)
        - Llevar al inicio automaticamente desde http://127.0.0.1:8000/.
        - Generacion del login y registro de cada usuario.

    
