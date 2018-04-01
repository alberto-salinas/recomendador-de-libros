


# Recomendador de Libros                

####  Sinopsis (una pequeña historia con algo de ficcion)

Demasiados libros en el mundo, el mundo escacea de un sistema capaz de
recomendar. Volumenes de libros son publicados cada año complicando
la decision del comprador, asi provocando que el cliente
pierda tiempo buscando articulos y reseñas. Lo que hubiera tomado unos 
minutos se convierte en una investigacion de tiempo completo.


#### Objetivo
Diseña un recomendador web de libros donde el usuario pueda ver sugerencias
disponibles dado un usuario. Se proveera un banco de datos en formato JSON. El formato es el siguiente:

```
	{
		“nombre_de_usuario” : {
			“libro1” : 3,
			“libro2” : 4,
			“libro3” : 4.3
		}
		...
		....
	}
```
#### Cliente
El cliente sera web utilizandose HTML, Javascript, y CSS. 
Usaremos Bootstrap como soporte de widgets facilitando el diseño. Este sera la ventana al mundo donde
usuarios podran interactuar con tu servicio.

#### Servicio de Recomendación
El servidor sera escrito en python. Utilizaremos la libreria FLASK para configurar
el servidor. Tendremos la liberatad de usar librerias de procesamiento de datos como
SciPy y Pandas para facilitar operaciones. Pero, que es un servidor? Un servidor es un programa con la abilidad
de comunicarse con el cliente. Este recibe pedidos del cliente que el servidor debe cumplir.

BASE DE DATOS
Usualmente un servicio de datos forma parte del stack. Este permite consultar subset de datos
dado un criterio usando lenguajes de datos como SQL

e.g. `SELECT gpa, last_name from Student;`

Pero para propositos academicos, usaremos un archivo JSON cual guardara la data motivando esta
aplicacion.

Preguntas?

Incluye una version minima de un servidor. Tambien se incluye Twitter Bootstrap para el diseño del cliente web.

Instrucciones para correr el servidor

1) Saca el repo de http://github.com
2) Entra al folder del repo.
3) Instala dependencias usando pip install -r requirements.txt
4) Corre el comando python panda-app.py