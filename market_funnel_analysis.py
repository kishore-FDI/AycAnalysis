import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ------------------ Market Sizing Model ------------------

def compute_sam_som(tam, sam_pct, som_pct):
    sam = tam * sam_pct
    som = sam * som_pct
    return sam, som

sectors = ["Education", "Healthcare", "Hospitality", "Social Impact", "Branding/SMEs"]
tam_2024 = np.array([169.2, 312.9, 4673.63, 87.5269, 34.03])  # USD Billions
sam_pct = np.array([0.30, 0.25, 0.20, 0.50, 0.40])
som_pct = np.array([0.10, 0.10, 0.05, 0.20, 0.10])

sam_2024, som_2024 = compute_sam_som(tam_2024, sam_pct, som_pct)

df_market = pd.DataFrame({
    "Sector": sectors,
    "TAM_2024 (B)": tam_2024,
    "SAM_2024 (B)": sam_2024,
    "SOM_2024 (B)": som_2024
})

print("\nMarket Sizing Summary:")
print(df_market.to_markdown(index=False))

cagr = np.array([0.181, 0.212, 0.068, 0.20, 0.0553])
years = np.arange(2024, 2031)
projected_tam = {sector: tam_2024[i] * (1 + cagr[i])**(years - 2024)
                 for i, sector in enumerate(sectors)}

plt.figure(figsize=(8, 5))
for sector in sectors:
    plt.plot(years, projected_tam[sector], label=sector)
plt.title("Projected TAM by Sector (2024–2030)")
plt.xlabel("Year")
plt.ylabel("TAM (USD Billions)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# ------------------ Client Acquisition Funnel ------------------

def simulate_funnel(initial_leads, conversion_rates):
    leads = [initial_leads]
    for rate in conversion_rates:
        leads.append(leads[-1] * rate)
    return leads

stages = ["Awareness", "Interest", "Consideration", "Proposal", "Engagement"]
conversion_rates = [0.20, 0.30, 0.25, 0.40]
initial_leads = 10000

lead_counts = simulate_funnel(initial_leads, conversion_rates)

df_funnel = pd.DataFrame({
    "Stage": stages,
    "Leads": [int(x) for x in lead_counts]
})

print("\nClient Acquisition Funnel:")
print(df_funnel.to_markdown(index=False))

plt.figure(figsize=(6, 4))
plt.barh(stages[::-1], lead_counts[::-1], color='darkcyan')
plt.title("Client Acquisition Funnel")
plt.xlabel("Leads")
plt.tight_layout()
plt.show()
