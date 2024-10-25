from aws_embedded_metrics import metric_scope
from aws_embedded_metrics.storage_resolution import StorageResolution
from os import environ
from logging import getLogger

logger = getLogger(__name__)

def metrics_enabled():
    return environ.get("AWS_CLOUDWATCH_CUSTOM_METRICS_ENABLED") == "true"

@metric_scope
def put_metric(metric_name, value, unit, metrics):
    try:
        logger.info(f"put metric: {metric_name} - {value} - {unit}")
        metrics.put_metric(metric_name, value, unit, StorageResolution.STANDARD)
    except Exception as e:
        # Might be noise in logs, as per:
        # https://github.com/awslabs/aws-embedded-metrics-python/issues/52
        logger.error(f"Error putting metric: {e}", exc_info=True)


def counter(metric_name, value):
    if metrics_enabled():
        put_metric(metric_name, value, "Count")

