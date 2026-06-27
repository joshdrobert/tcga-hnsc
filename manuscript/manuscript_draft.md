# Development of an Open-Source Genomic-Clinical Risk Score for Head and Neck Squamous Cell Carcinoma Using TCGA-HNSC

## Abstract

### Background
Head and neck squamous cell carcinoma outcomes vary substantially by clinical and molecular risk factors.

### Objective
To build a reproducible TCGA-HNSC clinical baseline for an eventual genomic-clinical risk score.

### Methods
Open TCGA-HNSC clinical XML supplements were downloaded through GDC and parsed into a patient-level cohort. A first-pass clinical-only logistic model predicted death event status using demographic, stage, TNM, grade, primary site, and smoking variables.

### Results
The current cohort includes 294 patients with 115 death events. Held-out validation performance was AUROC 0.657, AUPRC 0.561, and Brier score 0.231.

### Conclusions
The clinical-only baseline is reproducible and ready for HPV/p16 proxy enrichment and molecular feature selection.

## Introduction

## Methods

### Data Source
TCGA-HNSC open clinical supplements and file manifests were obtained from the GDC API.

### Predictors
Candidate predictors included sex, age, pathologic stage, TNM fields, histologic grade, primary site, and smoking history.

### Outcome
The first-pass endpoint was death event status.

### Model Development
A logistic regression model was fit and converted to an integer score table.

## Results

Generated outputs include the processed cohort, flattened XML table, missingness table, clinical characteristics, model performance, and integer score table.

## Discussion

The model provides a baseline but should be extended with HPV/p16 proxies, treatment variables, and molecular predictors.

## Limitations

Internal validation only, clinical-only predictors, and incomplete endpoint harmonization.

## Conclusion

The HNSC project now has a working clinical baseline and is ready for genomic-clinical extension.

