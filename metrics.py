from aws_embedded_metrics import metric_scope
from aws_embedded_metrics.storage_resolution import StorageResolution
from os import environ
from asyncio import get_event_loop
from logging import getLogger

logger = getLogger(__name__)

def metrics_enabled():
    value = environ.get("AWS_EMF_ENVIRONMENT_OVERRIDE")
    return value != "local"

@metric_scope
def put_metric(metric_name, value, unit, metrics):
    try:
        logger.info(f"put metric: {metric_name} - {value} - {unit}")
        metrics.put_metric(metric_name, value, unit, StorageResolution.STANDARD)
    finally:
        # Remove noise in logs
        # https://github.com/awslabs/aws-embedded-metrics-python/issues/52
        loop = get_event_loop()
        loop.run_until_complete(metrics.flush())


def counter(metric_name, value):
    if metrics_enabled():
        put_metric(metric_name, value, "Count")

