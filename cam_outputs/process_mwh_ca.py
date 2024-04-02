import os

import matplotlib.pyplot as plt
import pandas as pd

from pownet.processing.functions import get_dates
from pownet.core.visualize import get_fuel_color_map
from pownet.folder_sys import get_database_dir



# Need to map each generator to its fuel type
gen_map = pd.read_csv('data_camb_genparams.csv', usecols=['name', 'typ'])
gen_map = gen_map.set_index('name').to_dict()['typ']

set(gen_map.values())

# We will collect the annual dispatch to this dataframe
total_dispatch = pd.DataFrame()

# Thermal units
gen_thermo = pd.read_csv(
    'out_camb_R1_2016'+'_mwh.csv',header=0
    ).drop('Unnamed: 0', axis=1)
gen_thermo['Type'] = gen_thermo['Generator'].map(gen_map)
gen_thermo = gen_thermo.drop('Generator', axis=1)

gen_thermo = gen_thermo.groupby(['Time', 'Type']).sum()
gen_thermo = gen_thermo.reset_index()
gen_thermo = gen_thermo.pivot(columns='Type', index='Time')
gen_thermo.columns = gen_thermo.columns.get_level_values(1)
total_dispatch = gen_thermo.reset_index(drop=True)

# Hydro
gen_hydro = pd.read_csv(
    'out_camb_R1_2016'+'_hydro.csv',header=0).drop('Unnamed: 0', axis=1)
gen_hydro = gen_hydro.groupby(['Time']).sum()
gen_hydro = gen_hydro.reset_index(drop=True)
gen_hydro = gen_hydro.drop('Node', axis=1)
gen_hydro = gen_hydro.reset_index(drop=True)

total_dispatch['hydro'] = gen_hydro.Value


# Import (Hydro)
gen_hydro_import = pd.read_csv(
    'out_camb_R1_2016'+'_hydro_import.csv',header=0
    ).drop('Unnamed: 0', axis=1)
gen_hydro_import = gen_hydro_import.groupby(['Time']).sum()
gen_hydro_import = gen_hydro_import.reset_index(drop=True)
gen_hydro_import = gen_hydro_import.drop('Node', axis=1)
gen_hydro_import = gen_hydro_import.reset_index(drop=True)
    
total_dispatch['hydro_import'] = gen_hydro_import.Value


############ Time to plot the fuel mix!
'''
[
'coal_st', 
'imp_thai', 
'imp_viet', 
'oil_ic', 
'oil_st', 
'slack'
 ]
'''

column_map = {
    'coal_st': 'coal',
    'oil_ic': 'oil',
    'oil_st': 'oil',
    'slack': 'shortfall',
    }
total_dispatch = total_dispatch.rename(column_map, axis=1)

import_cols = ['imp_thai', 'imp_viet', 'hydro_import']
total_dispatch['import'] = total_dispatch[import_cols].sum(axis=1)
total_dispatch = total_dispatch.drop(import_cols, axis=1)

total_dispatch.index += 1

total_dispatch[total_dispatch < 0] = 0


#%%===================== Plot the annual fuel mix
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


# Plot section
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
