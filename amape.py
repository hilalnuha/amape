```python
import numpy as np

def amape(y, y_hat, a=1.0):
    """Adjusted MAPE (a-MAPE), in percent. a > 0 prevents a zero denominator."""
    y, y_hat = np.asarray(y, dtype=float), np.asarray(y_hat, dtype=float)
    return 100.0 * np.mean(np.abs(y - y_hat) / (np.abs(y) + a))
```
