import os
from datetime import datetime
import pandas as pd
from collections import defaultdict

def save_anomaly_reports(anomalies, output_dir='reports'):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    os.makedirs(output_dir, exist_ok=True)

    records_by_type = defaultdict(list)
    for a in anomalies:
        if not isinstance(a, dict):
            continue
        anomaly_type = a.get("Anomaly Type") or a.get("Type") or "Unknown"
        records_by_type[anomaly_type].append(a)

    for anomaly_type, rows in records_by_type.items():
        df = pd.DataFrame(rows)
        filename = f"{output_dir}/anomalies_{anomaly_type.replace(' ', '_').lower()}_{timestamp}.xlsx"
        df.to_excel(filename, index=False)
        print(f"[Report] Saved {len(rows)} entries to {filename}")
