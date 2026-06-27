from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PROJECT_ROOT
sys.path.append(str(REPO_ROOT / "_shared" / "02_common_functions"))

from tabular_risk_model import train_logistic_score  # noqa: E402


def main() -> None:
    enriched = PROJECT_ROOT / "data_processed" / "tcga_hnsc_clinical_expression_cohort.csv"
    data = pd.read_csv(enriched if enriched.exists() else PROJECT_ROOT / "data_processed" / "tcga_hnsc_analysis_cohort.csv")
    predictors = ["sex", "age_at_diagnosis_years", "pathologic_stage", "pathologic_t", "pathologic_n", "pathologic_m", "histologic_grade", "primary_site", "smoking_history"]
    predictors += [c for c in data.columns if c.startswith("expr_")]
    predictors = [c for c in predictors if c in data.columns]
    train_logistic_score(data, predictors, "event_death", PROJECT_ROOT / "models", PROJECT_ROOT / "tables")
    print("Trained TCGA-HNSC clinical mortality risk score")


if __name__ == "__main__":
    main()
