from __future__ import division # convert int or long division arguments to floating point values before division
from pyomo.environ import *
from pyomo.opt import SolverFactory

gn_nodes = ['304IPNPPA9','BaanRai','BangchakRefinery','GhecoOne','GulfJPNS','GulfJPUT','HongsaLignite','KaengKhoi2',
            'MitrBiopower','NakhonPathom','NikomMapTaPhut','NongKhai','NorthBangkok','Phetchaburi','PTTOlefins',
            'RatchaburiThermal','Rayong','SrirachaRefinery','UWCKomen'] ##Thermoplant and import nodes without demand

gd_nodes = ['Ayutthaya1','Ayutthaya2','BangKapi','BangkokNoi','BangMunNak','BangPakong','BoWin','BuriRam',
            'ChonBuri','ChonBuri2','Chumphon','Kalasin','Kamphaengphet','Kanchanaburi',
            'Kanchanaburi2','Khanom','KhonKaen1','KhonKaen3','Krabi','Lampang1','Lamphun2','LanKrabu',
            'LopBuri1','MaeHongSon','MaeMoh3','MaeTaeng','Mukdahan','NakhonRatchasima1',
            'NakhonSawan','NakhonSiThammarat','NamPhong2','NongChok','Phon','Phuket1','PrachinBuri1','PrachinBuri2',
            'PrachuapKhiriKhan','Rangsit','Ratchaburi','Ratchaburi3','Rayong1','Rayong2','RoiEt','Sadao',
            'SamutSakhon1','Saraburi1','Saraburi2','Saraburi3','Songkhla','SouthBangkok','SuphanBuri',
            'SuratThani','Surin','UbonRatchathani1','UdonThani1','WangNoi','Yala'] ##Thermoplant and import nodes with demand

g_nodes = gn_nodes + gd_nodes


model = AbstractModel()

## string indentifiers for the set of generators
## gn_nodes
model.Node1Generators =  Set()
model.Node2Generators =  Set()
model.Node3Generators =  Set()
model.Node4Generators =  Set()
model.Node5Generators =  Set()
model.Node6Generators =  Set()
model.Node7Generators =  Set()
model.Node8Generators =  Set()
model.Node9Generators =  Set()
model.Node10Generators =  Set()

model.Node11Generators =  Set()
model.Node12Generators =  Set()
model.Node13Generators =  Set()
model.Node14Generators =  Set()
model.Node15Generators =  Set()
model.Node16Generators =  Set()
model.Node17Generators =  Set()
model.Node18Generators =  Set()

## gd_nodes
model.Node19Generators =  Set()
model.Node20Generators =  Set()
model.Node21Generators =  Set()
model.Node22Generators =  Set()
model.Node23Generators =  Set()
model.Node24Generators =  Set()

model.Node25Generators =  Set()
model.Node26Generators =  Set()
model.Node27Generators =  Set()
model.Node28Generators =  Set()
model.Node29Generators =  Set()
model.Node30Generators =  Set()

model.Node31Generators =  Set()
model.Node32Generators =  Set()
model.Node33Generators =  Set()
model.Node34Generators =  Set()
model.Node35Generators =  Set()
model.Node36Generators =  Set()
model.Node37Generators =  Set()
model.Node38Generators =  Set()
model.Node39Generators =  Set()
model.Node40Generators =  Set()

model.Node41Generators =  Set()
model.Node42Generators =  Set()
model.Node43Generators =  Set()
model.Node44Generators =  Set()
model.Node45Generators =  Set()
model.Node46Generators =  Set()
model.Node47Generators =  Set()
model.Node48Generators =  Set()
model.Node49Generators =  Set()
model.Node50Generators =  Set()

model.Node51Generators =  Set()
model.Node52Generators =  Set()
model.Node53Generators =  Set()
model.Node54Generators =  Set()
model.Node55Generators =  Set()
model.Node56Generators =  Set()
model.Node57Generators =  Set()
model.Node58Generators =  Set()
model.Node59Generators =  Set()
model.Node60Generators =  Set()

model.Node61Generators =  Set()
model.Node62Generators =  Set()
model.Node63Generators =  Set()
model.Node64Generators =  Set()
model.Node65Generators =  Set()
model.Node66Generators =  Set()
model.Node67Generators =  Set()
model.Node68Generators =  Set()
model.Node69Generators =  Set()
model.Node70Generators =  Set()

model.Node71Generators =  Set()
model.Node72Generators =  Set()
model.Node73Generators =  Set()
model.Node74Generators =  Set()
model.Node75Generators =  Set()
model.Node76Generators =  Set()


