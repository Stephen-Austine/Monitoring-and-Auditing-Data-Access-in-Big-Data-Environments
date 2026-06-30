import sys
from pathlib import Path

import pandas as pd


def main() -> None:
    project_dir = Path(__file__).resolve().parent
    data_path = project_dir / "access_logs (1).csv"
    output_path = project_dir / "alerts.log"

    df = pd.read_csv(data_path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["hour"] = df["timestamp"].dt.hour
    df = df.sort_values("timestamp")

    user_failed_logins = (
        df[(df["action"] == "login") & (df["status"] == "failed")]
        .groupby("user_id")
        .size()
        .to_dict()
    )
    user_total_events = df.groupby("user_id").size().to_dict()
    user_deletes = df[df["action"] == "delete_record"].groupby("user_id").size().to_dict()
    user_ips = {}
    alerts = []

    def detect_anomalies(row):
        user = row["user_id"]
        action = row["action"]
        resource = row["resource"]
        status = row["status"]
        ip = row["ip_address"]
        hour = row["hour"]
        timestamp_str = row["timestamp"].strftime("%Y-%m-%d %H:%M:%S")

        alert_msgs = []

        if user in user_failed_logins and user_failed_logins[user] > 10:
            alert_msgs.append(
                f"High failed logins ({user_failed_logins[user]}) for user {user} - potential brute-force."
            )

        if hour in [0, 1, 2, 3, 4, 21, 22, 23]:
            alert_msgs.append(f"Suspicious hour ({hour}:00) activity for user {user} at {timestamp_str}.")

        if user in user_total_events and user_total_events[user] > 40:
            alert_msgs.append(f"Unusually high activity ({user_total_events[user]} events) for user {user}.")
        if user in user_deletes and user_deletes[user] > 5:
            alert_msgs.append(f"High delete actions ({user_deletes[user]}) for user {user} - potential data loss risk.")

        if action in ["delete_record", "update_record"] and resource in ["admin_panel", "config.yaml"]:
            alert_msgs.append(
                f"High-risk action '{action}' on sensitive resource '{resource}' by user {user} at {timestamp_str}."
            )

        if user not in user_ips:
            user_ips[user] = set()
        if ip not in user_ips[user]:
            alert_msgs.append(f"New IP access ({ip}) for user {user} at {timestamp_str} - verify identity.")
            user_ips[user].add(ip)

        for msg in alert_msgs:
            full_alert = (
                f"ALERT: {msg} (Action: {action}, Resource: {resource}, Status: {status}, IP: {ip})"
            )
            alerts.append(full_alert)

    df.apply(detect_anomalies, axis=1)

    for alert in alerts:
        try:
            print(alert)
        except BrokenPipeError:
            sys.exit(0)

    output_path.write_text("\n".join(alerts) + ("\n" if alerts else ""), encoding="utf-8")
    print(f"\nTotal alerts generated: {len(alerts)}")


if __name__ == "__main__":
    main()
