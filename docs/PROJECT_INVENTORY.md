# Diff-HyperGCL Project Inventory

## Project Title
Diff-HyperGCL: Diffusion-Based Hypergraph Contrastive Learning for Multimodal Intent Recognition

## Datasets
1. MIntRec
2. MIntRec2.0

## Methods
1. HC+DG (Handcrafted + Diffusion Generated)
2. DG+DG (Dual Diffusion Generated)

## Core Code
train_auto.py
generator.py
diffusion_generator.py
models.py
preprocessing.py
layers.py

## Main Results
HC_DG_MIntRec_10runs.txt
HC_DG_MIntRec20_10runs.txt
DG_DG_MIntRec_10runs.txt
DG_DG_MIntRec20_10runs.txt

## Analysis
1. Class-wise Analysis
2. Mean ± Std Analysis
3. Statistical Significance Testing

## Ablations
1. Modality Ablation
   T
   A
   V
   TA
   TV
   AV
   TAV

2. Generator Ablation
   FF
   FE
   EF
   EE

## Main Scientific Finding

HC+DG achieves the best performance on MIntRec.

DG+DG achieves the best performance on MIntRec2.0.

The optimal augmentation strategy is dataset-dependent.

## Core Novelty

Replacement of VHGAE with diffusion-based hypergraph augmentation.

Systematic investigation of HC+DG and DG+DG augmentation paradigms.

Discovery of dataset-dependent augmentation behavior in hypergraph contrastive learning.

## Paper Components Completed

✓ SOTA Comparison
✓ Modality Analysis
✓ Generator Analysis
✓ Class-wise Analysis
✓ Mean ± Std Analysis
✓ Statistical Testing
