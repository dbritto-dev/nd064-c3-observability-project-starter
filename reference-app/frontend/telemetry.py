# Built-in packages
import logging

# Third-party packages
from flask import Flask
from flask_opentracing import FlaskTracing
from flask_opentracing.tracing import opentracing
from jaeger_client.config import Config as JaegerClientConfig
from jaeger_client.metrics.prometheus import PrometheusMetricsFactory
from prometheus_client.exposition import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

# Local packages


class FlaskMetrics:
    def __init__(self, app: Flask = None) -> None:
        app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})


def get_opentracing_tracer(service) -> opentracing.Tracer:
    logging.getLogger("").handlers = []
    logging.basicConfig(format="%(message)s", level=logging.DEBUG)

    jaeger_client_config = JaegerClientConfig(
        config={
            "sampler": {
                "type": "const",
                "param": 1,
            },
            "logging": True,
        },
        service_name=service,
        validate=True,
        metrics_factory=PrometheusMetricsFactory(service_name_label=service),
    )
    return jaeger_client_config.initialize_tracer()


def register_telemetry(app: Flask) -> None:
    FlaskTracing(get_opentracing_tracer("frontend-service"), True, app)
    FlaskMetrics(app)
