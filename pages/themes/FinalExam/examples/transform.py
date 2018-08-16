import pandas as pd
import logging

# Setup basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Transformation function with a logical error
def calculate_transaction_volume(df):
    # Incorrect logic for demonstration purposes
    df['transaction_volume'] = df['quantity'] * df['unit_price']
    logging.info("Transaction volume calculated.")
    return df