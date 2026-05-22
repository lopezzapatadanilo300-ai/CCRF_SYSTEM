# CCRF System — Sistema de Gestión para Iglesias

Sistema web de gestión administrativa para la Centro Cristiana de Restauracion para la familia (CCRF), desarrollado con Django y orientado a la administración de sedes, miembros, finanzas e inventario mensual.

---

## Descripción del Proyecto

CCRF System es una aplicación web Full Stack que permite al Pastor Central gestionar múltiples sedes de una iglesia, y a cada Pastor de Sede administrar su propia congregación de forma independiente. El sistema incluye módulos de miembros, finanzas (ingresos y gastos), inventario mensual con reportes exportables, y un panel de reportes con ranking de diezmadores.

### Funcionalidades principales

- Autenticación con roles: Pastor Central y Pastor Sede
- Gestión de sedes y usuarios del sistema
- CRUD completo de miembros por sede
- Registro de movimientos financieros: diezmos, ofrendas, primicias, acción de gracias y gastos
- Dashboard con resumen de ingresos y gastos del mes
- Inventario mensual con envío de reportes al Pastor Central
- Exportación de reportes a PDF y Excel
- Ranking de diezmadores por año
- Diseño responsive con interfaz profesional

---

## Tecnologías Usadas

| Capa | Tecnología |
|---|---|
| Backend | Python 3.x + Django 6.x |
| Frontend | HTML5, CSS3, JavaScript |
| Base de Datos | MySQL (producción) / SQLite (desarrollo) |
| Exportación | ReportLab (PDF), OpenPyXL (Excel) |
| Estilos | CSS personalizado + Bootstrap 5 |
| Control de versiones | Git + GitHub |
| Despliegue | Render |

---

## Estructura del Proyecto

```
CCRF_SYSTEM/
├── ccrf_system/          # Configuración principal Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                 # Aplicación principal
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── dashboard_central.html
│   │   ├── dashboard_sede.html
│   │   ├── miembros.html
│   │   ├── finanzas.html
│   │   ├── inventario.html
│   │   ├── sedes.html
│   │   └── reportes.html
│   ├── models.py
│   ├── views.py
│   └── admin.py
├── .env.example
├── requirements.txt
└── manage.py
```

---

## Instrucciones de Instalación

### Requisitos previos

- Python 3.10 o superior
- pip
- Git
- MySQL (opcional, para producción)

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/CCRF_SYSTEM.git
cd CCRF_SYSTEM
```

### 2. Crear y activar el entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / Mac
python -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Copia el archivo de ejemplo y edítalo:

```bash
cp .env.example .env
```

Edita `.env` con tus datos (ver sección siguiente).

### 5. Aplicar migraciones

```bash
python manage.py migrate
```

### 6. Crear superusuario (Pastor Central)

```bash
python manage.py createsuperuser
```

> Luego entra al admin (`/admin`) y asigna el rol `pastor_central` al usuario creado.

### 7. Correr el servidor

```bash
python manage.py runserver
```

Abre tu navegador en `http://127.0.0.1:8000`

---

## Configuración de Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
# Entorno: 'production' para MySQL, cualquier otro valor usa SQLite
DJANGO_ENV=development

# Solo necesario si DJANGO_ENV=production
DB_NAME=nombre_base_datos
DB_USER=usuario_mysql
DB_PASSWORD=contraseña_mysql
DB_HOST=host_mysql
DB_PORT=3306

# Clave secreta de Django (genera una nueva en producción)
SECRET_KEY=tu_secret_key_aqui
```

> **Nota:** El archivo `.env` nunca debe subirse a GitHub. Está incluido en `.gitignore`.

### Generar una SECRET_KEY nueva

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## Despliegue en Render

1. Conecta tu repositorio de GitHub en [render.com](https://render.com)
2. Crea un nuevo **Web Service**
3. Configura las variables de entorno en el panel de Render:
   - `DJANGO_ENV` = `production`
   - `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
   - `SECRET_KEY`
4. En **Build Command** coloca:
   ```
   pip install -r requirements.txt && python manage.py migrate
   ```
5. En **Start Command** coloca:
   ```
   gunicorn ccrf_system.wsgi:application
   ```

---

## Roles del Sistema

| Rol | Permisos |
|---|---|
| Pastor Central | Gestión total: sedes, usuarios, miembros, finanzas, inventario, reportes globales |
| Pastor Sede | Gestión de su sede: miembros, finanzas, inventario propio |

---

## Credenciales de Prueba

```
Usuario: pastor_central
Contraseña: (la que configuraste al crear el superusuario)
```

---

## Autor

Desarrollado por Danilo lopez y Alan
Programa: Ingeniería de Sistemas — Herramientas Computacionales
Universidad Cooperativa de Colombia — 2026
