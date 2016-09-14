from flask import (
    Flask,
    Request,
)


SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")

app = Flask(__name__)


request_args = {
    ""
}


def validate_request_args(args):
    pass


def validate_slack_token(token):
    return token == SLACK_TOKEN


@app.route("/", "POST")
def dont_let_your_dreams_be_memes(app):
    # form-encoded args
    args = request.args()
    


