import flask


def main():
    app = flask.Flask(__name__)

    @app.route("/")
    def index():
        return "I can echo your request, go to `/[something]` to see me work!"

    @app.route("/<arg>")
    def echo(arg):
        return f"Echo: {arg}"

    app.run(host="0.0.0.0", port=8181)


if __name__ == "__main__":
    main()
