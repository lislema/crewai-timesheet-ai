from tools.excel_utils import load_timesheet

class DataLoaderAgent:
    def run(self, path: str):
        print("[DataLoader] Loading timesheet from:", path)
        return load_timesheet(path)
