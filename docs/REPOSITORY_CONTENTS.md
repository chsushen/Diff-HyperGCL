# Diff-HyperGCL Repository Contents

## Source Code

* train_auto.py
* generator.py
* diffusion_generator.py
* models.py
* layers.py
* preprocessing.py

## Datasets

* MIntRec
* MIntRec2.0

## Main Methods

* HC+DG (Handcrafted + Diffusion Generated)
* DG+DG (Dual Diffusion Generated)

## Main Experimental Results

* HC+DG on MIntRec
* HC+DG on MIntRec2.0
* DG+DG on MIntRec
* DG+DG on MIntRec2.0

## Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* Weighted Precision
* Weighted Recall
* Weighted F1 Score

## Analysis

* Mean ± Std Analysis
* Class-wise Analysis
* Statistical Significance Testing

## Ablation Studies

### Modality Ablation

* T
* A
* V
* TA
* TV
* AV
* TAV

### Generator Ablation

* FF
* FE
* EF
* EE

### Hypergraph Augmentation Ablation

* A0 Identity
* A1 Edge
* A2 Mask
* A3 Hyperedge
* A4 Adaptive
* A5 Subgraph
* A6 Feature Generator
* A6 Edge Generator

## Efficiency

* Parameter Count
* FLOPs
* MACs

## Reproducibility

The repository contains all code, raw experiment logs, result files, ablation studies, class-wise reports, statistical significance results, and efficiency measurements required to reproduce the reported findings.
