from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import logging
from logging.handlers import RotatingFileHandler
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()



def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    ENV = os.getenv("ENV", "development")

    if ENV == "development":
        origins = ["http://127.0.0.1:3000"]  # 本地开发地址（Vite默认端口）
    else:
        origins = ["https://v0-new-project-cydxhxkw9hp.vercel.app"]  # 线上前端域名

    CORS(app, origins=origins, supports_credentials=True)

    db.init_app(app)

    from app.routes import main_bp
    app.register_blueprint(main_bp)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    ))
    app.logger.addHandler(file_handler)
    app.logger.info('App startup')

    return app
