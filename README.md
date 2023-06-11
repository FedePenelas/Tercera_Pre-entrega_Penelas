# Tercera_Pre-entrega+Penelas
Corriendo la web con python manage.py runserver e ingresando con el navegador a 127.0.0.1:8000 vamos a la página principal de AdoptAR, una web de mascotas en adopción. 
En la página inicial hay información, botones y barra de contacto configuradas.
Cada boton lleva a una dirección distinta, donde se puede evidenciar la herencia de un template base que es el que tiene el index, página inicial.
La página forma parte de mi proyecto AdoptAR, el cual tiene la aplicación AdoptAR_pagina, donde se encuentran todos los componentes de la misma.
Allí dentro, en views.py se ven las vistas con las direcciones, en urls.py las correspondientes urls según la vista.
Dentro de la carpeta static, por ejemplo, se encuentran los templates correspondientes a cada vista.
En models.py estan migrados todos los modelos y vinculados a forms.py
En las secciones donar, transito y dar en adopción, se encuentran los formularios. Por una falta de tiempo, ya que estoy entregando el trabajo hoy día domingo 11/06/2023 porque tengo un viaje de trabajo en donde no podré continuar trabajando en la entrega, no llego a terminar el formulario. Teniendo casi 3 días menos para hacerlo, entrego el trabajo incompleto. Los formularios están, de hecho en las vistas se ven, y al completarlos nos lleva a una vista de confirmación. El problema hasta hoy, en el cual (insisto) no tengo tiempo para resolver, es que lo ingresado en esos formularios no se guardan en ningún lado. No se ven reflejados los datos en el panel de administración, como tampoco en el archivo SQL.
Agoté instancias como CoderAsk, pregunta a compañeros, ChatGPT y revisión de las clases, pero se puede ver como el código para que los formularios interactúen con los modelos está presente pero los mismos no son registrados en ninguna parte.
