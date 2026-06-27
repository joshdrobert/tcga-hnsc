from __future__ import annotations

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def yn(series: pd.Series) -> pd.Series:
    return series.fillna("").astype(str).str.upper().str.contains("YES|POSITIVE").astype(int)


def main() -> None:
    base = pd.read_csv(PROJECT_ROOT / "data_processed" / "tcga_hnsc_clinical_expression_cohort.csv")
    flat = pd.read_csv(PROJECT_ROOT / "data_processed" / "tcga_hnsc_clinical_xml_flat.csv")
    cols = [
        "submitter_id",
        "hpv_status_by_p16_testing",
        "hpv_status_by_ish_testing",
        "history_of_neoadjuvant_treatment",
        "radiation_therapy",
        "additional_radiation_therapy",
        "additional_pharmaceutical_therapy",
        "therapy_type",
        "drug_name",
        "primary_therapy_outcome_success",
        "followup_treatment_success",
        "new_tumor_event_after_initial_treatment",
    ]
    feat = flat[[c for c in cols if c in flat.columns]].drop_duplicates("submitter_id", keep="first")
    enriched = base.merge(feat, on="submitter_id", how="left")
    enriched["hpv_p16_positive"] = yn(enriched.get("hpv_status_by_p16_testing", pd.Series(index=enriched.index, dtype=object)))
    enriched["hpv_ish_positive"] = yn(enriched.get("hpv_status_by_ish_testing", pd.Series(index=enriched.index, dtype=object)))
    enriched["any_hpv_positive"] = enriched[["hpv_p16_positive", "hpv_ish_positive"]].max(axis=1)
    enriched["radiation_received"] = yn(enriched.get("radiation_therapy", pd.Series(index=enriched.index, dtype=object)))
    enriched["systemic_therapy_recorded"] = enriched.get("therapy_type", pd.Series(index=enriched.index, dtype=object)).notna().astype(int)
    enriched["new_tumor_event"] = yn(enriched.get("new_tumor_event_after_initial_treatment", pd.Series(index=enriched.index, dtype=object)))
    out = PROJECT_ROOT / "data_processed" / "tcga_hnsc_hpv_treatment_expression_cohort.csv"
    enriched.to_csv(out, index=False)
    summary = enriched[["hpv_p16_positive", "hpv_ish_positive", "any_hpv_positive", "radiation_received", "systemic_therapy_recorded", "new_tumor_event"]].sum().reset_index()
    summary.columns = ["feature", "positive_n"]
    summary.to_csv(PROJECT_ROOT / "tables" / "table_hpv_treatment_feature_counts.csv", index=False)
    print(f"Wrote HNSC HPV/treatment enriched cohort: {len(enriched):,}")


if __name__ == "__main__":
    main()

