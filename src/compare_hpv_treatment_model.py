from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PROJECT_ROOT
sys.path.append(str(REPO_ROOT / "_shared" / "02_common_functions"))

from model_comparison import compare_feature_sets  # noqa: E402


def main() -> None:
    data = pd.read_csv(PROJECT_ROOT / "data_processed" / "tcga_hnsc_hpv_treatment_expression_cohort.csv")
    clinical = ["sex", "age_at_diagnosis_years", "pathologic_stage", "pathologic_t", "pathologic_n", "pathologic_m", "histologic_grade", "primary_site", "smoking_history"]
    hpv_treatment = ["hpv_p16_positive", "hpv_ish_positive", "any_hpv_positive", "radiation_received", "systemic_therapy_recorded", "new_tumor_event"]
    expression = [c for c in data.columns if c.startswith("expr_")]
    compare_feature_sets(
        data,
        "event_death",
        {
            "clinical_only": clinical,
            "clinical_hpv_treatment": clinical + hpv_treatment,
            "clinical_hpv_treatment_expression": clinical + hpv_treatment + expression,
        },
        PROJECT_ROOT / "tables" / "table_hpv_treatment_model_comparison.csv",
    )
    print("Wrote HNSC HPV/treatment model comparison")


if __name__ == "__main__":
    main()

