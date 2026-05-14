import numpy as np


def mean_localization_error(pred_points: np.ndarray, gt_points: np.ndarray) -> float:
    """Berechnet den mittleren euklidischen Abstand zwischen vorhergesagten und Ground-Truth-Keypoints."""
    pred_points = np.asarray(pred_points, dtype=float)
    gt_points = np.asarray(gt_points, dtype=float)
    if pred_points.shape != gt_points.shape:
        raise ValueError("pred_points und gt_points müssen dieselbe Form haben.")
    return float(np.linalg.norm(pred_points - gt_points, axis=1).mean())
