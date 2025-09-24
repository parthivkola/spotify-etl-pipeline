import pandas as pd
import pytest
from etl_project.transform import transform_data


def test_transform_data():
    # Mock dataset
    data = {
        "track_name": ["Song A", "Song B"],
        "duration_ms": [180000, 240000],
        "popularity": [80, 60]
    }
    df = pd.DataFrame(data)

    transformed = transform_data(df)

    # Only Song A should remain (popularity > 70)
    assert len(transformed) == 1
    assert "duration_min" in transformed.columns
    assert transformed.iloc[0]["duration_min"] == 3.0
