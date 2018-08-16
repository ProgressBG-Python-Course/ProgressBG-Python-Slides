import pandas as pd
import pytest
from transform import calculate_transaction_volume

@pytest.fixture
def sample_data():
    data = {
        'transaction_id': [1, 2, 3],
        'quantity': [2, 5, 3],
        'unit_price': [10, 8, 12]
    }
    df = pd.DataFrame(data)
    return df

def test_calculate_transaction_volume(sample_data):
    # Calculate transaction volume
    result_df = calculate_transaction_volume(sample_data)
    # Assert that transaction_volume is calculated correctly
    for _, row in result_df.iterrows():
        expected_volume = row['quantity'] * row['unit_price']
        assert row['transaction_volume'] == expected_volume, f"Transaction volume calculated incorrectly for transaction_id={row['transaction_id']}"
