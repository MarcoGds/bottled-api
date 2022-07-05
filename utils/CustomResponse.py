from flask import make_response, jsonify

class CustomResponse():

  def format_response(json_dict, status_code):
    res = make_response(jsonify(json_dict), status_code)
    res.headers["Content-Type"] = "application/json"

    return res