import os
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

yr = 2016


mwh_q1 = pd.read_csv('./output/out_thai_v1_'+str(yr)+'_q1_mwh.csv',header=0)
mwh_q2 = pd.read_csv('./output/out_thai_v1_'+str(yr)+'_q2_mwh.csv',header=0)    
mwh_q3 = pd.read_csv('./output/out_thai_v1_'+str(yr)+'_q3_mwh.csv',header=0)
mwh_q4 = pd.read_csv('./output/out_thai_v1_'+str(yr)+'_q4_mwh.csv',header=0)

hydro_q1 = pd.read_csv('./output/out_thai_v1_'+str(yr)+'_q1_hydro.csv',header=0)
hydro_q2 = pd.read_csv('./output/out_thai_v1_'+str(yr)+'_q2_hydro.csv',header=0)
hydro_q3 = pd.read_csv('./output/out_thai_v1_'+str(yr)+'_q3_hydro.csv',header=0)
hydro_q4 = pd.read_csv('./output/out_thai_v1_'+str(yr)+'_q4_hydro.csv',header=0)

hydro_import_q1 = pd.read_csv('./output/out_thai_v1_'+str(yr)+'_q1_hydro_import.csv',header=0)
hydro_import_q2 = pd.read_csv('./output/out_thai_v1_'+str(yr)+'_q2_hydro_import.csv',header=0)
hydro_import_q3 = pd.read_csv('./output/out_thai_v1_'+str(yr)+'_q3_hydro_import.csv',header=0)
hydro_import_q4 = pd.read_csv('./output/out_thai_v1_'+str(yr)+'_q4_hydro_import.csv',header=0)

solar_q1 = pd.read_csv('./output/out_thai_v1_'+str(yr)+'_q1_solar.csv',header=0)
solar_q2 = pd.read_csv('./output/out_thai_v1_'+str(yr)+'_q2_solar.csv',header=0)
solar_q3 = pd.read_csv('./output/out_thai_v1_'+str(yr)+'_q3_solar.csv',header=0)
solar_q4 = pd.read_csv('./output/out_thai_v1_'+str(yr)+'_q4_solar.csv',header=0)

wind_q1 = pd.read_csv('./output/out_thai_v1_'+str(yr)+'_q1_wind.csv',header=0)
wind_q2 = pd.read_csv('./output/out_thai_v1_'+str(yr)+'_q2_wind.csv',header=0)
wind_q3 = pd.read_csv('./output/out_thai_v1_'+str(yr)+'_q3_wind.csv',header=0)
wind_q4 = pd.read_csv('./output/out_thai_v1_'+str(yr)+'_q4_wind.csv',header=0)



gen_thermo = pd.concat([mwh_q1,mwh_q2,mwh_q3,mwh_q4])
df_gen = pd.read_csv('./input/data_thai_thermo_2016.csv',header=0)
gen_name = df_gen['name']
gen_type = df_gen['typ']
for x in range(len(gen_name)):
    gen_thermo.loc[gen_thermo.Generator == gen_name[x], 'Type'] = gen_type[x]
gen_thermo = gen_thermo[['Time', 'Value', 'Type']]


gen_hydro = pd.concat([hydro_q1,hydro_q2,hydro_q3,hydro_q4])
gen_hydro = gen_hydro[['Time', 'Value']]
gen_hydro['Type'] = 'hydro'


gen_hydro_import = pd.concat([hydro_import_q1,hydro_import_q2,hydro_import_q3,hydro_import_q4])
gen_hydro_import = gen_hydro_import[['Time', 'Value']]
gen_hydro_import['Type'] = 'import'

gen_solar = pd.concat([solar_q1,solar_q2,solar_q3,solar_q4])
gen_solar = gen_solar[['Time', 'Value']]
gen_solar['Type'] = 'solar'


gen_wind = pd.concat([wind_q1,wind_q2,wind_q3,wind_q4])
gen_wind = gen_wind[['Time', 'Value']]
gen_wind['Type'] = 'wind'


mwh = pd.concat(
    [gen_thermo, gen_hydro, gen_hydro_import, gen_solar, gen_wind],
    axis = 0)
mwh = mwh.groupby(['Type', 'Time']).sum().unstack('Type').reset_index()
mwh.reset_index()


mwh_subset = mwh[mwh['Time'] < 25]
mwh_subset.columns = mwh_subset.columns.get_level_values(1)
mwh_subset = mwh_subset.drop('', axis=1)

mwh_subset['coal'] = mwh_subset['coal_imp'] + mwh_subset['coal_st']
mwh_subset['gas'] = mwh_subset['gas_cc'] \
    + mwh_subset['gas_gt'] + mwh_subset['gas_ic'] + + mwh_subset['gas_st']
mwh_subset['oil'] = mwh_subset['oil_gt'] \
    + mwh_subset['oil_ic'] + mwh_subset['oil_st']
    
cols2drop = [
    'coal_imp', 'coal_st', 'gas_cc', 'gas_gt', 'gas_ic', 'gas_st',
    'oil_gt', 'oil_ic', 'oil_st'
    ]

mwh_subset = mwh_subset.drop(cols2drop, axis=1)


fig, ax = plt.subplots()
mwh_subset.plot(kind='bar', stacked=True, ax=ax)
ax.legend(bbox_to_anchor=(1, 1.05))
plt.show()


###########
thermo_bytype = round(gen_thermo.groupby(['Type'])['Value'].sum()/1000,1)
hydro_byplant = round(gen_hydro.groupby(['Node'])['Value'].sum()/1000,1)
hydro_import_byplant = round(gen_hydro_import.groupby(['Node'])['Value'].sum()/1000,1)
solar_byplant = round(gen_solar.groupby(['Node'])['Value'].sum()/1000,1)
wind_byplant = round(gen_wind.groupby(['Node'])['Value'].sum()/1000,1)



hydro_gwh = sum(hydro_byplant)
hydro_import_gwh = sum(hydro_import_byplant)
solar_gwh = sum(solar_byplant)
wind_gwh = sum(wind_byplant)

gen_gwh = thermo_bytype
gen_gwh['hydro'] = hydro_gwh
gen_gwh['hydro_import'] = hydro_import_gwh
gen_gwh['solar'] = solar_gwh
gen_gwh['wind'] = wind_gwh

gen_gwh, sum(gen_gwh)

