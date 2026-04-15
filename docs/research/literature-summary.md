# Literature Review Summary

Systematic review following **PRISMA** methodology.

- **Initial papers identified:** 287 (IEEE Xplore, Google Scholar, arXiv, ACM)
- **After duplicate removal:** 224
- **After title/abstract screening:** 89
- **Final included papers:** 16

---

## 5 Key Themes

### Theme 1: CNN Baselines and Their Limitations
- Mohanty et al. (2016): AlexNet/GoogleNet on PlantVillage → 99.35% (lab conditions only)
- Ferentinos (2018): VGG/ResNet → 99.5% (controlled images, overfits)
- Too et al. (2019): Fine-tuned VGG16 → 99.7% (no field validation)
- **Gap:** High lab accuracy collapses by 15-20% in real field conditions (Singh et al., 2020)

### Theme 2: Vision Transformers for Plant Disease
- Dosovitskiy et al. (2020): ViT requires 14M+ training images
- Thakur et al. (2023): PlantViT — 96% accuracy but no mobile app, no security
- Kumar et al. (2024): Systematic review — ViT outperforms CNNs by 2-5%
- **Gap:** No agricultural ViT system with full security stack

### Theme 3: Knowledge Distillation as Solution
- Hinton et al. (2015): Distillation improves student accuracy by 3-8%
- Touvron et al. (2021): **DeiT** — 83.1% ImageNet with 12× less data than ViT
- Kumar et al. (2024): DeiT outperforms CNN baselines by 2-3% on PlantVillage
- **Our use:** ResNet-50 teacher → DeiT-Tiny student

### Theme 4: Mobile Deployment
- Mehta & Rastegari (2021): MobileViT — 78% ImageNet, mobile-friendly
- Li et al. (2023a): PMVT — 92% on custom dataset (no security)
- **Gap:** All mobile systems ignore security architecture

### Theme 5: Security & Privacy
- Zhang et al. (2022): Proposed encryption — conceptual only, no implementation
- Sharma et al. (2024): Federated learning — communication overhead too high for rural networks
- **Gap:** No production agricultural AI system with documented, auditable security stack

---

## Critical Gap (Our Contribution)

No existing system combines:
1. ✅ Data-efficient transformer (DeiT with knowledge distillation)
2. ✅ Defense-in-depth security stack (JWT + TLS 1.3 + Magic Bytes + rate limiting)
3. ✅ Deterministic treatment engine (no hallucination risk)

---

## Literature Matrix

| Author | Year | Method | Dataset | Accuracy | Key Finding | Limitation |
|--------|------|--------|---------|----------|-------------|-----------|
| Mohanty et al. | 2016 | AlexNet/GoogleNet | PlantVillage (54k) | 99.35% | DL works on plant diseases | Poor real-world generalization |
| Ferentinos | 2018 | VGG, ResNet | Custom (87k) | 99.5% | Deeper models improve accuracy | High compute, overfitting |
| Too et al. | 2019 | Fine-tuned VGG16 | PlantVillage | 99.7% | Transfer learning reduces training | No field validation |
| Dosovitskiy et al. | 2020 | ViT | ImageNet | High | Global attention patterns | Needs 14M+ images |
| Singh et al. | 2020 | ResNet-50 | PlantDoc (2.5k) | Baseline | First real-world field dataset | Small dataset |
| Thapa et al. | 2020 | Mobile CNN | Apple dataset | 88% | Smartphone deployment | Limited classes, no security |
| Touvron et al. | 2021 | **DeiT** | ImageNet | 83.1% | Knowledge distillation for ViT | Not tested on agricultural data |
| Mehta & Rastegari | 2021 | MobileViT | ImageNet | 78% | Mobile-friendly ViT | Accuracy-efficiency tradeoff |
| Zhang et al. | 2022 | Secure AI | Theoretical | N/A | Proposed encryption | Conceptual, no implementation |
| Chen et al. | 2023 | MobileNet | PlantVillage | 94% | Channel attention improves features | Lab images only |
| Li et al. (a) | 2023 | PMVT | Custom | 92% | Mobile ViT for plant diseases | No security |
| Li et al. (b) | 2023 | Mobile ViT | ImageNet | 79% | Speed-accuracy optimization | General purpose |
| Thakur et al. | 2023 | PlantViT | PlantVillage | 96% | ViT designed for plants | No mobile, no security |
| Kumar et al. | 2024 | CNN vs ViT | PV + PlantDoc | N/A | ViT beats CNN by 2-5% | Review paper |
| Liu et al. | 2024 | Attention CNN | Grape dataset | 95% | Hybrid attention features | Complex, slow training |
| Singh et al. | 2024 | ViT + GAN | Synthetic | 97% | GAN improves generalization | Synthetic data quality |
