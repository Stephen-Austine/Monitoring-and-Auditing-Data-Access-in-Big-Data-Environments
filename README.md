[README.md](https://github.com/user-attachments/files/28758223/README.md)
# Monitoring and Auditing Data Access in Big Data Environments

A simulation-based security analytics project that demonstrates how access logs can be transformed into actionable audit insights. The work combines a reproducible Python workflow, an exploratory notebook, a rule-based anomaly detector, and supporting documentation in a structure suitable for GitHub presentation.

![Project Overview](assets/images/action_distribution.png)

## Why this project matters

This repository models a lightweight Security Operations Center (SOC) workflow for monitoring user activity in a big-data environment. It showcases how raw event data can be ingested, analyzed, and used to flag suspicious behavior such as brute-force login attempts, off-hours access, unusual activity spikes, and high-risk actions on sensitive resources.

The implementation is intentionally simple and reproducible, making it useful for academic demonstrations, interview portfolios, and hands-on learning in audit logging and anomaly detection.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Workflow Architecture](#workflow-architecture)
- [Dataset](#dataset)
- [Anomaly Detection Rules](#anomaly-detection-rules)
- [Visualizations](#visualizations)
- [Getting Started](#getting-started)
- [How to Run](#how-to-run)
- [Expected Output](#expected-output)
- [Project Findings](#project-findings)
- [Future Improvements](#future-improvements)
- [Authors](#authors)

---

## Project Overview

The project was developed as part of a course-focused exercise on monitoring and auditing data access. It simulates a realistic enterprise environment with user activity logs and uses Python-based analytics to uncover suspicious behaviors that would typically be surfaced by SIEM-like tools such as Splunk, ELK, or Microsoft Sentinel.

This repository is designed to be practical and professional:

- it uses a real dataset structure,
- it includes transparent analysis steps,
- it produces alert output and visual summaries,
- and it is easy to run locally or in a cloud notebook environment.

---

## Key Features

- Simulated access-log dataset with 500 events across 15 users and multiple resource types
- Interactive notebook workflow for exploratory data analysis and chart generation
- Rule-based anomaly detector that flags suspicious activity patterns
- Structured alert output written to a log file for review
- Supporting Excel dashboard, reports, and presentation artifacts
- A reproducible Python packaging setup with dependency management and tests

---

## Project Structure

```text
.
├── Monitoring and Auditing Data Access (Big Data)/
│   ├── access_logs (1).csv
│   ├── monitoring_setup.ipynb
│   ├── Anomaly_detection.py
│   ├── alerts.log
│   ├── Dashboard.xlsx
│   ├── Monitoring Setup.docx
│   ├── Monitoring Audit Report.docx
│   ├── DSA4030-Monitoring and auding data access-Methodology.docx
│   ├── Lightweight Log Auditing Blueprint.pptx
│   ├── action_distribution.png
│   └── response_time_rolling.png
├── assets/
│   └── images/
│       ├── action_distribution.png
│       └── response_time_rolling.png
├── tests/
│   └── test_anomaly_detection.py
├── requirements.txt
├── pyproject.toml
├── Makefile
├── PROJECT_SUMMARY.md
└── README.md
```

---

## Workflow Architecture

```text
User activity simulation
        │
        ▼
Access log dataset
        │
        ├── Exploratory analysis and visualization
        │        │
        │        ▼
        │   Notebook + charts
        │
        └── Rule-based anomaly detection
                 │
                 ▼
             alerts.log
```

This architecture mirrors the core SIEM journey of ingesting events, analyzing them, and raising alerts for review.

---

## Dataset

The main dataset is stored in the project folder as access_logs (1).csv.

Each row represents a single access event and includes:

- timestamp
- user_id
- action
- resource
- status
- ip_address
- response_time_ms

The dataset is synthetic but structured to resemble enterprise access telemetry.

---

## Anomaly Detection Rules

The anomaly detection logic in Anomaly_detection.py applies the following rules:

| Rule | Logic | Why it matters |
|---|---|---|
| Brute-force detection | More than 10 failed login attempts by a user | Strong signal of credential abuse |
| Off-hours access | Access during 00:00–04:00 or 21:00–23:00 | May indicate unauthorized access |
| High event volume | More than 40 events from one user | Possible automation or misuse |
| Excessive deletes | More than 5 delete_record actions | Indicates data destruction risk |
| High-risk action on sensitive resource | delete_record or update_record on admin_panel or config.yaml | Critical tampering risk |
| New IP access | First-time IP seen for a user | May require identity verification |

All alerts are written in a readable format such as:

```text
ALERT: High failed logins (12) for user user_3 - potential brute-force. (Action: login, Resource: admin_panel, Status: failed, IP: 192.168.1.42)
```

---

## Visualizations

The notebook and analysis workflow generate multiple visuals, including:

- events per user,
- actions per hour of the day,
- failed login attempts per user,
- overall action distribution,
- response time trend over time.

### Preview

| Action Distribution | Response Time Trend |
|---|---|
| ![Action Distribution](assets/images/action_distribution.png) | ![Response Time Trend](assets/images/response_time_rolling.png) |

---

## Getting Started

### Prerequisites

- Python 3.9+
- pip
- Optional: Jupyter Notebook or VS Code with Python support

### Installation

```bash
git clone <your-repo-url>
cd Monitoring-and-Auditing-Data-Access-in-Big-Data-Environments
python3 -m pip install -r requirements.txt
```

You can also install the project in editable mode via:

```bash
python3 -m pip install -e .
```

---

## How to Run

### 1. Run the anomaly detector

```bash
make run
```

or directly:

```bash
python3 "Monitoring and Auditing Data Access (Big Data)/Anomaly_detection.py"
```

### 2. Explore the notebook

```bash
jupyter notebook "Monitoring and Auditing Data Access (Big Data)/monitoring_setup.ipynb"
```

### 3. Run tests

```bash
make test
```

---

## Expected Output

After running the detection script, the repository will generate an alerts log file containing structured findings for suspicious access behavior.

The script also prints the alerts to the terminal for immediate review.

---

## Project Findings

The project highlights a few important patterns in the synthetic dataset:

- Some users show unusually high activity levels and may merit closer review.
- Delete operations appear relatively frequent, which could indicate overly broad permissions.
- Off-hours access and new-IP access events are strong security indicators.
- Response time trends remain mostly stable, with isolated spikes that could suggest system stress or load issues.

These findings are documented further in the included report files.

---

## Future Improvements

Planned enhancements include:

- integrating geolocation enrichment for suspicious IP activity,
- replacing rule-based detection with statistical or machine-learning models,
- connecting the workflow to a live log source,
- adding severity scoring and alert deduplication,
- building a live dashboard with a real-time monitoring stack.

---

## Authors

Stephen Austine

---

This project is academic in nature and uses synthetic data only. No real user data was collected or used.
