# Built-in packages

# Third-party packages
from flask import Flask
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    BatchSpanProcessor,
    SpanExporter,
)
from opentelemetry.exporter.jaeger.thrift import JaegerExporter

# Local packages

RESOURCE_SERVICE_NAME = "trial-service"


def get_span_exporter(app: Flask) -> SpanExporter:
    return ConsoleSpanExporter() if app.debug else JaegerExporter()


def register_tracing(app: Flask) -> None:
    trace.set_tracer_provider(
        TracerProvider(
            resource=Resource({SERVICE_NAME: RESOURCE_SERVICE_NAME}),
            active_span_processor=BatchSpanProcessor(get_span_exporter(app)),
        )
    )

    FlaskInstrumentor().instrument_app(app)
    RequestsInstrumentor().instrument()
