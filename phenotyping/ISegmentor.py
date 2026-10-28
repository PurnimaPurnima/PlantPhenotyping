from abc import ABC, abstractmethod

import numpy as np


class ISegmentor(ABC):
    @abstractmethod
    def segment(self, image: np.ndarray) -> np.ndarray:
        """Return a segmented version of the input image."""
        raise NotImplementedError
