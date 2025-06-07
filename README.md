# Sam - CodeBashing (LMS) Plugin Python

A Python based plugin for Soren platform, for using and assigning courses with CodeBashing.

## Features
- FastAPI-based REST API
- Modular action system
- Configuration management through PluginManager
- Standardized response format
- Automatic API documentation
- Type safety with Pydantic models
- CORS support

## Plugin Architecture

The plugin follows a modular architecture designed to run as a standalone service in a Docker container.

### Directory Structure

```
plugin-root/
├── src/
│   ├── v1/                    # API version namespace
│   │   ├── methods/           # Action implementations
│   │   ├── services/          # Provider-specific implementations
│   │   ├── middlewares/       # Custom middlewares
│   │   │   └── config_manager.py  # Plugin configuration management
│   │   └── core/             # Core configurations and models
│   └── main.py               # FastAPI app configuration
├── plugin.configs.json       # Plugin configurations
└── README.md                # Documentation
```

### Key Components

#### 1. Plugin Configuration
- `plugin.configs.json`: Defines plugin metadata and available configurations
- Configurations include service credentials and operational parameters
- Managed through the PluginManager middleware

#### 2. Core API Routes

- **Action List**: `GET /api/v1/methods`
  - Returns available plugin methods
  - Used for discovery and integration

- **Action Configuration**: `GET /api/v1/methods/:actionName`
  - Returns configuration requirements for specific methods
  - Supports frontend validation

- **Action Execution**: `POST /api/v1/methods/:actionName`
  - Executes requested methods with provided parameters
  - Returns standardized response format

#### 3. Response Format
All API responses follow a standard structure:

```json
{
  "status": "success|error",
  "data": {},
  "message": "Optional message"
}
```

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Development Setup

#### Clone the repository

```bash
git clone https://github.com/SorenHQ/sam-lms-plugin-1.git
cd sam-lms-plugin-python
```


#### Create virtual environment

```bash
python -m venv venv
```

##### Activate virtual environment

  - Windows  
    `venv\Scripts\activate`

  - Unix/MacOS  
    `source venv/bin/activate`

#### Install dependencies

```bash
pip install -r requirements.txt
```


#### Run development server

```bash
uvicorn src.main:app --reload
```


### API Documentation
FastAPI provides automatic interactive API documentation:

- Swagger UI: http://localhost:80/docs
- ReDoc: http://localhost:80/redoc

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
[MIT License](LICENSE)

## Support
For support, please open an issue in the GitHub repository.
