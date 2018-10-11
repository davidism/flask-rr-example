from flask import Request
from flask import send_file
from werkzeug.exceptions import default_exceptions

from flask_rr import FlaskRR
from flask_rr import Response

app = FlaskRR(__name__)


@app.route("/")
@app.route("/hello")
def hello(req: Request, res: Response):
    name = req.args.get("name", "World")
    res.data = f"Hello, {name}!"


@app.route("/status/<int:code>")
def status(req, res, *, code):
    res.status_code = code
    res.data = default_exceptions[code].description


@app.route("/download")
def download(req, res):
    return send_file(__file__, as_attachment=True)
