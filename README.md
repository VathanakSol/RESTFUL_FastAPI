# FastAPI User & Product Management System

A modern, well-structured FastAPI application demonstrating best practices for building scalable web APIs with comprehensive user and product management functionality.

## 🚀 Features

- **RESTful API** - Clean API endpoints for user and product management
- **Database Integration** - SQLAlchemy ORM with configurable database support
- **Admin Interface** - HTML templates for user and product administration
- **Modular Architecture** - Well-organized code structure following FastAPI best practices
- **Environment Configuration** - Secure configuration management with Pydantic Settings
- **Authentication Ready** - Security module prepared for authentication implementation
- **Partial Updates** - Advanced PATCH operations supporting selective field updates
- **Full CRUD Operations** - Complete Create, Read, Update, Delete functionality for all entities

## 📁 Project Structure

```
├── app/
│   ├── api/
│   │   └── deps.py              # API dependencies
│   ├── core/
│   │   ├── config.py            # Application configuration
│   │   └── security.py          # Security utilities
│   ├── crud/
│   │   ├── user.py              # User database operations
│   │   └── product.py           # Product database operations
│   ├── db/
│   │   └── session.py           # Database session management
│   ├── models/
│   │   ├── user.py              # User SQLAlchemy model
│   │   └── product.py           # Product SQLAlchemy model
│   ├── router/
│   │   ├── info.py              # Information endpoints
│   │   ├── user.py              # User management endpoints
│   │   └── product.py           # Product management endpoints
│   ├── schemas/
│   │   ├── user.py              # User Pydantic schemas
│   │   └── product.py           # Product Pydantic schemas
│   ├── templates/
│   │   ├── users.html           # User admin templates
│   │   └── products.html        # Product admin templates
│   └── main.py                  # Application entry point
├── .env                         # Environment variables
├── .env.example                 # Environment template
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Setup

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   ```bash
   cp .env.example .env
   ```

   Edit `.env` file with your configuration:

   ```env
   API_KEY=your_api_key_here
   DATABASE_URL=sqlite:///./app.db
   ```

5. **Run the application**
   ```bash
   cd app
   uvicorn main:app --reload
   ```

The application will be available at `http://localhost:8000`

## 📚 API Documentation

Once the application is running, you can access:

- **Interactive API Documentation (Swagger UI)**: `http://localhost:8000/docs`
- **Alternative API Documentation (ReDoc)**: `http://localhost:8000/redoc`
- **Admin Users Interface**: `http://localhost:8000/admin/users`

## 🔗 API Endpoints

### Information Endpoints

- `GET /api/v1/info/*` - Application information endpoints

### User Management

- `GET /api/v1/user/*` - User management endpoints
- `GET /admin/users` - Admin interface for viewing all users

### Product Management

- `GET /api/v1/product/` - List all products
- `GET /api/v1/product/{product_id}` - Get specific product by ID
- `POST /api/v1/product/` - Create new product
- `PUT /api/v1/product/{product_id}` - Update entire product (all fields required)
- `PATCH /api/v1/product/{product_id}` - Partial update product (only provided fields)
- `DELETE /api/v1/product/{product_id}` - Delete specific product
- `GET /admin/products` - Admin interface for viewing all products

## 🗄️ Database

The application uses SQLAlchemy ORM with the following models:

### User Model

- `id` - Primary key (Integer)
- `username` - Unique username (String)
- `email` - Unique email address (String)

### Product Model

- `id` - Primary key (Integer)
- `name` - Unique product name (String, 2-10 characters)
- `description` - Product description (String, optional)
- `price` - Product price (Float, must be > 1)
- `stock` - Stock availability (Boolean)

The database is automatically created when the application starts.

## 🏗️ Architecture

This project follows FastAPI best practices with a modular architecture:

- **Separation of Concerns** - Clear separation between API routes, business logic, and data access
- **Dependency Injection** - Proper use of FastAPI's dependency injection system
- **Pydantic Models** - Type-safe request/response models
- **Environment Configuration** - Secure configuration management
- **Template Support** - Jinja2 templates for admin interfaces

## 🔧 Development

### Adding New Features

1. **Models** - Add new SQLAlchemy models in `app/models/`
2. **Schemas** - Create Pydantic schemas in `app/schemas/`
3. **CRUD Operations** - Implement database operations in `app/crud/`
4. **API Routes** - Add new endpoints in `app/router/`
5. **Templates** - Add HTML templates in `app/templates/`

### Key Implementation Details

#### PATCH Operations

The application implements intelligent PATCH operations that support partial updates:

```python
# Example: Update only the price of a product
PATCH /api/v1/product/1
{
  "price": 29.99
}
```

This will update only the price field, leaving name, description, and stock unchanged.

#### Schema Validation

- **ProductCreate/ProductUpdate**: All fields required
- **ProductPatch**: All fields optional for selective updates
- **Field Validation**: Built-in validation for price (> 1), name length (2-10 chars)

### Running in Development Mode

```bash
cd app
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 🚀 Deployment

### Production Setup

1. **Set production environment variables**
2. **Use a production WSGI server**:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
   ```

### Docker (Optional)

Create a `Dockerfile` for containerized deployment:

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ .
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔍 Additional Notes

- The application uses SQLite by default but can be configured for other databases
- Security features are prepared but may need additional implementation for production use
- The admin interface provides simple HTML views for user and product management
- All API endpoints are automatically documented via FastAPI's built-in documentation
- PATCH operations support partial updates - only send the fields you want to change
- Full CRUD operations available for both users and products
- API key authentication is implemented for all endpoints

## 📞 Support

For questions or issues, please open an issue in the repository or contact the development team.
