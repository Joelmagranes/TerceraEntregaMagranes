# TerceraEntrega Magranes

**Aplicación Django para gestionar autos, sucursales y ventas.**

## Tabla de contenidos
- Descripción
- Funcionalidades
- Instalación y ejecución

## Descripción
Este proyecto es una aplicación web desarrollada con Django que permite gestionar información de **autos**, **sucursales** y **ventas**, incluyendo autenticación de usuarios, perfiles con avatar y permisos especiales para acciones administrativas.

## Funcionalidades

### 🔐 Autenticación y perfiles
- Registro de usuarios.
- Inicio y cierre de sesión.
- Edición de perfil.
- Carga de avatar (visible en el navbar).
- Cambio de contraseña.
- Vista **About Me**.
- Permisos: solo usuarios **staff** pueden eliminar sucursales.

### 🚗 Autos
- CRUD completo (crear, listar, editar, eliminar).
- Búsqueda por modelo.
- Validaciones básicas.
- Gestión desde el panel de administración.

### 🏢 Sucursales
- CRUD completo.
- Búsqueda por ciudad.
- Eliminación protegida: solo usuarios **is_staff** pueden borrar.
- Vista de confirmación antes de eliminar.


### 🧭 Navegación y estructura
- Página de inicio con accesos rápidos.
- Navbar dinámico según el estado del usuario.
- Templates con herencia y diseño consistente.
- Archivos estáticos correctamente configurados.

## Instalación y ejecución
-Clonar el repositorio 
-Clonar el repositorio 
-Crear y activar un entorno virtual: 
  -py pipenv shell 
  -py manage.py runserver 
  -Ejecutar migraciones: 
  -py make migrations 
  -py manage.py migrate 
  -Ejecutar el servidor: 
  -py pipenv shell 
  -py manage.py runserver

## LINK del Video que demuestra que la pagina funciona: 
https://drive.google.com/drive/folders/1EJm-jan5DFNnBFH3wgtqFRIVvEEvzyKn