model.Generators = model.Node1Generators | model.Node2Generators | model.Node3Generators | model.Node4Generators | \
                   model.Node5Generators | model.Node6Generators | model.Node7Generators | model.Node8Generators | \
                   model.Node9Generators | model.Node10Generators | model.Node11Generators | model.Node12Generators | \
                   model.Node13Generators | model.Node14Generators | model.Node15Generators | model.Node16Generators | \
                   model.Node17Generators | model.Node18Generators | model.Node19Generators | model.Node20Generators | \
                   model.Node21Generators | model.Node22Generators | model.Node23Generators | model.Node24Generators | \
                   model.Node25Generators | model.Node26Generators | model.Node27Generators | model.Node28Generators | \
                   model.Node29Generators | model.Node30Generators |\
                   model.Node31Generators | model.Node32Generators | model.Node33Generators | model.Node34Generators | \
                   model.Node35Generators | model.Node36Generators | model.Node37Generators | model.Node38Generators | \
                   model.Node39Generators | model.Node40Generators |\
                   model.Node41Generators | model.Node42Generators | model.Node43Generators | model.Node44Generators | \
                   model.Node45Generators | model.Node46Generators | model.Node47Generators | model.Node48Generators | \
                   model.Node49Generators | model.Node50Generators | \
                   model.Node51Generators | model.Node52Generators | model.Node53Generators | model.Node54Generators | \
                   model.Node55Generators | model.Node56Generators | model.Node57Generators | model.Node58Generators | \
                   model.Node59Generators | model.Node60Generators | \
                   model.Node61Generators | model.Node62Generators | model.Node63Generators | model.Node64Generators | \
                   model.Node65Generators | model.Node66Generators | model.Node67Generators | model.Node68Generators | \
                   model.Node69Generators | model.Node70Generators | \
                   model.Node71Generators | model.Node72Generators | model.Node73Generators | model.Node74Generators | \
                   model.Node75Generators | model.Node76Generators

### Generators by Fuel Type
model.Biomass_st = Set()
model.Coal_st = Set()
model.Coal_imp = Set()
model.Gas_cc = Set()
model.Gas_st = Set()
model.Gas_gt = Set()
model.Gas_ic = Set()
model.Oil_gt = Set()
model.Oil_ic = Set()
model.Oil_st = Set()
model.Wsth_st = Set()

model.Slack = Set()


###Allocate generators that will ensure minimum reserves
model.ResGenerators = model.Gas_cc | model.Gas_ic | model.Gas_gt | model.Oil_gt | model.Oil_ic


### Nodal Matrix
model.nodes = Set()
model.sources = Set(within=model.nodes)
model.sinks = Set(within=model.nodes)

##model.g_nodes = Set()
model.h_nodes = Set()
model.h_imports = Set()
model.s_nodes = Set()
model.w_nodes = Set()
model.d_nodes = Set()

model.gd_nodes = Set()
model.gn_nodes = Set()
model.td_nodes = Set()
model.tn_nodes = Set()

#####==== generators parameters from model input ===####

#Generator Type
model.typ = Param(model.Generators)

#State parameters
model.node = Param(model.Generators)

#Max Generating Capacity
model.maxcap = Param(model.Generators)

#Min Generating Capacity
model.mincap = Param(model.Generators)

#cost function
model.heat_rate = Param(model.Generators)

#Variable O&M
model.var_om = Param(model.Generators)

#Fixed O&M cost
model.fix_om  = Param(model.Generators)

#Start cost
model.st_cost = Param(model.Generators)

#Ramp rate
model.ramp  = Param(model.Generators)

#Minimun up time
model.minup = Param(model.Generators)

#Minmun down time
model.mindn = Param(model.Generators)

#Derate Factor to Max Generating Capacity
model.deratef = Param(model.Generators,within=NonNegativeReals)

#Transmission Path parameters
model.linemva = Param(model.sources, model.sinks)
model.linesus = Param(model.sources, model.sinks)


### parameters for model runs  
## Full range of time series information provided in .dat file (1 year)
model.SimHours = Param(within=PositiveIntegers)
model.SH_periods = RangeSet(1,model.SimHours+1)
model.SimDays = Param(within=PositiveIntegers)
model.SD_periods = RangeSet(1,model.SimDays+1)

### Transmission Loss as a % of production
model.TransLoss = Param(within=NonNegativeReals)

### Maximum line-usage as a percent of line-capacity
model.n1criterion = Param(within=NonNegativeReals)

### Minimum spinning reserve as a percent of total reserve
model.spin_margin = Param(within=NonNegativeReals)

# Operating horizon information 
model.HorizonHours = Param(within=PositiveIntegers)
model.HH_periods = RangeSet(0,model.HorizonHours)
model.hh_periods = RangeSet(1,model.HorizonHours)
model.ramp_periods = RangeSet(2,24)

#Demand over simulation period
model.SimDemand = Param(model.d_nodes*model.SH_periods, within=NonNegativeReals)
#Horizon demand
model.HorizonDemand = Param(model.d_nodes*model.hh_periods,within=NonNegativeReals,mutable=True)

#Reserve for the entire system
model.SimReserves = Param(model.SH_periods, within=NonNegativeReals)
model.HorizonReserves = Param(model.hh_periods, within=NonNegativeReals,mutable=True)

##Variable resources over simulation period
model.SimHydro = Param(model.h_nodes, model.SH_periods, within=NonNegativeReals)
model.SimSolar = Param(model.s_nodes, model.SH_periods, within=NonNegativeReals)
model.SimWind = Param(model.w_nodes, model.SH_periods, within=NonNegativeReals)

