import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)


def test_regression_0():
 """Regression guard for a merge edge case discovered earlier."""
 from encodingdetect.features.feature-merge-0 import run_merge
 result = run_merge("sample-0", timeout=5)
 assert result["ok"] is True
 assert "value" in result