# Ledger API

API REST hecha con Django para llevar el control de gastos de un usuario. Es mi primer proyecto y lo hice con un objetivo claro: terminarlo y desplegarlo antes de empezar mis estudios universitarios, para poder contruir suites de test completos, tanto backend como frontend automatizados mientras estoy estudiando, por eso el proyecto avanzará despacio pero constante.

## ¿Qué hace?

- Registro y login de usuarios (autenticación por sesión de Django)
- Crear, ver, editar y borrar gastos (`expenses`)
- Cada usuario solo puede ver y gestionar sus propios gastos
- Asignar gastos por categorías (`categories`)
- Asignar presupuestos por categorías (`budgets`)

##  Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Pytest
- Postman/Bruno

## 📦 Instalación en local

1. Clona el repo:
```bash
git clone https://github.com/JuanASanta/ledger-api.git
cd ledger-api
```

2. Crea el entorno virtual e instala dependencias:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Crea un archivo `.env` en la raíz del proyecto con tus variables (revisa `config/settings.py` para ver los nombres exactos que usa el proyecto):
```
SECRET_KEY=tu-secret-key
DEBUG=True
DB_NAME=ledger_db
DB_USER=postgres
DB_PASSWORD=tu-password
DB_HOST=localhost
DB_PORT=5432
```

4. Aplica las migraciones y levanta el servidor:
```bash
python manage.py migrate
python manage.py runserver
```

La API estará disponible en `http://localhost:8000/`

## 📍 Endpoints principales

> Nota: estos son los endpoints previstos, voy a ir actualizando esta tabla según los vaya cerrando.

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/api/register/` | Registrar un usuario nuevo |
| POST | `/api/login/` | Iniciar sesión |
| GET | `/api/expenses/` | Listar mis gastos |
| POST | `/api/expenses/` | Crear un gasto |
| GET | `/api/expenses/<id>/` | Ver un gasto concreto |
| PUT | `/api/expenses/<id>/` | Editar un gasto |
| DELETE | `/api/expenses/<id>/` | Borrar un gasto |
| GET | `/api/categories/` | Listar mis categorías |
| POST | `/api/categories/` | Crear una categoría |
| GET | `/api/categories/<id>/` | Ver una categoría concreta |
| PUT | `/api/categories/<id>/` | Editar una categoría |
| DELETE | `/api/categories/<id>/` | Borrar una categoría |
| GET | `/api/budgets/` | Listar mis presupuestos |
| POST | `/api/budgets/` | Crear un presupuesto |
| GET | `/api/budgets/<id>/` | Ver un presupuesto concreto |
| PUT | `/api/budgets/<id>/` | Editar un presupuesto |
| DELETE | `/api/budgets/<id>/` | Borrar un presupuesto |


## ✅ Estado del proyecto

En desarrollo activo. Es un proyecto pequeño a propósito, pensado para llevarlo hasta el final y tenerlo desplegado como parte de mi portfolio.

### Por hacer

Los pasos por hacer, así como nuevas funcionalidades y alcances se aúnan en el archivo ROADMAP.md. Esto, para tener un registro de todo lo que he avanzado sin hacer el README.md demasiado grande.

## 🙋 Sobre mí

Soy Juan Antonio, terminé el ciclo de DAW en 2025 y ahora mismo estoy compaginando el grado en Ingeniería Informática con la búsqueda de mi primera oportunidad como QA Automation Junior | Fullstack Junior | QA Manual. Este proyecto es parte de mi portfolio, ¡cualquier feedback es bienvenido!