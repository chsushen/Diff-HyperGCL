# Loss Ablation Study

L1 = Cross Entropy Classification Loss

L2 = Classification Loss + Contrastive Loss

L3 = Classification Loss + Diffusion Reconstruction Loss

L4 = Full Model (Classification + Contrastive + Diffusion Loss)

Datasets:
- MIntRec
- MIntRec2.0

Models:
- DG+DG (Dual Diffusion Generator)
- HC+DG (Handcrafted View + Diffusion Generator)

Metrics:
ACC, Precision, Recall, F1, Weighted Precision,
Weighted Recall, Weighted F1
