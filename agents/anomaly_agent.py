import pandas as pd
from datetime import datetime

class AnomalyAgent:
    def run(self, df: pd.DataFrame):
        anomalies = []

        for _, row in df.iterrows():
            emp_id = row.get("Employee ID")
            name = row.get("Employee Name")
            date = row.get("Date")
            status = row.get("Status")
            lunch = row.get("Lunch Break (mins)")
            start = row.get("Start Time")
            end = row.get("End Time")

            def parse_time(time_str):
                try:
                    return datetime.strptime(time_str, "%I:%M %p")
                except:
                    return None

            if status == "Vacation":
                anomalies.append({
                    "Employee ID": emp_id,
                    "Employee Name": name,
                    "Date": date,
                    "Anomaly Type": "Vacation"
                })
            elif status == "Sick Leave":
                anomalies.append({
                    "Employee ID": emp_id,
                    "Employee Name": name,
                    "Date": date,
                    "Anomaly Type": "Sick Leave"
                })
            elif status == "Present" and start and end:
                start_dt = parse_time(start)
                end_dt = parse_time(end)
                if start_dt and end_dt and lunch:
                    total_minutes = (end_dt - start_dt).total_seconds() / 60 - int(lunch)
                    hours_worked = total_minutes / 60

                    if hours_worked > 9:
                        anomalies.append({
                            "Employee ID": emp_id,
                            "Employee Name": name,
                            "Date": date,
                            "Anomaly Type": "Over 9 Hours"
                        })
                    elif hours_worked < 9:
                        anomalies.append({
                            "Employee ID": emp_id,
                            "Employee Name": name,
                            "Date": date,
                            "Anomaly Type": "Under 9 Hours"
                        })

                    if int(lunch) > 120:
                        anomalies.append({
                            "Employee ID": emp_id,
                            "Employee Name": name,
                            "Date": date,
                            "Anomaly Type": "Long Lunch"
                        })

        return anomalies
