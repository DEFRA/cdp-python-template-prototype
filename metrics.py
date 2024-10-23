from aws_embedded_metrics import metric_scope
from aws_embedded_metrics.storage_resolution import StorageResolution
from os import environ
from logging import getLogger

logger = getLogger(__name__)

def metrics_enabled():
    value = environ.get("AWS_EMF_ENVIRONMENT_OVERRIDE")
    return value != "local"

@metric_scope
def put_metric(metric_name, value, unit):
    logger.info(f"Counter metric: {metric_name} - {value}")
    metrics.put_metric(metric_name, value, unit, StorageResolution.STANDARD)

def counter(metric_name, value):
    if metrics_enabled():
        put_metric(metric_name, value, "Count")

