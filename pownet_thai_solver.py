from pyomo.opt import SolverFactory, SolverStatus
from pyomo.core import Var
from pyomo.core import Param
from operator import itemgetter
import pandas as pd
from datetime import datetime
import os


yr = 2016


##run pownet (a year will run in four quarters)
for q in range(0,4):
    if q == 0:
        start = 1
        end  = 90      

    if q == 1:
        start = 91
        end  = 181        

    if q == 2:
        start = 182
        end  = 273        

    if q == 3:
        start = 274
        end  = 365 
        
    from pownet_thai_model import model
    ##create instance with data
    instance = model.create_instance('./input/pownet_thai_v1_data_'+str(yr)+'.dat')
    
    ##solver, threads    
    opt = SolverFactory("gurobi") ##gurobi SolverFactory("CPLEX")
    opt.options["threads"] = 1
    opt.options["TimeLimit"] = 120 ##in seconds 
    H = instance.HorizonHours
    K=range(1,H+1)        
        
        
    #Space to store results
    on=[]
    switch=[]

    mwh=[]
    hydro=[]
    solar=[]
    wind=[]

    hydro_import=[]

    srsv=[]
    nrsv=[]

    vlt_angle=[]

    for day in range(start,end+1):
        for z in instance.d_nodes:
         #load Demand and Reserve time series data
            for i in K:
                instance.HorizonDemand[z,i] = instance.SimDemand[z,(day-1)*24+i]
                instance.HorizonReserves[i] = instance.SimReserves[(day-1)*24+i] 

        for z in instance.h_nodes:
         #load Hydropower time series data
            for i in K:
                instance.HorizonHydro[z,i] = instance.SimHydro[z,(day-1)*24+i]

        for z in instance.s_nodes:
         #load Solar time series data
            for i in K:
                instance.HorizonSolar[z,i] = instance.SimSolar[z,(day-1)*24+i]

        for z in instance.w_nodes:
         #load Wind time series data
            for i in K:
                instance.HorizonWind[z,i] = instance.SimWind[z,(day-1)*24+i]

        for z in instance.h_imports:
         #load Hydropower time series data
            for i in K:
                instance.HorizonHydroImport[z,i] = instance.SimHydroImport[z,(day-1)*24+i]
        
        for z in instance.Generators:
         #load Deratef time series data 
             for i in K:
                 instance.HorizonDeratef[z,i] = instance.SimDeratef[z,(day-1)*24+i]

        thai_result = opt.solve(instance,tee=True) ##,tee=True
        
        if thai_result.solver.status == SolverStatus.aborted: #max time limit reached 
            thai_result.solver.status = SolverStatus.warning #change status so that results can be loaded
            
        instance.solutions.load_from(thai_result)   

    #  #The following section is for storing and sorting results
        for v in instance.component_objects(Var, active=True):
            varobject = getattr(instance, str(v))
            a=str(v)
            if a=='hydro':

                 for index in varobject:
                     if int(index[1]>0 and index[1]<25):
                        if index[0] in instance.h_nodes:
                            hydro.append((index[0],index[1]+((day-1)*24),varobject[index].value))   

            if a=='solar':

                 for index in varobject:
                     if int(index[1]>0 and index[1]<25):
                        if index[0] in instance.s_nodes:
                            solar.append((index[0],index[1]+((day-1)*24),varobject[index].value))   

            if a=='wind':

                 for index in varobject:
                     if int(index[1]>0 and index[1]<25):
                        if index[0] in instance.w_nodes:
                            wind.append((index[0],index[1]+((day-1)*24),varobject[index].value))   


            if a=='hydro_import':

                 for index in varobject:
                     if int(index[1]>0 and index[1]<25):
                        if index[0] in instance.h_imports:
                            hydro_import.append((index[0],index[1]+((day-1)*24),varobject[index].value))   

            if a=='vlt_angle':

                 for index in varobject:
                     if int(index[1]>0 and index[1]<25):
                        if index[0] in instance.nodes:
                            vlt_angle.append((index[0],index[1]+((day-1)*24),varobject[index].value))   

            if a=='mwh':
                ini_mwh_ = {}
                for index in varobject:
                    if int(index[1]>0 and index[1]<25):
                        mwh.append((index[0],index[1]+((day-1)*24),varobject[index].value))
                    if int(index[1])==24:
                        ini_mwh_[index[0]] = varobject[index].value    

            if a=='on': 
                ini_on_ = {} 
                for index in varobject:
                    if int(index[1]>0 and index[1]<25):
                        on.append((index[0],index[1]+((day-1)*24),varobject[index].value))
                    if int(index[1])==24:
                        ini_on_[index[0]] = varobject[index].value

            if a=='switch':  
                for index in varobject:
                    if int(index[1]>0 and index[1]<25):
                        switch.append((index[0],index[1]+((day-1)*24),varobject[index].value))


            if a=='srsv':    
                for index in varobject:
                    if int(index[1]>0 and index[1]<25):
                        srsv.append((index[0],index[1]+((day-1)*24),varobject[index].value))


            if a=='nrsv':    
                for index in varobject:
                    if int(index[1]>0 and index[1]<25):
                        nrsv.append((index[0],index[1]+((day-1)*24),varobject[index].value))
                        
        # Update initialization values for "on" and "mwh"
        for z in instance.Generators:
            instance.ini_on[z] = round(ini_on_[z])
            instance.ini_mwh[z] = max(round(ini_mwh_[z],2),0)  

        print(day)
        print(str(datetime.now()))


    ###outputs to dataframe
    hydro_pd=pd.DataFrame(hydro,columns=('Node','Time','Value'))
    hydro_import_pd=pd.DataFrame(hydro_import,columns=('Node','Time','Value'))
    solar_pd=pd.DataFrame(solar,columns=('Node','Time','Value'))
    wind_pd=pd.DataFrame(wind,columns=('Node','Time','Value'))

    vlt_angle_pd=pd.DataFrame(vlt_angle,columns=('Node','Time','Value'))

    mwh_pd=pd.DataFrame(mwh,columns=('Generator','Time','Value'))    
    on_pd=pd.DataFrame(on,columns=('Generator','Time','Value'))
    switch_pd=pd.DataFrame(switch,columns=('Generator','Time','Value'))
    srsv_pd=pd.DataFrame(srsv,columns=('Generator','Time','Value'))
    nrsv_pd=pd.DataFrame(nrsv,columns=('Generator','Time','Value'))

    ###Save outputs
    mwh_pd.to_csv('./output/out_thai_v1_'+str(yr)+'_q'+str(q+1)+'_mwh.csv')

    hydro_pd.to_csv('./output/out_thai_v1_'+str(yr)+'_q'+str(q+1)+'_hydro.csv')
    hydro_import_pd.to_csv('./output/out_thai_v1_'+str(yr)+'_q'+str(q+1)+'_hydro_import.csv')
    solar_pd.to_csv('./output/out_thai_v1_'+str(yr)+'_q'+str(q+1)+'_solar.csv')
    wind_pd.to_csv('./output/out_thai_v1_'+str(yr)+'_q'+str(q+1)+'_wind.csv')

    vlt_angle_pd.to_csv('./output/out_thai_v1_'+str(yr)+'_q'+str(q+1)+'_vlt_angle.csv')

    on_pd.to_csv('./output/out_thai_v1_'+str(yr)+'_q'+str(q+1)+'_on.csv')
    switch_pd.to_csv('./output/out_thai_v1_'+str(yr)+'_q'+str(q+1)+'_switch.csv')
    srsv_pd.to_csv('./output/out_thai_v1_'+str(yr)+'_q'+str(q+1)+'_srsv.csv')
    nrsv_pd.to_csv('./output/out_thai_v1_'+str(yr)+'_q'+str(q+1)+'_nrsv.csv')

