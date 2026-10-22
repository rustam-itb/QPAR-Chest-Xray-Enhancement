# External clinical image dataset

**No patient or clinical image files are included in this repository.**

Use the **Chest X-Ray Images (Pneumonia)** Kaggle dataset (Kermany et al.). Extract the dataset to `data/chest_xray/`, with JPEG images recursively available in the train/test/val subfolders, or set the environment variable `CHEST_XRAY_DIR` to its location.

The benchmark uses **5,856** clinical-source JPEG radiographs, resizes them to **128 × 128** after center cropping, and generates simulated low-dose paired observations. Follow the dataset provider's access and redistribution terms.

The notebook refuses to run the **clinical benchmark** if the JPEG files are missing; synthetic hand phantoms are not a valid substitute.
