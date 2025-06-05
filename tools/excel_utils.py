import pandas as pd

def load_timesheet(path: str) -> pd.DataFrame:
    return pd.read_excel(path)

def summarize_employee(df, employee_id):
    return df[df['Employee ID'] == employee_id].to_string(index=False)
