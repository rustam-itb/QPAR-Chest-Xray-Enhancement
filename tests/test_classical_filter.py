"""Deterministic, dataset-free checks of the public classical equivalent."""
import numpy as np
import pytest
from src.qpar_classical import BoxFilterClassical


def test_constant_image_invariant():
    arr = np.full((16, 16), 127, dtype=np.uint8)
    np.testing.assert_array_equal(BoxFilterClassical().process(arr), arr)


def test_manual_two_tap_cyclic_average():
    arr = np.arange(64, dtype=np.uint8).reshape(8, 8)
    s = 0.25
    x = (1 - s) * arr.astype(float) + s * np.roll(arr.astype(float), 1, axis=1)
    expected = (1 - s) * x + s * np.roll(x, 1, axis=0)
    result = BoxFilterClassical(patch=8, s=s).process(arr)
    np.testing.assert_array_equal(result, expected.astype(np.uint8))


def test_identity_at_zero_strength():
    arr = np.random.default_rng(123).integers(0, 256, (16, 24), dtype=np.uint8)
    np.testing.assert_array_equal(BoxFilterClassical(s=0).process(arr), arr)


def test_non_divisible_shape():
    arr = np.random.default_rng(123).integers(0, 256, (9, 11), dtype=np.uint8)
    assert BoxFilterClassical(patch=8).process(arr).shape == arr.shape


def test_invalid_strength():
    with pytest.raises(ValueError):
        BoxFilterClassical(s=0.6)
