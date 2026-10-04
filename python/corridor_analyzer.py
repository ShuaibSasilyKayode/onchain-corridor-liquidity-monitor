import os
import pandas as pd

# Dynamically resolve file paths relative to this script location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, '..', 'data', 'transactions_sample.csv')

def analyze_corridors(file_path=DATA_PATH):
    if not os.path.exists(file_path):
        print(f"Error: Dataset not found at {file_path}")
        return

    df = pd.read_csv(file_path)

    # Calculate global metrics
    total_txns = len(df)
    successful_df = df[df['status'] == 'SUCCESS']
    total_volume = successful_df['amount_usd'].sum()
    successful_txns = len(successful_df)
    overall_success_rate = (successful_txns / total_txns) * 100 if total_txns > 0 else 0

    print("=" * 75)
    print("      CROSS-BORDER LIQUIDITY & CORRIDOR PERFORMANCE REPORT      ")
    print("=" * 75)
    print(f"Total Transactions Processed : {total_txns}")
    print(f"Total Successful Volume      : ${total_volume:,.2f} USD")
    print(f"Overall Success Rate         : {overall_success_rate:.2f}%\n")

    # Group by Corridor and Payment Rail
    corridor_summary = df.groupby(['corridor', 'payment_rail']).agg(
        Total_Count=('transaction_id', 'count'),
        Success_Count=('status', lambda x: (x == 'SUCCESS').sum()),
        Volume_USD=('amount_usd', lambda x: x[df.loc[x.index, 'status'] == 'SUCCESS'].sum()),
        Avg_Latency_Sec=('latency_seconds', 'mean')
    ).reset_index()

    # Calculate Success Rate
    corridor_summary['Success_Rate_%'] = (
        corridor_summary['Success_Count'] / corridor_summary['Total_Count']
    ) * 100

    # Determine primary failure reason per rail
    failed_df = df[df['status'] != 'SUCCESS']
    
    # Check if a failure_reason column exists, otherwise fall back to status
    reason_col = 'failure_reason' if 'failure_reason' in df.columns else 'status'
    
    if not failed_df.empty:
        primary_bottlenecks = (
            failed_df.groupby(['corridor', 'payment_rail'])[reason_col]
            .agg(lambda x: x.mode()[0] if not x.empty else 'None')
            .reset_index()
            .rename(columns={reason_col: 'Primary_Bottleneck'})
        )
        corridor_summary = pd.merge(
            corridor_summary, primary_bottlenecks, on=['corridor', 'payment_rail'], how='left'
        )
    else:
        corridor_summary['Primary_Bottleneck'] = 'None'

    # Clean up display formatting
    corridor_summary['Primary_Bottleneck'] = corridor_summary['Primary_Bottleneck'].fillna('None')
    corridor_summary['Volume_USD'] = corridor_summary['Volume_USD'].apply(lambda x: f"${x:,.2f}")
    corridor_summary['Success_Rate_%'] = corridor_summary['Success_Rate_%'].apply(lambda x: f"{x:.1f}%")
    corridor_summary['Avg_Latency_Sec'] = corridor_summary['Avg_Latency_Sec'].apply(lambda x: f"{x:.1f}s")

    # Print clean summary table
    print("--- BREAKDOWN BY CORRIDOR & PAYMENT RAIL ---")
    print(
        corridor_summary[
            [
                'corridor',
                'payment_rail',
                'Total_Count',
                'Volume_USD',
                'Success_Rate_%',
                'Avg_Latency_Sec',
                'Primary_Bottleneck',
            ]
        ].to_string(index=False)
    )
    print("=" * 75)

if __name__ == '__main__':
    analyze_corridors()