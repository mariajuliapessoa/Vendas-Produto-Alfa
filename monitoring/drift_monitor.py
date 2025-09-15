import pandas as pd
from evidently.report import Report
from evidently.metrics import DataDriftPreset

def check_drift(reference_path, current_path):
    reference = pd.read_csv(reference_path)
    current = pd.read_csv(current_path)

    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=reference, current_data=current)
    report.save_html("drift_report.html")

if __name__ == "__main__":
    check_drift("data/historico.csv", "data/novos_dados.csv")
