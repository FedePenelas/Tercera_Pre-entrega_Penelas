# Tercera_Pre-entrega_Penelas.
ACLARACION: Tanto las carpetas como el nombre del repositorio quedan como Tercera entrega, pero se encuentra dentro todo lo referido al proyecto final. Sucede que trabajé sobre la tercera entrega y por eso quedaron los nombres. A modo de precaución, van a permanecer de esta manera.

Dentro del archivo comprimido se encuentran los archivos relacionados al proyecto en lo que a codigo se refiere. Luego, en la carpeta llamada ARCHIVOS AGREGADOS, se encuentran los casos de prueba y el video explicativo.

Mediante git init se inició la carpeta raíz a partir de la cual todo lo que esta dentro fue pusheado a este repositorio.

Se crea proyecto de Django y sus correspondientes aplicaciones.

Corriendo la web con python manage.py runserver, parado en la carpeta del prouecto e ingresando con el navegador a 127.0.0.1:8000 vamos a la página principal de AdoptAR, una web de mascotas en adopción. 

En la página inicial hay información, botones y barra de contacto configuradas. En el encabezado junto a los botones se encuentran los botones Crear Cuenta e Iniciar Sesion, mediante los cuales se pone en funcionamiento todo lo referido a usuarios, cuentas y avatares. En el pie de página tambien están editados los textos, incluso el About Us y contact.

Cada boton lleva a una dirección distinta, donde se puede evidenciar la herencia de un template base que es el que tiene el index, página inicial.

La página forma parte de mi proyecto AdoptAR, el cual tiene la aplicación AdoptAR_pagina, donde se encuentran todos los componentes de la misma, y la aplicación AdoptAR_login donde se encuentra todo lo relacionado a los usuarios como crear cuentas, iniciar sesion, editar cuentas, borrarlas, asignar avatar, dejar comentarios, etc.

Allí dentro, en views.py se ven las vistas con las direcciones, en urls.py las correspondientes urls según la vista.

Dentro de la carpeta static, por ejemplo, se encuentran los templates correspondientes a cada vista. Los avatares también tienen su carpeta.

En models.py estan migrados todos los modelos y vinculados a forms.py. Los modelos tienen la función __str__ para que aparezcan con el nombre específico en el panel de administración de la aplicación web.

En las secciones donar, transito y dar en adopción, se encuentran los formularios. Los mismos son completados y enviados, y este movimiento se registra en la base de datos y los modelos cargados.

Luego, en los botones Buscar Transito por ejemplo, al ingresar el nombre de un registrado, devuelve los datos ingresados.

En cuanto al CRUD, la función misma de crear cuenta, eliminarla, editarla, hace que en todo lo relacionado a usuarios se encuentre plasmado.

Se pueden crear cualquier cantidad de usuarios, cada uno se puede asignar su propio avatar. Al iniciar sesion, se eliminan los botones Crear Cuenta e Iniciar sesion, y se reemplazan por el avatar y el nombre del usuario. Los mismos te acompañan en toda la navegación no importa en que vista te encuentres.

La carpeta de objetos prueba se adjuntará mediante un link a google drive. Se adjuntará también una carpeta con el video explicativo
