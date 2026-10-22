"""Direct classical equivalent of the QPAR cyclic two-tap filter.

Returns uint8 exactly as in the accompanying benchmark notebook.
"""
from __future__ import annotations

import numpy as np


class BoxFilterClassical:
    """Two successive weighted cyclic shifts, applied independently to patches."""

    def __init__(self, patch: int = 8, s: float = 0.25):
        if patch < 1 or patch & (patch - 1):
            raise ValueError("patch must be a positive power of two")
        if not 0 <= s <= 0.5:
            raise ValueError("s must be in [0, 0.5]")
        self.patch, self.s = patch, float(s)

    def process(self, img: np.ndarray) -> np.ndarray:
        """Process a 2-D grayscale uint8 image using patchwise cyclic averaging."""
        if img.ndim != 2:
            raise ValueError("expected a 2-D grayscale image")
        p, s = self.patch, self.s
        h, w = img.shape
        ph, pw = (p - h % p) % p, (p - w % p) % p
        f = np.pad(img.astype(np.float64), ((0, ph), (0, pw)), mode="reflect")
        out = np.empty_like(f)
        for i in range(0, f.shape[0], p):
            for j in range(0, f.shape[1], p):
                blk = f[i:i+p, j:j+p]
                bx = (1 - s) * blk + s * np.roll(blk, 1, axis=1)
                by = (1 - s) * bx + s * np.roll(bx, 1, axis=0)
                out[i:i+p, j:j+p] = by
        return np.clip(out[:h, :w], 0, 255).astype(np.uint8)
