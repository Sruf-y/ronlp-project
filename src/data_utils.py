"""Runtime-agnostic dataset loaders.
Works locally (WSL2) and in Colab without modification."""

import os
from datasets import load_from_disk, load_dataset

PROJECT_ROOT = "/home/botofan/ronlp-project"
LAROSEDA_LOCAL = f"{PROJECT_ROOT}/data/laroseda_hf"
RONEC_LOCAL    = f"{PROJECT_ROOT}/data/ronec_hf"


def get_laroseda():
    """Return LaRoSeDa DatasetDict. Uses local cache if present, else downloads."""
    if os.path.exists(LAROSEDA_LOCAL):
        return load_from_disk(LAROSEDA_LOCAL)
    return load_dataset("universityofbucharest/laroseda")


def get_ronec():
    """Return RONEC DatasetDict."""
    if os.path.exists(RONEC_LOCAL):
        return load_from_disk(RONEC_LOCAL)
    return load_dataset("community-datasets/ronec")
