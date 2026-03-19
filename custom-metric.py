import boto3
from datetime import datetime

REGION = "us-east-1"
NAMESPACE = "Lab/MonitoreoRDS"
METRIC_NAME = "HighCPUInstances"

cloudwatch = boto3.client("cloudwatch", region_name=REGION)

def publish_custom_metric(value):
    cloudwatch.put_metric_data(
        Namespace=NAMESPACE,
        MetricData=[
            {
                "MetricName": METRIC_NAME,
                "Timestamp": datetime.utcnow(),
                "Value": value,
                "Unit": "Count",
                "Dimensions": [
                    {
                        "Name": "Environment",
                        "Value": "Lab"
                    }
                ]
            }
        ]
    )

if __name__ == "__main__":
    high_cpu_count = 0
    publish_custom_metric(high_cpu_count)
    print(f"Métrica personalizada enviada: {METRIC_NAME} = {high_cpu_count}")