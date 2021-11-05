# Built-in packages
import logging

# Third-party packages
from flask import Flask, g
from jaeger_client import Config
from jaeger_client.metrics.prometheus import PrometheusMetricsFactory
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.trace import TracerProvider, Tracer
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    BatchSpanProcessor,
    SpanExporter,
)
from opentelemetry.exporter.jaeger.thrift import JaegerExporter

# Local packages


def init_tracer(service):
    logging.getLogger("").handlers = []
    logging.basicConfig(format="%(message)s", level=logging.DEBUG)

    config = Config(
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
    return config.initialize_tracer()


def get_tracer() -> Tracer:
    return g.tracer if "tracer" in g else init_tracer("trial-service")


def get_span_exporter(app: Flask) -> SpanExporter:
    return ConsoleSpanExporter() if app.debug else JaegerExporter()


def register_instrumentors(app: Flask) -> None:
    trace.set_tracer_provider(
        TracerProvider(active_span_processor=BatchSpanProcessor(get_span_exporter(app)))
    )

    FlaskInstrumentor().instrument_app(app)
    RequestsInstrumentor().instrument()
