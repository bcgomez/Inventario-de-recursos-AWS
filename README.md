# Inventario-de-recursos-AWS

# AWS Resource Inventory & Monitoring System

## 📌 Overview

This project implements a basic AWS monitoring and inventory system using Python and Boto3.

It scans AWS resources across multiple regions, analyzes RDS CPU utilization, and publishes custom metrics to Amazon CloudWatch.

---

## 🚀 Features

* Multi-region AWS resource scanning
* Inventory generation (EC2, S3, Lambda, RDS)
* RDS CPU monitoring using CloudWatch
* Threshold-based alert system
* Custom metrics publishing to CloudWatch
* Report generation (alerts summary)

---

## 🛠️ Technologies Used

* Python
* AWS Boto3
* Amazon CloudWatch
* Amazon RDS

---

## 📂 Project Structure

```
aws-resource-inventory-monitoring/
│
├── src/
│   ├── inventory.py
│   ├── rds_alerts.py
│   └── custom_metric.py
│
├── outputs/
│   ├── inventory.json
│   └── alerts_report.txt
│
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

### 1. Inventory Script

Scans AWS services and generates a JSON inventory of resources.

```bash
python src/inventory.py
```

### 2. Alert System

Checks CPU usage of RDS instances and compares against a defined threshold.

```bash
python src/rds_alerts.py
```

### 3. Custom Metrics

Publishes custom metrics (e.g., number of high CPU instances) to CloudWatch.

```bash
python src/custom_metric.py
```

---

## 📊 Example Output

```
VALIDACIÓN DE CPU EN RDS - Umbral: 20%
No RDS instances found → metric = 0
```

---

## 🧠 Key Learning Outcomes

* AWS multi-region resource management
* CloudWatch metrics integration
* Automation with Python and Boto3
* Monitoring system design fundamentals

---

## 👩‍💻 Author

Barbara Catalina Gomez Perez

---

## 📌 Notes

This project was developed as part of a hands-on AWS learning lab. Even when no resources are found, the system validates connectivity, permissions, and monitoring logic.
