from aws_embedded_metrics import metric_scope
from aws_embedded_metrics.storage_resolution import StorageResolution
from os import environ
from logging import getLogger

logger = getLogger(__name__)

def metrics_enabled():
    value = environ.get("AWS_EMF_ENVIRONMENT_OVERRIDE")
    return value != "local"

def counter(metric_name, value):
    if metrics_enabled():
        logger.info(f"Counter metric: {metric_name} - {value}")
        metrics = metric_scope.metrics()
        metrics.put_metric(metric_name, value, "Count", StorageResolution.STANDARD)
