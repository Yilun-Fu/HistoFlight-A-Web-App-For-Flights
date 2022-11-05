from flask import Flask, request
from service.airport import airport_bp
from service.flight import flight_bp
from service.ticket import ticket_bp

app = Flask(__name__)

app.register_blueprint(airport_bp, url_prefix="/api/")
app.register_blueprint(flight_bp, url_prefix="/api/")
app.register_blueprint(ticket_bp, url_prefix="/api/")