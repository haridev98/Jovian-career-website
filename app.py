from flask import Flask

app = Flask(__name__)


@app.route("/")
def Hell_world():
 # print( "hellow world")
  return "World------------- Hello"

if __name__=="__main__":
  app.run('0.0.0.0',debug = True)