#Variable resources over horizon
model.HorizonHydro = Param(model.h_nodes,model.hh_periods,within=NonNegativeReals,mutable=True)
model.HorizonSolar = Param(model.s_nodes,model.hh_periods,within=NonNegativeReals,mutable=True)
model.HorizonWind = Param(model.w_nodes,model.hh_periods,within=NonNegativeReals,mutable=True)

##Hydro import over simulation period
model.SimHydroImport = Param(model.h_imports, model.SH_periods, within=NonNegativeReals)
#Hydro import over horizon
model.HorizonHydroImport = Param(model.h_imports,model.hh_periods,within=NonNegativeReals,mutable=True)

##Initial conditions
model.ini_on = Param(model.Generators, within=Binary, initialize=0,mutable=True) 
model.ini_mwh = Param(model.Generators,initialize=0,mutable=True)


#####============= Decision variables ===============########
##Amount of day-ahead energy generated by each generator at each hour
model.mwh = Var(model.Generators,model.HH_periods, within=NonNegativeReals,initialize=0)

#1 if unit is on in hour i
model.on = Var(model.Generators,model.HH_periods, within=Binary, initialize=0)

#1 if unit is switching on in hour i
model.switch = Var(model.Generators,model.HH_periods, within=Binary,initialize=0)

#Amount of spining reserce offered by each unit in each hour
model.srsv = Var(model.Generators,model.HH_periods, within=NonNegativeReals,initialize=0)

#Amount of non-sping reserve ovvered by each unit in each hour
model.nrsv = Var(model.Generators,model.HH_periods, within=NonNegativeReals,initialize=0)

#Hydropower production
model.hydro = Var(model.h_nodes,model.HH_periods,within=NonNegativeReals)

#Solar production
model.solar = Var(model.s_nodes,model.HH_periods,within=NonNegativeReals)

#wind production
model.wind = Var(model.w_nodes,model.HH_periods,within=NonNegativeReals)

#Hydropower import
model.hydro_import = Var(model.h_imports,model.HH_periods,within=NonNegativeReals)

#Voltage angles at line
model.vlt_angle = Var(model.nodes,model.HH_periods)


####========= Objective function ==================###

def SysCost(model):
    fixed = sum(model.maxcap[j]*model.fix_om[j]*model.on[j,i] for i in model.hh_periods for j in model.Generators)
    starts = sum(model.maxcap[j]*model.st_cost[j]*model.switch[j,i] for i in model.hh_periods for j in model.Generators)

    coal_st = sum(model.mwh[j,i]*(model.heat_rate[j]*5.0 + model.var_om[j]) for i in model.hh_periods for j in model.Coal_st)  
    coal_imp = sum(model.mwh[j,i]*(model.heat_rate[j]*5.25 + model.var_om[j]) for i in model.hh_periods for j in model.Coal_imp)  
    biomass_st = sum(model.mwh[j,i]*(model.heat_rate[j]*3.02 + model.var_om[j]) for i in model.hh_periods for j in model.Biomass_st)

    gas_cc = sum(model.mwh[j,i]*(model.heat_rate[j]*5.85 + model.var_om[j]) for i in model.hh_periods for j in model.Gas_cc)
    gas_st = sum(model.mwh[j,i]*(model.heat_rate[j]*5.85 + model.var_om[j]) for i in model.hh_periods for j in model.Gas_st)
    gas_gt = sum(model.mwh[j,i]*(model.heat_rate[j]*5.85 + model.var_om[j]) for i in model.hh_periods for j in model.Gas_gt)
    gas_ic = sum(model.mwh[j,i]*(model.heat_rate[j]*5.85 + model.var_om[j]) for i in model.hh_periods for j in model.Gas_ic)

    oil_gt = sum(model.mwh[j,i]*(model.heat_rate[j]*8.0 + model.var_om[j]) for i in model.hh_periods for j in model.Oil_gt)
    oil_ic = sum(model.mwh[j,i]*(model.heat_rate[j]*8.0 + model.var_om[j]) for i in model.hh_periods for j in model.Oil_ic)
    oil_st = sum(model.mwh[j,i]*(model.heat_rate[j]*8.0 + model.var_om[j]) for i in model.hh_periods for j in model.Oil_st)

    wsth_st = sum(model.mwh[j,i]*(model.heat_rate[j]*3.02 + model.var_om[j]) for i in model.hh_periods for j in model.Wsth_st)  

    import_hydro = sum(model.hydro_import[j,i]*40 for i in model.hh_periods for j in model.h_imports) 
    
    slack = sum(model.mwh[j,i]*model.heat_rate[j]*1000 for i in model.hh_periods for j in model.Slack)
    
    return fixed +starts +coal_st +biomass_st +gas_cc +gas_st +gas_gt +gas_ic +oil_gt +oil_ic +oil_st +wsth_st +slack +import_hydro+coal_imp

model.SystemCost = Objective(rule=SysCost, sense=minimize)


####=== Reference Node =====#####
def ref_node(model,i):
    return model.vlt_angle['NongChok',i] == 0 ##NongChok=max_load node
model.Ref_NodeConstraint= Constraint(model.hh_periods,rule= ref_node)

