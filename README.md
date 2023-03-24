# proyecto_final_python_vasquez

## Proyecto Final Coder House - Python
- Comisión: 48405
- Alumno: Hugo Abraham Vasquez
- Nombre del Proyecto: Blog Ecónomico y Financiero

### Versión
1.0

Para poder correr este proyecto es necesario tener instalado python 3.9 o superior. 

### Paquetes necesarios para la instalación
Desde la terminal correr el siguiente comando
```bash
pip3 install django
```

### Cargar datos de pruebas

Para terminal bash en windows/linux/macos:
```bash
python3 manage.py shell < seed_data.py
```

Para terminal cmd/powershell en windows:
Primero entrar al shell de django con
```bash
python3 manage.py shell
```
Una vez en el shell hacer import seed_data
```bash
Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> import seed_data
```

### Para poder correr el servidor 

Desde la terminal correr el siguiente comando

```bash
python3 manage.py runserver
```

### Descripción del Proyecto
Página Web destinada a usuarios que desean leer o publicar noticias de economía o finanzas en un blog, en el caso que el usuario dese publicar noticias debera realizar un registro e ingresar datos de registro (usuario y contraseña).

Para navegar en la pagina Web el usuario podra acceder desde el menu nav a:
INICIO: Donde podra acceder a las 6 publicaciones mas recientes e ir al detalle de cada una de estas.
NOSOTROS: Donde podra ver una reseña o ABOUT de la pagina.
PUBLICACIONES: Donde se depliega una lista de todas las publicaciones y se podra acceder al detalle si asi se desea.
ENVIAR MENSAJE: Donde se podra enviar un mensaje a alguno de los usuarios registrados.
INGRESAR: Donde se podra acceder si YA eres un usuario registrado.
REGISTRO: Donde te deberas registrar si todavia NO eres un usuario registrado

Una vez te registres o ingreses con tus datos de usuario y contraseña iras a la pagina de MIS PUBLICACIONES donde veraz las publicaciones que haz realizado hasta la fecha y tendras las opciones de ir a: DETALLE, ACTUALIZAR O BORRAR dicha publicacion. Tambien podras ir al link PUBLICACIONES pero solo estaras habilitado para actualizar o borrar tus propias publicaciones, en las demas solo podras acceder al detalle.

Tambien al ingresar o registrarte se habilita el link de NUEVA PUBLICACION donde podras subir al portal una nueva publicacion. De la misma forma podras accede al link MENSAJES, donde podras ver si tienes mensajes y borrarlos si asi lo deseas. Finalmente al ingresar o registrarte como usuario tendras acceso al link ACTUALIZAR AVATAR que te permitira agregar o modifcar un avatar o foto en tu perfil.

Presionando el boto salir, haras un logout y podras seguir navegando la pagina sin estar logueado.

Nota: La opción de actualizar y borrar publicaciones solo le está permitido al autor de la publicación.

### Acontinuacion se suministran nombres de usuarios y contraseñas ya creadas con las que se realizaron las pruebas de la pagina:

### NOTA: usuario admin y su contraseña 123 corresponden  al superusuario del proyecto
- usuario: admin
contraseña: 123

- usuario: eva
contraseña: 9876543va

- usuario: tiago
contraseña: 3456789go

- usuario: lucas
contraseña: 9876543lu

- usuario: catalina
contraseña: 3456789ca


### Tecnología Utilizada
- Front-End
- HTML 5
- CSS 3
- Javascript ES6
- Bootstrap 5.3
- Back-End
- Python 3.11.2
- Django 4.1.7

### Video Demostración
https://drive.google.com/file/d/1UAhwQjAHrTNYs2SVAbdA8rJUYlyfbSSR/view?usp=share_link

