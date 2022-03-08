import flask


application = flask.Flask(__name__)

@application.route("/")
def index():
    return "I can echo your request, go to `/[something]` to see me work!"

@application.route("/<arg>")
def echo(arg):
    return f"Echo: {arg}"

if (__name__ == "__main__"):
    application.run(host="0.0.0.0", port=8181)
