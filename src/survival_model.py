from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PROJECT_ROOT
sys.path.append(str(REPO_ROOT / "_shared" / "02_common_functions"))

from survival_models import fit_cox_model, write_km_plot  # noqa: E402


def main() -> None:
    data = pd.read_csv(PROJECT_ROOT / "data_processed" / "tcga_hnsc_clinical_expression_cohort.csv")
    predictors = ["sex", "age_at_diagnosis_years", "pathologic_stage", "histologic_grade", "smoking_history"]
    fit_cox_model(data, predictors, "overall_survival_days", "event_death", PROJECT_ROOT / "tables", "hnsc")
    write_km_plot(data, "overall_survival_days", "event_death", "pathologic_stage", PROJECT_ROOT / "figures" / "hnsc_km_by_stage.png")
    print("Wrote HNSC Cox survival model")


if __name__ == "__main__":
    main()
