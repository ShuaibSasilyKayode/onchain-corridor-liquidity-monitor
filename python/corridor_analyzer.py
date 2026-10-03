import pandas as pd

def analyze_corridors(file_path):
    df = pd.read_csv(file_path)
    
    total_txns = len(df)
    total_volume = df[df['status'] == 'SUCCESS']['amount_usd'].sum()
    successful_txns = len(df[df['status'] == 'SUCCESS'])
    overall_success_rate = (successful_txns / total_txns) * 100
    
    print("=" * 65)
    print("      CROSS-BORDER LIQUIDITY & CORRIDOR PERFORMANCE REPORT      ")
    print("=" * 65)
    print(f"Total Transactions Processed : {total_txns}")
    print(f"Total Successful Volume      : ${total_volume:,.2f} USD")
    print(f"Overall Success Rate         : {overall_success_rate:.2f}%\n")
    
    corridor_summary = df.groupby(['corridor', 'payment_rail']).agg(
        Total_Count=('transaction_id', 'count'),
        Success_Count=('status', lambda x: (x == 'SUCCESS').sum()),
        Volume_USD=('amount_usd', lambda x: x[df.loc[x.index, 'status'] == 'SUCCESS'].sum()),
        Avg_Latency_Sec=('latency_seconds', 'mean')
    ).reset_index()
    
    corridor_summary['Success_Rate_%'] = ((corridor_summary['Success_Count'] / corridor_summary['Total_Count']) * 100).round(2)
    corridor_summary['Avg_Latency_Sec'] = corridor_summary['Avg_Latency_Sec'].round(1)
    corridor_summary['Volume_USD'] = corridor_summary['Volume_USD'].map("${:,.2f}".format)
    
    print("--- CORRIDOR BREAKDOWN ---")
    print(corridor_summary[['corridor', 'payment_rail', 'Volume_USD', 'Success_Rate_%', 'Avg_Latency_Sec']].to_string(index=False))
    
    failures = df[df['status'] == 'FAILED']
    if not failures.empty:
        print("\n--- FAILURE REASON AUDIT ---")
        failure_summary = failures.groupby('failure_reason')['transaction_id'].count().reset_index()
        failure_summary.columns = ['Failure Reason', 'Count']
        print(failure_summary.to_string(index=False))

if __name__ == "__main__":
    analyze_corridors('../data/transactions_sample.csv')