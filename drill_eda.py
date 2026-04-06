import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def compute_summary(df):
    summary = df.describe()
    summary.loc['median'] = df.median(numeric_only=True)
    
    rows_to_keep = ['count', 'mean', 'median', 'std', 'min', 'max']
    summary = summary.loc[rows_to_keep]
    
    summary.to_csv('output/summary.csv')
    return summary

def plot_distributions(df, columns, output_path):
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes_flat = axes.flatten()
    
    for i, col in enumerate(columns):
        if i < len(axes_flat):
            sns.histplot(data=df, x=col, kde=True, ax=axes_flat[i])
            axes_flat[i].set_title(f'Distribution of {col}')
    
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def plot_correlation(df, output_path):
    # Select only numeric columns for correlation
    numeric_df = df.select_dtypes(include=['number'])
    corr_matrix = numeric_df.corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')
    
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

if __name__ == "__main__":
    # Create output directory if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')

    # Load data
    df = pd.read_csv('data/sample_sales.csv')
    
    # Task 1
    compute_summary(df)
    
    # Task 2
    # Identifying numeric columns for the plot
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    # Use the first 4 numeric columns or as many as available
    plot_distributions(df, numeric_cols[:4], 'output/distributions.png')
    
    # Task 3
    plot_correlation(df, 'output/correlation.png')
    
    print("All tasks completed. Check the 'output' directory.")