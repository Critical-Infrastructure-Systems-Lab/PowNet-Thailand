import os

import matplotlib.pyplot as plt
import pandas as pd

from pownet.processing.functions import get_dates
from pownet.core.visualize import get_fuel_color_map
from pownet.folder_sys import get_database_dir




# Read the total_dispatch dataframe. Either load from PowNet or read a saved file (must process ourselves)
# from sample_analysis_genmix import total_dispatch
total_dispatch = pd.read_csv('mwh.csv', header=0).drop('Unnamed: 0', axis=1)

'''
[
 'biomass_st', 
 'coal_imp', 'coal_st', 
 'gas_cc', 'gas_gt', 'gas_ic', 'gas_st', 
 'hydro', 'import', 
 'oil_gt', 'oil_ic', 'oil_st', 
 'slack', 'solar', 'wind', 'wsth_st'
 ]
'''

coal_cols = ['coal_imp', 'coal_st']
gas_cols = ['gas_st', 'gas_cc', 'gas_gt', 'gas_ic']
oil_cols = ['oil_gt', 'oil_ic', 'oil_st']

total_dispatch['coal'] = total_dispatch[coal_cols].sum(axis=1)
total_dispatch['gas'] = total_dispatch[gas_cols].sum(axis=1)
total_dispatch['oil'] = total_dispatch[oil_cols].sum(axis=1)

total_dispatch = total_dispatch.drop(coal_cols + gas_cols + oil_cols, axis=1)

column_map = {
    'biomass_st': 'biomass',
    'slack': 'shortfall_positive',
    'wsth_st': 'wsth'
    }
total_dispatch = total_dispatch.rename(column_map, axis=1)
total_dispatch.index += 1

# Fix numerical instability
total_dispatch[total_dispatch < 0] = 0


#%% Plot the annual fuel mix
# Reorder by fuel types for plotting
fuel_mix_order = pd.read_csv(
    os.path.join(get_database_dir(), 'fuels.csv'),
    header = 0,
    )['name']
fuel_mix_order = [fuel for fuel in fuel_mix_order if fuel in total_dispatch.columns]
total_dispatch = total_dispatch[fuel_mix_order]

# Create columns to use later
dates = get_dates(year=2016)
dates.index += 1
timesteps = total_dispatch.shape[0]

monthly_dispatch = total_dispatch.iloc[:timesteps+1].copy()
monthly_dispatch['month'] = dates['date'].dt.to_period('M')
monthly_dispatch = monthly_dispatch.groupby('month').sum()
monthly_dispatch.index = monthly_dispatch.index.strftime('%b')


fig, ax = plt.subplots(figsize=(8, 5))

monthly_dispatch.plot.bar(
    stacked = True,
    ax = ax,
    linewidth = 0,
    color = get_fuel_color_map(),
    legend = False
    )

# Plot formatting
fig.legend(
    loc = 'outside lower center',
    # title = 'Legend',
    ncols = 4,
    fontsize = 'small',
    bbox_to_anchor=(0.5, -0.1)
    )
ax.set_xlabel('')
ax.set_ylabel('Power (MW)')
ax.set_ylim(bottom=0)
plt.show()



#%% Plot the first 48 hours
dispatch_48 = total_dispatch.iloc[:48]


fig, ax = plt.subplots(figsize=(8, 5))

dispatch_48.plot.bar(
    stacked = True,
    ax = ax,
    linewidth = 0,
    color = get_fuel_color_map(),
    legend = False
    )

# Plot formatting
fig.legend(
    loc = 'outside lower center',
    # title = 'Legend',
    ncols = 4,
    fontsize = 'small',
    bbox_to_anchor=(0.5, -0.1)
    )
ax.set_xlabel('')
ax.set_ylabel('Power (MW)')
ax.set_ylim(bottom=0)
plt.show()
