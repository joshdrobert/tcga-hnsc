from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PROJECT_ROOT
sys.path.append(str(REPO_ROOT / "_shared" / "02_common_functions"))

from rigorous_validation import validate_feature_sets  # noqa: E402


def main() -> None:
    data = pd.read_csv(PROJECT_ROOT / "data_processed" / "tcga_hnsc_hpv_treatment_expression_cohort.csv")
    clinical = ["sex", "age_at_diagnosis_years", "pathologic_stage", "pathologic_t", "pathologic_n", "pathologic_m", "histologic_grade", "primary_site", "smoking_history"]
    enriched = clinical + ["hpv_p16_positive", "hpv_ish_positive", "any_hpv_positive", "radiation_received", "systemic_therapy_recorded", "new_tumor_event"]
    expression = [column for column in data.columns if column.startswith("expr_")]
    validate_feature_sets(
        data,
        "event_death",
        {
            "clinical_only": clinical,
            "clinical_hpv_treatment": enriched,
            "clinical_hpv_treatment_expression": enriched + expression,
        },
        PROJECT_ROOT / "tables",
        PROJECT_ROOT / "figures",
        "hnsc",
    )


if __name__ == "__main__":
    main()