######=== Power Balance =====########
################=========Hydropower Plants=============################
def HPnodes_Balance(model,z,i):
    dis_hydro = model.hydro[z,i]
    #demand = model.HorizonDemand[z,i]
    impedance = sum(model.linesus[z,k] * (model.vlt_angle[z,i] - model.vlt_angle[k,i]) for k in model.sinks)
    return (1 - model.TransLoss) * dis_hydro == impedance ##- demand
model.HPnodes_BalConstraint= Constraint(model.h_nodes,model.hh_periods,rule= HPnodes_Balance)

################=========Hydropower Imports=============################
def HP_Imports_Balance(model,z,i):
    hp_import = model.hydro_import[z,i]
    #demand = model.HorizonDemand[z,i]
    impedance = sum(model.linesus[z,k] * (model.vlt_angle[z,i] - model.vlt_angle[k,i]) for k in model.sinks)
    return (1 - model.TransLoss) * hp_import == impedance ##- demand
model.HP_Imports_BalConstraint= Constraint(model.h_imports,model.hh_periods,rule= HP_Imports_Balance)

################=========Solar Plants=============################
def Solarnodes_Balance(model,z,i):
    dis_solar = model.solar[z,i]
    impedance = sum(model.linesus[z,k] * (model.vlt_angle[z,i] - model.vlt_angle[k,i]) for k in model.sinks)
    return (1 - model.TransLoss) * dis_solar == impedance ##- demand
model.Solarnodes_BalConstraint= Constraint(model.s_nodes,model.hh_periods,rule= Solarnodes_Balance)

##############=========Wind Plants=============################
def Windnodes_Balance(model,z,i):
    dis_wind = model.wind[z,i]
    impedance = sum(model.linesus[z,k] * (model.vlt_angle[z,i] - model.vlt_angle[k,i]) for k in model.sinks)
    return (1 - model.TransLoss) * dis_wind == impedance ##- demand
model.Windnodes_BalConstraint= Constraint(model.w_nodes,model.hh_periods,rule= Windnodes_Balance)


