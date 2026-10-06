from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "website_requests_total",
    "Total number of requests received by the website"
)


@app.route("/")
def home():
    REQUEST_COUNT.inc()

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Monitoring Demo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 100px;
                background: #f4f4f4;
            }

            .container {
                background: white;
                width: 500px;
                margin: auto;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }

            h1 {
                color: #333;
            }

            p {
                color: #666;
            }

            .status {
                color: green;
                font-weight: bold;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>DevOps Monitoring Demo</h1>
            <p>Flask application monitored using Prometheus.</p>
            <p class="status">Application Status: Running</p>
        </div>
    </body>
    </html>
    """


@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)