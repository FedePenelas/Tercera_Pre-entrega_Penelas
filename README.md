# Tercera_Pre-entrega_Penelas.
Mediante git init se inició la carpeta raíz a partir de la cual todo lo que esta dentro fue pusheado a este repositorio.

Se crea proyecto de Django y su correspondiente aplicación.

Corriendo la web con python manage.py runserver, parado en la carpeta del prouecto e ingresando con el navegador a 127.0.0.1:8000 vamos a la página principal de AdoptAR, una web de mascotas en adopción. 

En la página inicial hay información, botones y barra de contacto configuradas. En el pie de página tambien están editados los textos, incluso el About Us y contact.

Cada boton lleva a una dirección distinta, donde se puede evidenciar la herencia de un template base que es el que tiene el index, página inicial.

La página forma parte de mi proyecto AdoptAR, el cual tiene la aplicación AdoptAR_pagina, donde se encuentran todos los componentes de la misma.

Allí dentro, en views.py se ven las vistas con las direcciones, en urls.py las correspondientes urls según la vista.

Dentro de la carpeta static, por ejemplo, se encuentran los templates correspondientes a cada vista.

En models.py estan migrados todos los modelos y vinculados a forms.py. Los modelos tienen la función __str__ para que aparezcan con el nombre específico en el panel de administración de la aplicación web.

En las secciones donar, transito y dar en adopción, se encuentran los formularios. Los mismos son completados y enviados, y este movimiento se registra en la base de datos y los modelos cargados.

Por una falta de tiempo, ya que estoy entregando el trabajo hoy día domingo 11/06/2023 porque tengo un viaje de trabajo en donde no podré continuar trabajando en la entrega, no llego a terminar el formulario. Teniendo casi 3 días menos para hacerlo, entrego el trabajo incompleto. Los formularios están, de hecho en las vistas se ven, y al completarlos nos lleva a una vista de confirmación. El problema hasta hoy, en el cual (insisto) no tengo tiempo para resolver, es que lo ingresado en esos formularios se guardan en la base de datos, pero luego no puedo traermelos con el uso del formulario de busqueda.

Puedo generar nuevos registros, pero al momento de querer traerlos con el formulario de búsqueda, lo cual era una consigna del trabajo, me queda en blanco. Seguramente sea un error de codigo y falta de ver el detalle, porque al ser varias páginas casi idénticas hice mucho copy paste, el cual no tengo tiempo de revisar. Son las 20:20 del día domingo 11/06 y estoy a punto de irme a Córdoba, Argentina.

Lamento no poder finalizar la entrega del trabajo.
