# Built-in packages
import logging

# Third-party packages
from flask import Flask
from flask_opentracing import FlaskTracing
from flask_opentracing.tracing import opentracing
from jaeger_client.config import Config as JaegerClientConfig
from jaeger_client.metrics.prometheus import PrometheusMetricsFactory
from prometheus_flask_exporter import PrometheusMetrics as FlaskMetrics

# Local packages


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
    FlaskTracing(get_opentracing_tracer("backend-service"), True, app)
    FlaskMetrics(app)
