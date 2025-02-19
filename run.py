from app import create_app
from dotenv import load_dotenv
load_dotenv()  # This loads variables from .env into the environment

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
