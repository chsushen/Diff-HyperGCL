# Diff-HyperGCL

Official implementation of:

**Diff-HyperGCL: Diffusion-Based Hypergraph Contrastive Learning for Multimodal Intent Recognition**

---

## Overview

Diff-HyperGCL replaces the original VHGAE augmentation module of HyperGCL with a diffusion-based generator for hypergraph contrastive learning.

Two augmentation paradigms are investigated:

- HC+DG (Handcrafted + Diffusion Generated)
- DG+DG (Dual Diffusion Generated)

Experiments are conducted on:

- MIntRec
- MIntRec2.0

---

## Key Findings

- HC+DG achieves the best performance on MIntRec.
- DG+DG achieves the best performance on MIntRec2.0.
- The optimal augmentation strategy is dataset-dependent.

---

## Main Results

| Method | Dataset | Accuracy |
|----------|----------|----------|
| HC+DG | MIntRec | 85.72 ± 0.99 |
| DG+DG | MIntRec | 85.07 ± 0.63 |
| HC+DG | MIntRec2.0 | 73.84 ± 0.37 |
| DG+DG | MIntRec2.0 | 73.97 ± 0.45 |

---



## Datasets

### MIntRec

Official Dataset Repository:
https://github.com/thuiar/MIntRec

Official Benchmark Paper:
https://arxiv.org/abs/2209.04355

### MIntRec2.0

Official Dataset Repository:
https://github.com/thuiar/MIntRec2.0

Official Benchmark Paper:
https://arxiv.org/abs/2403.10943

Download the datasets from the official repositories and follow the preprocessing protocol described by the benchmark authors.

---

## Repository Structure

- code/ : Core implementation
- results/ : Main experimental results
- paper_tables/ : Paper-ready tables
- ablations/ : Modality and generator ablations
- docs/ : Documentation and reports
- tables/ : Statistical analyses

---

## Reproducibility

### Environment Setup

pip install -r requirements.txt

### Experimental Variants

- HC+DG (Handcrafted + Diffusion Generated)
- DG+DG (Dual Diffusion Generated)

### Available Analyses

- Modality Ablation (T, A, V, TA, TV, AV, TAV)
- Generator Ablation (FF, FE, EF, EE)
- Class-wise Analysis
- Statistical Significance Testing
- Mean ± Standard Deviation Analysis

Refer to the corresponding files in results/, ablations/, and paper_tables/ for the reported experimental results.

---

## Included Analyses

- Class-wise Analysis
- Modality Ablation
- Generator Ablation
- Mean ± Std Analysis
- Statistical Significance Testing

---

## Core Files

- train_auto.py
- generator.py
- diffusion_generator.py
- models.py

---

## Citation

Citation information will be added after publication.
