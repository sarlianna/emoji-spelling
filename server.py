import os
import shlex
import json
from flask import (
    Flask,
    request,
    Response,
    abort
)

from memes import (
    main as format_memes,
    LETTER_BITMAPS_5,
)


SLACK_TOKEN = os.environ.get("SLACK_TOKEN", "")


app = Flask(__name__)


request_args = [
        "token",
        "team_id",
        "team_domain",
        "channel_id",
        "channel_name",
        "user_id",
        "user_name",
        "command",
        "text",
        "response_url"
]

DEFAULTS = ["MEMES", ":kappa:", False, ":blank:", ":pogchamp:", ":pogchamp:", ":kappa:"]


def validate_request_args(args):
    res_args = shlex.split(args["text"])
    def get_arg_or_default(index):
        try:
            result = res_args[index]
        except IndexError:
            result = DEFAULTS[index]
        return result

    res = {
        "text": get_arg_or_default(0),
        "filled": get_arg_or_default(1),
        "multipart": bool(get_arg_or_default(2)),
        "space": get_arg_or_default(3),
        "filled2": get_arg_or_default(4),
        "filled3": get_arg_or_default(5),
        "filled4": get_arg_or_default(6)
    }
    return res


def validate_slack_token(token):
    return token == SLACK_TOKEN


def format_slack_response(meme_result):
    response = {
            "response_type": "in_channel",
            "text": meme_result
    }
    return response


@app.route("/", methods=["POST"])
def dont_let_your_dreams_be_memes():
    token = request.form["token"]
    if not validate_slack_token(token):
        abort(401)
    args = validate_request_args(request.form)

    result = format_memes(args["text"], LETTER_BITMAPS_5, args["multipart"], [args["space"], args["filled"], args["filled2"], args["filled3"], args["filled4"]])

    response = format_slack_response(result)
    return (json.dumps(response), 200, {"content-type": "application/json"})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
