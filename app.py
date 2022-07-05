from flask import Flask, jsonify, abort, request
from routes.drink_bp import drink_bp

app = Flask(__name__)

app.register_blueprint(drink_bp, url_prefix = '/drinks')

if __name__ =='__main__':
  app.run()