#########======= Transformers with demand Nodes =========#######
def TDnodes_Balance(model,z,i):
    demand = model.HorizonDemand[z,i]
    impedance = sum(model.linesus[z,k] * (model.vlt_angle[z,i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return - demand == impedance
model.TDnodes_BalConstraint= Constraint(model.td_nodes,model.hh_periods,rule= TDnodes_Balance)

#########======= Transformers without demand Nodes =========#######
def TNnodes_Balance(model,z,i):
    #demand = model.HorizonDemand[z,i]
    impedance = sum(model.linesus[z,k] * (model.vlt_angle[z,i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return 0 == impedance
model.TNnodes_BalConstraint= Constraint(model.tn_nodes,model.hh_periods,rule= TNnodes_Balance)


##########============ Thermoplants and Import Nodes without Demand ==============############
def Node1_Balance(model,i):
    gg = 1
    thermo = sum(model.mwh[j,i] for j in model.Node1Generators)    
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo == impedance #- demand
model.Node1_BalConstraint= Constraint(model.hh_periods,rule= Node1_Balance)

def Node2_Balance(model,i):
    gg = 2
    thermo = sum(model.mwh[j,i] for j in model.Node2Generators)    
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo == impedance #- demand
model.Node2_BalConstraint= Constraint(model.hh_periods,rule= Node2_Balance)

def Node3_Balance(model,i):
    gg = 3
    thermo = sum(model.mwh[j,i] for j in model.Node3Generators)    
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo == impedance #- demand
model.Node3_BalConstraint= Constraint(model.hh_periods,rule= Node3_Balance)

def Node4_Balance(model,i):
    gg = 4
    thermo = sum(model.mwh[j,i] for j in model.Node4Generators)    
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo == impedance #- demand
model.Node4_BalConstraint= Constraint(model.hh_periods,rule= Node4_Balance)

def Node5_Balance(model,i):
    gg = 5
    thermo = sum(model.mwh[j,i] for j in model.Node5Generators)    
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo == impedance #- demand
model.Node5_BalConstraint= Constraint(model.hh_periods,rule= Node5_Balance)

def Node6_Balance(model,i): ##HongsaLignite
    gg = 6
    thermo = sum(model.mwh[j,i] for j in model.Node6Generators)    
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo == impedance #10% gen to Laos_domestic grid
model.Node6_BalConstraint= Constraint(model.hh_periods,rule= Node6_Balance)

def Node7_Balance(model,i):
    gg = 7
    thermo = sum(model.mwh[j,i] for j in model.Node7Generators)    
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo == impedance #- demand
model.Node7_BalConstraint= Constraint(model.hh_periods,rule= Node7_Balance)

def Node8_Balance(model,i):
    gg = 8
    thermo = sum(model.mwh[j,i] for j in model.Node8Generators)    
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo == impedance #- demand
model.Node8_BalConstraint= Constraint(model.hh_periods,rule= Node8_Balance)

def Node9_Balance(model,i):
    gg = 9
    thermo = sum(model.mwh[j,i] for j in model.Node9Generators)    
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo == impedance #- demand
model.Node9_BalConstraint= Constraint(model.hh_periods,rule= Node9_Balance)

def Node10_Balance(model,i):
    gg = 10
    thermo = sum(model.mwh[j,i] for j in model.Node10Generators)    
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo == impedance #- demand
model.Node10_BalConstraint= Constraint(model.hh_periods,rule= Node10_Balance)

def Node11_Balance(model,i):
    gg = 11
    thermo = sum(model.mwh[j,i] for j in model.Node11Generators)    
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo == impedance #- demand
model.Node11_BalConstraint= Constraint(model.hh_periods,rule= Node11_Balance)

def Node12_Balance(model,i):
    gg = 12
    thermo = sum(model.mwh[j,i] for j in model.Node12Generators)    
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo == impedance #- demand
model.Node12_BalConstraint= Constraint(model.hh_periods,rule= Node12_Balance)

def Node13_Balance(model,i):
    gg = 13
    thermo = sum(model.mwh[j,i] for j in model.Node13Generators)    
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo == impedance #- demand
model.Node13_BalConstraint= Constraint(model.hh_periods,rule= Node13_Balance)

def Node14_Balance(model,i):
    gg = 14
    thermo = sum(model.mwh[j,i] for j in model.Node14Generators)    
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo == impedance #- demand
model.Node14_BalConstraint= Constraint(model.hh_periods,rule= Node14_Balance)

def Node15_Balance(model,i):
    gg = 15
    thermo = sum(model.mwh[j,i] for j in model.Node15Generators)    
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo == impedance #- demand
model.Node15_BalConstraint= Constraint(model.hh_periods,rule= Node15_Balance)

def Node16_Balance(model,i):
    gg = 16
    thermo = sum(model.mwh[j,i] for j in model.Node16Generators)    
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo == impedance #- demand
model.Node16_BalConstraint= Constraint(model.hh_periods,rule= Node16_Balance)

def Node17_Balance(model,i):
    gg = 17
    thermo = sum(model.mwh[j,i] for j in model.Node17Generators)    
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo == impedance #- demand
model.Node17_BalConstraint= Constraint(model.hh_periods,rule= Node17_Balance)

def Node18_Balance(model,i):
    gg = 18
    thermo = sum(model.mwh[j,i] for j in model.Node18Generators)    
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo == impedance #- demand
model.Node18_BalConstraint= Constraint(model.hh_periods,rule= Node18_Balance)

def Node19_Balance(model,i):
    gg = 19
    thermo = sum(model.mwh[j,i] for j in model.Node19Generators)    
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo == impedance
model.Node19_BalConstraint= Constraint(model.hh_periods,rule= Node19_Balance)


##########============ Thermoplants and Import Nodes with Demand ==============############
def Node20_Balance(model,i):
    gg = 20
    thermo = sum(model.mwh[j,i] for j in model.Node20Generators)    
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node20_BalConstraint= Constraint(model.hh_periods,rule= Node20_Balance)

def Node21_Balance(model,i):
    gg = 21
    thermo = sum(model.mwh[j,i] for j in model.Node21Generators)    
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node21_BalConstraint= Constraint(model.hh_periods,rule= Node21_Balance)

def Node22_Balance(model,i):
    gg = 22
    thermo = sum(model.mwh[j,i] for j in model.Node22Generators)    
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node22_BalConstraint= Constraint(model.hh_periods,rule= Node22_Balance)

def Node23_Balance(model,i):
    gg = 23
    thermo = sum(model.mwh[j,i] for j in model.Node23Generators)    
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node23_BalConstraint= Constraint(model.hh_periods,rule= Node23_Balance)

def Node24_Balance(model,i):
    gg = 24
    thermo = sum(model.mwh[j,i] for j in model.Node24Generators)    
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node24_BalConstraint= Constraint(model.hh_periods,rule= Node24_Balance)

def Node25_Balance(model,i):
    gg = 25
    thermo = sum(model.mwh[j,i] for j in model.Node25Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node25_BalConstraint= Constraint(model.hh_periods,rule= Node25_Balance)

def Node26_Balance(model,i):
    gg = 26
    thermo = sum(model.mwh[j,i] for j in model.Node26Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node26_BalConstraint= Constraint(model.hh_periods,rule= Node26_Balance)

def Node27_Balance(model,i):
    gg = 27
    thermo = sum(model.mwh[j,i] for j in model.Node27Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node27_BalConstraint= Constraint(model.hh_periods,rule= Node27_Balance)

def Node28_Balance(model,i):
    gg = 28
    thermo = sum(model.mwh[j,i] for j in model.Node28Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node28_BalConstraint= Constraint(model.hh_periods,rule= Node28_Balance)

def Node29_Balance(model,i):
    gg = 29
    thermo = sum(model.mwh[j,i] for j in model.Node29Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node29_BalConstraint= Constraint(model.hh_periods,rule= Node29_Balance)

def Node30_Balance(model,i):
    gg = 30
    thermo = sum(model.mwh[j,i] for j in model.Node30Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node30_BalConstraint= Constraint(model.hh_periods,rule= Node30_Balance)

def Node31_Balance(model,i):
    gg = 31
    thermo = sum(model.mwh[j,i] for j in model.Node31Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node31_BalConstraint= Constraint(model.hh_periods,rule= Node31_Balance)

def Node32_Balance(model,i):
    gg = 32
    thermo = sum(model.mwh[j,i] for j in model.Node32Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node32_BalConstraint= Constraint(model.hh_periods,rule= Node32_Balance)

def Node33_Balance(model,i):
    gg = 33
    thermo = sum(model.mwh[j,i] for j in model.Node33Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node33_BalConstraint= Constraint(model.hh_periods,rule= Node33_Balance)

def Node34_Balance(model,i):
    gg = 34
    thermo = sum(model.mwh[j,i] for j in model.Node34Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node34_BalConstraint= Constraint(model.hh_periods,rule= Node34_Balance)

def Node35_Balance(model,i):
    gg = 35
    thermo = sum(model.mwh[j,i] for j in model.Node35Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node35_BalConstraint= Constraint(model.hh_periods,rule= Node35_Balance)

def Node36_Balance(model,i):
    gg = 36
    thermo = sum(model.mwh[j,i] for j in model.Node36Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node36_BalConstraint= Constraint(model.hh_periods,rule= Node36_Balance)

def Node37_Balance(model,i):
    gg = 37
    thermo = sum(model.mwh[j,i] for j in model.Node37Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node37_BalConstraint= Constraint(model.hh_periods,rule= Node37_Balance)

def Node38_Balance(model,i):
    gg = 38
    thermo = sum(model.mwh[j,i] for j in model.Node38Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node38_BalConstraint= Constraint(model.hh_periods,rule= Node38_Balance)

def Node39_Balance(model,i):
    gg = 39
    thermo = sum(model.mwh[j,i] for j in model.Node39Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node39_BalConstraint= Constraint(model.hh_periods,rule= Node39_Balance)

def Node40_Balance(model,i):
    gg = 40
    thermo = sum(model.mwh[j,i] for j in model.Node40Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node40_BalConstraint= Constraint(model.hh_periods,rule= Node40_Balance)

def Node41_Balance(model,i):
    gg = 41
    thermo = sum(model.mwh[j,i] for j in model.Node41Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node41_BalConstraint= Constraint(model.hh_periods,rule= Node41_Balance)

def Node42_Balance(model,i):
    gg = 42
    thermo = sum(model.mwh[j,i] for j in model.Node42Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node42_BalConstraint= Constraint(model.hh_periods,rule= Node42_Balance)

def Node43_Balance(model,i):
    gg = 43
    thermo = sum(model.mwh[j,i] for j in model.Node43Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node43_BalConstraint= Constraint(model.hh_periods,rule= Node43_Balance)

def Node44_Balance(model,i):
    gg = 44
    thermo = sum(model.mwh[j,i] for j in model.Node44Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node44_BalConstraint= Constraint(model.hh_periods,rule= Node44_Balance)

def Node45_Balance(model,i):
    gg = 45
    thermo = sum(model.mwh[j,i] for j in model.Node45Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node45_BalConstraint= Constraint(model.hh_periods,rule= Node45_Balance)

def Node46_Balance(model,i):
    gg = 46
    thermo = sum(model.mwh[j,i] for j in model.Node46Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node46_BalConstraint= Constraint(model.hh_periods,rule= Node46_Balance)

def Node47_Balance(model,i):
    gg = 47
    thermo = sum(model.mwh[j,i] for j in model.Node47Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node47_BalConstraint= Constraint(model.hh_periods,rule= Node47_Balance)

def Node48_Balance(model,i):
    gg = 48
    thermo = sum(model.mwh[j,i] for j in model.Node48Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node48_BalConstraint= Constraint(model.hh_periods,rule= Node48_Balance)

def Node49_Balance(model,i):
    gg = 49
    thermo = sum(model.mwh[j,i] for j in model.Node49Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node49_BalConstraint= Constraint(model.hh_periods,rule= Node49_Balance)

def Node50_Balance(model,i):
    gg = 50
    thermo = sum(model.mwh[j,i] for j in model.Node50Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node50_BalConstraint= Constraint(model.hh_periods,rule= Node50_Balance)

def Node51_Balance(model,i):
    gg = 51
    thermo = sum(model.mwh[j,i] for j in model.Node51Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node51_BalConstraint= Constraint(model.hh_periods,rule= Node51_Balance)

def Node52_Balance(model,i): ##Include wind
    gg = 52
    thermo = sum(model.mwh[j,i] for j in model.Node52Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node52_BalConstraint= Constraint(model.hh_periods,rule= Node52_Balance)

def Node53_Balance(model,i):
    gg = 53
    thermo = sum(model.mwh[j,i] for j in model.Node53Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node53_BalConstraint= Constraint(model.hh_periods,rule= Node53_Balance)

def Node54_Balance(model,i):
    gg = 54
    thermo = sum(model.mwh[j,i] for j in model.Node54Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node54_BalConstraint= Constraint(model.hh_periods,rule= Node54_Balance)

def Node55_Balance(model,i):
    gg = 55
    thermo = sum(model.mwh[j,i] for j in model.Node55Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node55_BalConstraint= Constraint(model.hh_periods,rule= Node55_Balance)

def Node56_Balance(model,i):
    gg = 56
    thermo = sum(model.mwh[j,i] for j in model.Node56Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node56_BalConstraint= Constraint(model.hh_periods,rule= Node56_Balance)

def Node57_Balance(model,i):
    gg = 57
    thermo = sum(model.mwh[j,i] for j in model.Node57Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node57_BalConstraint= Constraint(model.hh_periods,rule= Node57_Balance)

def Node58_Balance(model,i):
    gg = 58
    thermo = sum(model.mwh[j,i] for j in model.Node58Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node58_BalConstraint= Constraint(model.hh_periods,rule= Node58_Balance)

def Node59_Balance(model,i):
    gg = 59
    thermo = sum(model.mwh[j,i] for j in model.Node59Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node59_BalConstraint= Constraint(model.hh_periods,rule= Node59_Balance)

def Node60_Balance(model,i):
    gg = 60
    thermo = sum(model.mwh[j,i] for j in model.Node60Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node60_BalConstraint= Constraint(model.hh_periods,rule= Node60_Balance)

def Node61_Balance(model,i):
    gg = 61
    thermo = sum(model.mwh[j,i] for j in model.Node61Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node61_BalConstraint= Constraint(model.hh_periods,rule= Node61_Balance)

def Node62_Balance(model,i):
    gg = 62
    thermo = sum(model.mwh[j,i] for j in model.Node62Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node62_BalConstraint= Constraint(model.hh_periods,rule= Node62_Balance)

def Node63_Balance(model,i):
    gg = 63
    thermo = sum(model.mwh[j,i] for j in model.Node63Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node63_BalConstraint= Constraint(model.hh_periods,rule= Node63_Balance)

def Node64_Balance(model,i):
    gg = 64
    thermo = sum(model.mwh[j,i] for j in model.Node64Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node64_BalConstraint= Constraint(model.hh_periods,rule= Node64_Balance)

def Node65_Balance(model,i):
    gg = 65
    thermo = sum(model.mwh[j,i] for j in model.Node65Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node65_BalConstraint= Constraint(model.hh_periods,rule= Node65_Balance)

def Node66_Balance(model,i):
    gg = 66
    thermo = sum(model.mwh[j,i] for j in model.Node66Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node66_BalConstraint= Constraint(model.hh_periods,rule= Node66_Balance)

def Node67_Balance(model,i):
    gg = 67
    thermo = sum(model.mwh[j,i] for j in model.Node67Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node67_BalConstraint= Constraint(model.hh_periods,rule= Node67_Balance)

def Node68_Balance(model,i):
    gg = 68
    thermo = sum(model.mwh[j,i] for j in model.Node68Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node68_BalConstraint= Constraint(model.hh_periods,rule= Node68_Balance)

def Node69_Balance(model,i):
    gg = 69
    thermo = sum(model.mwh[j,i] for j in model.Node69Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node69_BalConstraint= Constraint(model.hh_periods,rule= Node69_Balance)

def Node70_Balance(model,i):
    gg = 70
    thermo = sum(model.mwh[j,i] for j in model.Node70Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node70_BalConstraint= Constraint(model.hh_periods,rule= Node70_Balance)

def Node71_Balance(model,i):
    gg = 71
    thermo = sum(model.mwh[j,i] for j in model.Node71Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node71_BalConstraint= Constraint(model.hh_periods,rule= Node71_Balance)

def Node72_Balance(model,i):
    gg = 72
    thermo = sum(model.mwh[j,i] for j in model.Node72Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node72_BalConstraint= Constraint(model.hh_periods,rule= Node72_Balance)

def Node73_Balance(model,i):
    gg = 73
    thermo = sum(model.mwh[j,i] for j in model.Node73Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node73_BalConstraint= Constraint(model.hh_periods,rule= Node73_Balance)

def Node74_Balance(model,i):
    gg = 74
    thermo = sum(model.mwh[j,i] for j in model.Node74Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node74_BalConstraint= Constraint(model.hh_periods,rule= Node74_Balance)

def Node75_Balance(model,i):
    gg = 75
    thermo = sum(model.mwh[j,i] for j in model.Node75Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node75_BalConstraint= Constraint(model.hh_periods,rule= Node75_Balance)

def Node76_Balance(model,i):
    gg = 76
    thermo = sum(model.mwh[j,i] for j in model.Node76Generators)
    demand = model.HorizonDemand[g_nodes[gg-1],i]
    impedance = sum(model.linesus[g_nodes[gg-1],k] * (model.vlt_angle[g_nodes[gg-1],i] - model.vlt_angle[k,i]) for k in model.sinks)   
    return (1 - model.TransLoss) * thermo - demand == impedance
model.Node76_BalConstraint= Constraint(model.hh_periods,rule= Node76_Balance)


###========= Constraints ============####
#Constraints for Max & Min Capacity of Thermoplants and Imports
def MaxC(model,j,i):
    return model.mwh[j,i]  <= model.on[j,i] * model.maxcap[j] *model.deratef[j]
model.MaxCap= Constraint(model.Generators,model.hh_periods,rule=MaxC)

def MinC(model,j,i):
    return model.mwh[j,i] >= model.on[j,i] * model.mincap[j]
model.MinCap= Constraint(model.Generators,model.hh_periods,rule=MinC)

#Max capacity constraints on hydropower 
def HydroC(model,z,i):
    return model.hydro[z,i] <= model.HorizonHydro[z,i]  
model.HydroConstraint= Constraint(model.h_nodes,model.hh_periods,rule=HydroC)

#Max capacity constraints on solar 
def SolarC(model,z,i):
    return model.solar[z,i] <= model.HorizonSolar[z,i]  
model.SolarConstraint= Constraint(model.s_nodes,model.hh_periods,rule=SolarC)

#Max capacity constraints on wind
def WindC(model,z,i):
    return model.wind[z,i] <= model.HorizonWind[z,i]  
model.WindConstraint= Constraint(model.w_nodes,model.hh_periods,rule=WindC)

#Max capacity constraints on hydropower import
def HydroImportC(model,z,i):
    return model.hydro_import[z,i] <= model.HorizonHydroImport[z,i]  
model.HydroImportConstraint= Constraint(model.h_imports,model.hh_periods,rule=HydroImportC)


######========== Transmission Line Constraints =========#############
def MaxLine(model,s,k,i):
    if model.linemva[s,k] > 0:
        return (model.n1criterion) * model.linemva[s,k] >= model.linesus[s,k] * (model.vlt_angle[s,i] - model.vlt_angle[k,i])
    else:
        return Constraint.Skip
model.MaxLineConstraint= Constraint(model.sources,model.sinks,model.hh_periods,rule=MaxLine)

def MinLine(model,s,k,i):
    if model.linemva[s,k] > 0:
        return (-model.n1criterion) * model.linemva[s,k] <= model.linesus[s,k] * (model.vlt_angle[s,i] - model.vlt_angle[k,i])
    else:
        return Constraint.Skip
model.MinLineConstraint= Constraint(model.sources,model.sinks,model.hh_periods,rule=MinLine)


####========== Reserve Constraint =========#############
##System Reserve Requirement
def SysReserve(model,i):
    return sum(model.srsv[j,i] for j in model.ResGenerators) + sum(model.nrsv[j,i] for j in model.ResGenerators) >= model.HorizonReserves[i]
model.SystemReserve = Constraint(model.hh_periods,rule=SysReserve)

##Spinning Reserve Requirement
def SpinningReq(model,i):
    return sum(model.srsv[j,i] for j in model.ResGenerators) >= model.spin_margin * model.HorizonReserves[i] 
model.SpinReq = Constraint(model.hh_periods,rule=SpinningReq)           

##Spinning reserve can only be offered by units that are online
def SpinningReq2(model,j,i):
    return model.srsv[j,i] <= model.on[j,i]*model.maxcap[j] *model.deratef[j]
model.SpinReq2= Constraint(model.Generators,model.hh_periods,rule=SpinningReq2) 

##Non-Spinning reserve can only be offered by units that are offline
def NonSpinningReq(model,j,i):
    return model.nrsv[j,i] <= (1 - model.on[j,i])*model.maxcap[j] *model.deratef[j]
model.NonSpinReq= Constraint(model.Generators,model.hh_periods,rule=NonSpinningReq)


######========== Zero Sum Constraint =========#############
def ZeroSum(model,j,i):
    return model.mwh[j,i] + model.srsv[j,i] + model.nrsv[j,i] <= model.maxcap[j] *model.deratef[j]
model.ZeroSumConstraint=Constraint(model.Generators,model.hh_periods,rule=ZeroSum)

######========== Logical Constraint =========#############
##Switch is 1 if unit is turned on in current period
def SwitchCon(model,j,i):
    return model.switch[j,i] >= 1 - model.on[j,i-1] - (1 - model.on[j,i])
model.SwitchConstraint = Constraint(model.Generators,model.hh_periods,rule = SwitchCon)


######========== Up/Down Time Constraint =========#############
##Min Up time
def MinUp(model,j,i,k):
    if i > 0 and k > i and k < min(i+model.minup[j]-1,model.HorizonHours):
        return model.on[j,i] - model.on[j,i-1] <= model.on[j,k]
    else: 
        return Constraint.Skip
model.MinimumUp = Constraint(model.Generators,model.HH_periods,model.HH_periods,rule=MinUp)

##Min Down time
def MinDown(model,j,i,k):
   if i > 0 and k > i and k < min(i+model.mindn[j]-1,model.HorizonHours):
       return model.on[j,i-1] - model.on[j,i] <= 1 - model.on[j,k]
   else:
       return Constraint.Skip
model.MinimumDown = Constraint(model.Generators,model.HH_periods,model.HH_periods,rule=MinDown)


######==========Ramp Rate Constraints =========#############
def Ramp1(model,j,i):
    a = model.mwh[j,i]
    b = model.mwh[j,i-1]
    return a - b <= model.ramp[j] 
model.RampCon1 = Constraint(model.Generators,model.ramp_periods,rule=Ramp1)

def Ramp2(model,j,i):
    a = model.mwh[j,i]
    b = model.mwh[j,i-1]
    return b - a <= model.ramp[j] 
model.RampCon2 = Constraint(model.Generators,model.ramp_periods,rule=Ramp2)
