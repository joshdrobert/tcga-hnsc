from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PROJECT_ROOT
sys.path.append(str(REPO_ROOT / "_shared" / "02_common_functions"))

from validation_extras import cross_validated_metrics, simple_km_table  # noqa: E402


def main() -> None:
    data = pd.read_csv(PROJECT_ROOT / "data_processed" / "tcga_hnsc_clinical_expression_cohort.csv")
    clinical = ["sex", "age_at_diagnosis_years", "pathologic_stage", "pathologic_t", "pathologic_n", "pathologic_m", "histologic_grade", "primary_site", "smoking_history"]
    cross_validated_metrics(data, clinical, "event_death", "hnsc_clinical_only").to_csv(PROJECT_ROOT / "tables" / "table_cross_validation.csv", index=False)
    simple_km_table(data, "overall_survival_days", "event_death", "pathologic_stage", PROJECT_ROOT / "tables" / "table_survival_by_stage_horizon.csv")
    print("Wrote HNSC validation summaries")


if __name__ == "__main__":
    main()

