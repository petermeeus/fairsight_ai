# FairSight AI

This is a Flask-based web application for AI-powered contract analysis.

## Features

- User authentication (signup, login, logout, password reset)
- File upload for contract analysis
- Dummy ML analysis integration (placeholder for future ML model)
- Responsive design with a modern UI
- Modular Flask structure with Blueprints

## Setup

1. Create a virtual environment and activate it.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set environment variables in a `.env` file (see sample above).
4. Initialize the database:
   ```
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```
5. Run the application:
   ```
   python run.py
   ```

## Deployment

For production, use Gunicorn or uWSGI. Ensure to set environment variables for production.

## Future Enhancements

- Integrate a production-ready ML model for contract analysis.
- Implement user roles and analytics dashboard.
- Add social authentication and multi-language support.
