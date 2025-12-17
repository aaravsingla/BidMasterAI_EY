import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set the visual style
sns.set_style("whitegrid")
plt.rcParams['font.family'] = 'sans-serif'

# ==========================================
# CHART 1: TIME IMPACT ANALYSIS (Stacked Bar)
# ==========================================
def create_impact_chart():
    # Data: Time in Hours
    # Manual Process (Total ~5 Days = 40 Hours working time)
    manual_data = {
        'Phase': 'Manual Process',
        'RFP Discovery': 4,
        'Tech Matching': 24, # 3 Days
        'Pricing & Calc': 8, # 1 Day
        'Human Review': 0    # Built into the process
    }

    # BidMaster AI (Total ~45 Mins = 0.75 Hours)
    ai_data = {
        'Phase': 'BidMaster AI',
        'RFP Discovery': 0.1, # 6 mins
        'Tech Matching': 0.1, # 6 mins
        'Pricing & Calc': 0.1, # 6 mins
        'Human Review': 0.5   # 30 mins
    }

    df = pd.DataFrame([manual_data, ai_data])
    
    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create Stacked Bars
    phases = ['RFP Discovery', 'Tech Matching', 'Pricing & Calc', 'Human Review']
    colors = ['#FFC20E', '#2E2E38', '#808080', '#28a745'] # EY Colors (Yellow, Black, Grey, Green)
    
    df.set_index('Phase')[phases].plot(kind='bar', stacked=True, color=colors, ax=ax, width=0.4)

    # Styling
    ax.set_title("Process Cycle Time: Manual vs. BidMaster AI", fontsize=16, fontweight='bold', pad=20)
    ax.set_ylabel("Time (Working Hours)", fontsize=12)
    ax.set_xlabel("")
    plt.xticks(rotation=0, fontsize=12)
    
    # Add Text Annotations
    for c in ax.containers:
        ax.bar_label(c, fmt='%.1f h', label_type='center', color='white', fontsize=10, weight='bold')

    # Add Total Time Labels on top
    totals = df.set_index('Phase')[phases].sum(axis=1)
    for i, total in enumerate(totals):
        ax.text(i, total + 1, f"Total: {total:.1f} Hrs", ha='center', fontsize=12, fontweight='bold', color='black')

    plt.legend(title="Process Phase", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    
    # Save
    plt.savefig('chart_time_impact.png', dpi=300)
    print("✅ Generated 'chart_time_impact.png'")
    plt.show()

# ==========================================
# CHART 2: GAP ANALYSIS HEATMAP
# ==========================================
def create_heatmap():
    # Data: 0 = Critical Gap (Red), 1 = Deviation (Yellow), 2 = Match (Green)
    data = [
        [2, 2, 0], # Voltage: Match, Match, Fail
        [2, 2, 2], # Conductor: Match, Match, Match
        [2, 1, 0], # Armour: Match, Deviation, Fail
        [2, 2, 2], # Insulation: Match, Match, Match
        [2, 0, 0]  # Sheath: Match, Fail, Fail
    ]
    
    columns = ['Internal SKU A\n(Best Match)', 'Internal SKU B\n(Partial)', 'Internal SKU C\n(No-Bid)']
    rows = ['Voltage Grade', 'Conductor Material', 'Armour Type', 'Insulation Type', 'Sheath Property']
    
    df_heat = pd.DataFrame(data, columns=columns, index=rows)

    # Plotting
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Custom Color Map (Red -> Yellow -> Green)
    cmap = sns.color_palette(["#dc3545", "#ffc107", "#28a745"]) 
    
    sns.heatmap(df_heat, cmap=cmap, annot=False, cbar=False, linewidths=1, linecolor='white', square=True)

    # Styling
    ax.set_title("Automated Parametric Gap Analysis", fontsize=16, fontweight='bold', pad=20)
    plt.yticks(rotation=0, fontsize=11)
    plt.xticks(fontsize=11)

    # Custom Legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#28a745', label='Exact Match'),
        Patch(facecolor='#ffc107', label='Minor Deviation (<5%)'),
        Patch(facecolor='#dc3545', label='Critical Gap (Make-to-Order)')
    ]
    ax.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3, frameon=False)

    plt.tight_layout()
    
    # Save
    plt.savefig('chart_gap_analysis.png', dpi=300)
    print("✅ Generated 'chart_gap_analysis.png'")
    plt.show()

if __name__ == "__main__":
    create_impact_chart()
    create_heatmap()