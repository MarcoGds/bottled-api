from flask import Flask, request

app = Flask(__name__)

@app.route('/query-string')
def query_string():

  param1 = request.args['teste']

  return 'via query string ' + param1

if(__name__ == '__main__'):
  app.run()