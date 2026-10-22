# Chest X-ray enhancement: conventional, QPAR, and hybrid comparison

Research code accompanying the conference paper **“Conventional, Quantum-Simulated, and Hybrid Enhancement of Simulated Low-Dose Chest Radiographs: Measured Performance and Phantom-Induced Ranking Reversal”**, by Bryan Gabriel Izaac Sasabone and Rustam (Telkom University).

## What is included

- `notebooks/X_Ray_Quantum_Enhancement.ipynb`: executable source for the NLM–CLAHE baseline, quantum-simulated QPAR, direct classical QPAR equivalent, QPAR–CLAHE hybrid, reversed-order hybrid, paired degradation, fidelity metrics, and chest/hand phantom generators. Outputs have been cleared before publication.
- `src/qpar_classical.py`: standalone implementation of the mathematically equivalent separable two-tap cyclic averaging filter.
- `tests/test_classical_filter.py`: fast, dataset-free tests of the direct classical filter.
- `results/recorded_aggregate_metrics.csv`: **rounded aggregate values transcribed from the saved output of the original executed student notebook**, not newly recomputed data.
- `data/README.md` and `results/README.md`: dataset instructions and result-provenance notes.

## Reproduce the clinical experiment

1. Install Python 3.11 or 3.12 in a clean virtual environment; install the packages below. The original saved notebook executed on a different Python environment, so cross-platform runtimes need not match.

   ```bash
   python -m venv .venv
   # Activate .venv for your operating system, then:
   python -m pip install -r requirements.txt
   python -m ipykernel install --user --name qpar-xray --display-name "QPAR X-ray"
   ```

2. Download **Chest X-Ray Images (Pneumonia)** (Kermany et al.) from Kaggle separately. Place the extracted JPEGs in `data/chest_xray/` or set `CHEST_XRAY_DIR` to the folder containing the dataset. **The clinical data are NOT bundled**, and the code refuses to use a phantom substitute if the chest-X-ray files are absent. See `data/README.md`.
3. Start Jupyter in the repository root, open `notebooks/X_Ray_Quantum_Enhancement.ipynb`, select the QPAR X-ray kernel, and run cells in sequence. Running the 5,856-image benchmark is an independent reproduction attempt and requires local computing resources.
4. After the clinical benchmark, the optional export cell produces individual metrics and an environment manifest under `results/`. The plot cells generate files under `figures/`.
5. To rerun the phantom controls, set `RUN_PHANTOM_CONTROL = True` in the notebook; this runs a separate experiment and is off by default.

## Algorithmic distinction

QPAR is constructed with Qiskit, but its image-processing path computes a **dense unitary** with `qiskit.quantum_info.Operator` and multiplies that matrix by a NumPy state vector. These results **do not measure quantum hardware or per-image Aer execution**. The direct classical equivalent is a separable, patchwise two-tap cyclic filter. Both should match to within a gray level after 8-bit quantization.

The study evaluates quantum-representation/simulation overhead and phantom-dependent ranking. It **does not** establish quantum-hardware advantage or diagnostic utility, nor benchmark modern learned denoisers such as DnCNN and U-Net.

## Reproduced vs. reported results

The file `results/recorded_aggregate_metrics.csv` contains the *saved output* of a prior clinical and phantom execution. The clinical benchmark used **5,856** image pairs. It reported the following rounded clinical results:

| Method | Mean runtime (ms/image) | SSIM | PSNR (dB) |
|---|---:|---:|---:|
| Conventional (NLM–CLAHE) | 18.67 | 0.388 | 17.26 |
| Pure QPAR (dense-unitary emulation) | 31.30 | 0.390 | 20.71 |
| Classical equivalent | 3.93 | 0.390 | 20.71 |
| Hybrid (QPAR–CLAHE) | 31.41 | 0.394 | 20.53 |

The original console output differs in a few rounded values from an earlier manuscript version. Details appear in `results/README.md`; the table here should **not** be described as a new, independent rerun.

## Quick local tests

```bash
python -m pytest -q
```

The tests require NumPy but do not require clinical images or quantum hardware. The full Qiskit/classical equivalence sanity check is in the notebook.

## Repository scope and release notes

- No clinical images, patient records, download credentials, raw per-image records, or runtime notebook output cells are included. The dataset must be obtained from its provider, subject to the provider's terms.
- The earlier manuscript's mixing-strength curve is omitted: the original executed notebook did not contain a reproducible sweep for it.
- The GitHub link will become available **only after you create and publish this repository**. Do not put a placeholder or invented URL in the manuscript.
- No software license has been selected by the authors in this package. Choose and add an appropriate `LICENSE` file if you intend to grant reuse rights.
