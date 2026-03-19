import boto3
from datetime import datetime, timedelta

REGIONS = ["us-east-1", "us-east-2", "us-west-2"]
THRESHOLD = 20.0

def get_rds_instances(rds_client):
    response = rds_client.describe_db_instances()
    return response.get("DBInstances", [])

def get_cpu_metric(cloudwatch_client, db_identifier):
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(minutes=10)

    response = cloudwatch_client.get_metric_statistics(
        Namespace="AWS/RDS",
        MetricName="CPUUtilization",
        Dimensions=[
            {
                "Name": "DBInstanceIdentifier",
                "Value": db_identifier
            }
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,
        Statistics=["Average"],
        Unit="Percent"
    )

    datapoints = response.get("Datapoints", [])
    if not datapoints:
        return None

    latest = max(datapoints, key=lambda x: x["Timestamp"])
    return latest["Average"]

def main():
    print("=" * 70)
    print(f"VALIDACIÓN DE CPU EN RDS - Umbral: {THRESHOLD}%")
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    total_global = 0
    normal_global = 0
    alta_global = 0
    sin_datos_global = 0

    for region in REGIONS:
        print(f"\nRevisando región: {region}")
        print("-" * 70)

        rds = boto3.client("rds", region_name=region)
        cloudwatch = boto3.client("cloudwatch", region_name=region)

        dbs = get_rds_instances(rds)

        if not dbs:
            print("No hay instancias RDS en esta región.")
            continue

        print("Analizando instancias RDS:\n")

        for db in dbs:
            db_id = db["DBInstanceIdentifier"]
            total_global += 1

            cpu = get_cpu_metric(cloudwatch, db_id)

            if cpu is None:
                sin_datos_global += 1
                print(f"{db_id}: sin datos de CPU")
            elif cpu > THRESHOLD:
                alta_global += 1
                print(f"{db_id}: CPU Alta ({cpu:.2f}%)")
            else:
                normal_global += 1
                print(f"{db_id}: CPU Normal ({cpu:.2f}%)")

    print("\n" + "=" * 70)
    print("RESUMEN GENERAL")
    print("=" * 70)
    print(f"Total de instancias RDS: {total_global}")
    print(f"Instancias con CPU normal: {normal_global}")
    print(f"Instancias con CPU alta: {alta_global}")
    print(f"Instancias sin datos: {sin_datos_global}")

if __name__ == "__main__":
    main()

