# Result provenance

`recorded_aggregate_metrics.csv` is a **transcription of console output that was already saved in the uploaded student's executed Jupyter notebook**. These numbers have **not** been recomputed by this package; they are rounded summary values rather than individual observations. They are provided to help a reader understand which aggregate values were actually recorded.

Important discrepancies relative to earlier paper files:

- The saved console output rounds clinical **Hybrid PSNR to 20.53 dB**, whereas one manuscript Table I version reported **20.54 dB**.
- The saved console output rounds chest-phantom Conventional SSIM to **0.420**, whereas one manuscript Table II version reported **0.422**.
- The chest-phantom conventional-minus-hybrid SSIM difference was printed as **+0.041** at higher precision in the original execution, even though subtracting the separately rounded numbers (0.420 - 0.380) gives 0.040.
- Clinical and phantom runtimes should not be mixed; measurements depend on execution environment.

**Per-image results are NOT included**: they were not persisted as CSV in the uploaded original notebook. Only rerunning the clinical benchmark and then executing its export cell can generate `clinical_per_image_metrics.csv`, `clinical_summary.json`, and `execution_manifest.json`. Do not claim these raw files are available on GitHub unless actually added later.
