from models.Drink import Drink
from flask import Flask, jsonify, abort, request
from utils.CustomResponse import CustomResponse

def index():
  return CustomResponse.format_response(Drink.selectAll(), 200)

def create():

  if request.is_json:
    
    drink_req = request.get_json()
    return CustomResponse.format_response(Drink.insert(drink_req), 201)

  return format({"error" : "Request must be JSON"}, 415)

def read(id):
  return CustomResponse.format_response(Drink.select(id), 200)

def update(id):
  
  drink_req = request.get_json()

  Drink.update(id, drink_req)
  
  return CustomResponse.format_response(Drink.select(id), 200)

def destroy(id):
  return CustomResponse.format_response(Drink.delete(id), 200)
