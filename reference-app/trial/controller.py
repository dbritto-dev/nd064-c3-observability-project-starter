# Built-in packages

# Third-party packages
from flask import Flask
from flask.json import jsonify
from requests import get

# Local packages
from tracing import get_tracer


def register_routes(app: Flask) -> None:
    @app.route("/")
    def homepage():
        tracer = get_tracer()
        gh_jobs_url = "https://jobs.github.com/positions.json?description=python"

        with tracer.start_span("get-python-jobs") as span:
            span.set_tag("http.url", gh_jobs_url)
            homepages = []
            res = get(gh_jobs_url)
            span.set_tag("http.status_code", res.status_code)
            python_jobs = res.json()
            span.set_tag("python_jobs.count", len(python_jobs))
            for result in python_jobs:
                try:
                    homepages.append(get(result["company_url"]))
                except:
                    return "Unable to get site for %s" % result["company"]

        return jsonify(homepages)
