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

Luego, en los botones Buscar Transito por ejemplo, al ingresar el nombre de un registrado, devuelve los datos ingresados.

Por una falta de tiempo, ya que estoy entregando el trabajo hoy día domingo 11/06/2023 porque tengo un viaje de trabajo en donde no podré continuar trabajando en la entrega, no llego a terminar el formulario. Teniendo casi 3 días menos para hacerlo, entrego el trabajo incompleto. El problema hasta hoy, en el cual (insisto) no tengo tiempo para resolver, es que las barras que por lo general están al pie de la página, al ingresar datos ahi no se guardan en ningún lado. La idea era que se guarden e incorporen en el modelo Persona, y que luego al ir al boton Buscar Persona se pueda ver. Por la falta de tiempo mencionada es que al llenar el campo al pie de pagina no pasa nada, lo mismo si vamos a Buscar Persona y queremos ingresar algo no se podrá.

Seguramente sea un error de codigo y falta de ver el detalle, porque al ser varias páginas casi idénticas hice mucho copy paste, el cual no tengo tiempo de revisar. Son las 21:00 del día domingo 11/06 y estoy a punto de irme a Córdoba, Argentina. Salgo a las 23:00.

Lamento no poder finalizar la entrega del trabajo.
