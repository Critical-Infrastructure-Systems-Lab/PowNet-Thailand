import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##simulation year (varies for climate-dependent inputs)
yr = 2016 


##for the current setup, rest of code can remain unchanged
SimDays = 365
SimHours = SimDays * 24
HorizonHours = 24  ##planning horizon (e.g., 24, 48, 72 hours etc.)
TransLoss = 0.075  ##transmission loss as a percent of generation
n1criterion = 0.75 ##maximum line-usage as a percent of line-capacity
res_margin = 0.15  ##minimum reserve as a percent of system demand
spin_margin = 0.50 ##minimum spinning reserve as a percent of total reserve


##name of pownet datafile
data_name = './input/pownet_thai_v1_data_'+str(yr)+''



#read thermo plant parameters into DataFrame
df_gen = pd.read_csv('./input/data_thai_thermo_2016.csv',header=0)
df_gen['ini_on']=0 
df_gen['ini_mwh']=0 

#read derate factors of dispatchable units for the simulation year
df_gen_deratef = pd.read_csv('input/data_thai_thermo_deratef_'+str(yr)+'.csv',header=0) 
gen_units = list(df_gen_deratef.columns[4:]) ##v1.3

##hourly ts of load except the direct exports
df_load = pd.read_csv('./input/data_thai_load_2016.csv',header=0)   

##hourly ts of hydropower (Thai dams)
df_hydro = pd.read_csv('./input/hydropower/data_thai_hydro_'+str(yr)+'.csv',header=0)   

##hourly ts of hydropower import (Laotian dams)
df_hydro_import = pd.read_csv('./input/hydropower/data_thai_hydro_import_'+str(yr)+'.csv',header=0)   

##hourly ts of solar
df_solar = pd.read_csv('./input/data_thai_solar_2016.csv',header=0)   

##hourly ts of wind
df_wind = pd.read_csv('./input/data_thai_wind_2016.csv',header=0)

#read transmission path parameters into DataFrame
df_trans1 = pd.read_csv('./input/data_thai_transparam_2016.csv',header=0)

#capacity and susceptence of each transmission line (both directions)
df_trans2 = pd.DataFrame([df_trans1['sink'],df_trans1['source'],df_trans1['linemva'],df_trans1['linesus']]).transpose()
df_trans2.columns = ['source','sink','linemva','linesus']
df_paths = pd.concat([df_trans1,df_trans2], axis=0)
df_paths.index = np.arange(len(df_paths))

#hourly ts of reserve for national demand
df_reserves = pd.DataFrame((df_load.iloc[:,4:184].sum(axis=1)*res_margin).values,columns=['Reserve'])



###list nodes
h_nodes = ['Sirindhorn','BangLangDam','BhumibolDam','ChulabhornDam','KaengKrachanDam','KiridharnDam','LamTakhongJVDam',
           'PakMunDam','RajjaprabhaDam','SirikitDam','SrinagarindDam','ThungNaDam','UbolratanaDam','VajiralongkornDam']

h_imports = ['HouayHo','NamLeuk','NamMang3','NamNgum1','NamNgum2','NamTheun2','TheunHinboun','Xeset1','Xeset2']

s_nodes = ['Phrae','PranBuri','ThatPhanom','Pangnga2','ChonBuri3','Thalan2','Ubon2','LopBuri2','NakhonChaisi',
           'NakhonNayok','NakhonPhanom','Pattani','SakonNakhon','Sukhothai','Salokbat',]

w_nodes = ['Chaiyaphum1','NakhonRatchasima2']

gn_nodes = ['304IPNPPA9','BaanRai','BangchakRefinery','GhecoOne','GulfJPNS','GulfJPUT','HongsaLignite','KaengKhoi2',
            'MitrBiopower','NakhonPathom','NikomMapTaPhut','NongKhai','NorthBangkok','Phetchaburi','PTTOlefins',
            'RatchaburiThermal','Rayong','SrirachaRefinery','UWCKomen'] ##Thermoplants without demand

gd_nodes = ['Ayutthaya1','Ayutthaya2','BangKapi','BangkokNoi','BangMunNak','BangPakong','BoWin','BuriRam',
            'ChonBuri','ChonBuri2','Chumphon','Kalasin','Kamphaengphet','Kanchanaburi',
            'Kanchanaburi2','Khanom','KhonKaen1','KhonKaen3','Krabi','Lampang1','Lamphun2','LanKrabu',
            'LopBuri1','MaeHongSon','MaeMoh3','MaeTaeng','Mukdahan','NakhonRatchasima1',
            'NakhonSawan','NakhonSiThammarat','NamPhong2','NongChok','Phon','Phuket1','PrachinBuri1','PrachinBuri2',
            'PrachuapKhiriKhan','Rangsit','Ratchaburi','Ratchaburi3','Rayong1','Rayong2','RoiEt','Sadao',
            'SamutSakhon1','Saraburi1','Saraburi2','Saraburi3','Songkhla','SouthBangkok','SuphanBuri',
            'SuratThani','Surin','UbonRatchathani1','UdonThani1','WangNoi','Yala'] ##Thermoplants with demand

g_nodes = gn_nodes + gd_nodes
print ('Gen_Nodes:',len(g_nodes))

td_nodes = ['AkaraMining','AmnatCharoen','AngThong1','AngThong2','AoPhai','BanBueng','BanDon','BangLamung1','BangPaIn1',
            'BangPaIn2','BangPhli','BangSaphan','BanKhai','BanPhai','BanPong1','BanPong2','Banteay_Meanchay',
            'BuengSamPhan','ChaAm','Chacheongsao','ChaengWatthana','ChaiBadan','ChaiNat','Chanthaburi','Chatuchak',
            'ChiangMai1','ChiangMai2','ChiangMai3','Chiangrai','ChiupingMalaysia','ChomBueng','ChomThien',
            'ChomThong','ChumPhae','DoembangNangbuat','GurunMalaysia','HangChat','HatYai1','HatYai2','HuaHin',
            'HuaWat','KaengKhoi','KamphaengSaen','Kantharalak','KhlongNgae','Khong','KhonKaen2','Klaeng',
            'LamPooRa','LangSuan','LatPhrao','Loei','LomSak','MaeChan','MahaSarakham','Manorom',
            'NakhonPhanom2','NamPhong1','Nan1','NavaNakhon','Nonthaburi','OnNuch','Pakbo','PakChong','Paksan',
            'Phachi2','Phangnga2','PhanThong','Phatthalung','Phayao','Phetchabun','Phichit','Phitsanulok1',
            'Phitsanulok2','Phuket2','Phuket3','Phunphin','PluakDaeng','PrakhonChai','Ranong','Ranot',
            'Ratchaburi1','Ratchaburi2','Ratchadaphisek','Rayong3','RoiEt2','SaiNoi','SakonNakhon2',
            'SamPhran1','SamPhran2','SamutSakhon3','SamutSakhon4','SamutSongkhram','Saraburi4','Sattahip1',
            'Sattahip2','Satun','Sawankhalok','SiKhiu','SimahaPhot','SingBuri','SiRacha','SiSaKet','Somdet',
            'Songkhla2','SouthBangkokCC','SouthThonBuri','SungaiKolok','Surin2','Tak1','Tak2','Takhli2','TakuaPa','Thalan1',
            'Thalan3','ThaMuang','ThaTako','ThaWung','Theparak','Thoeng','ThungSong','UbonRatchathani2',
            'UdonThani2','UdonThani3','Uttaradit','WatthanaNakhon','Yala2','Yasothon'] ##Transformers with demand

tn_nodes = ['BangYo','BanVean','Donkoi','MaeMoh4','Nabong','Narathiwat','Nasaithong','NongBuaLamPhu','Paksong','Paktang',
            'PhangKhon','PhoneSoung','Phontong','Thakhek','Thalath','Thanaleng','BuengKan','Lampang2'] ##Transformers without demand


d_nodes = gd_nodes + td_nodes
print ('Demand_Nodes:',len(d_nodes))

all_nodes = h_nodes + h_imports + s_nodes + w_nodes + gn_nodes + gd_nodes + tn_nodes + td_nodes
print ('Total_Nodes:',len(all_nodes))
#print (all_nodes)

#list plant types
types = ['biomass_st','coal_st','coal_imp','gas_cc','gas_st','gas_gt','gas_ic','oil_gt','oil_ic','oil_st','wsth_st','slack']


########====== write data.dat file ======########
with open(''+str(data_name)+'.dat', 'w') as f:

###### generator sets by generator nodes
    for z in g_nodes:
        # node string
        z_int = g_nodes.index(z)
        f.write('set Node%dGenerators :=\n' % (z_int+1))
        # pull relevant generators
        for gen in range(0,len(df_gen)):
            if df_gen.loc[gen,'node'] == z:
                unit_name = df_gen.loc[gen,'name']
                unit_name = unit_name.replace(' ','_')
                f.write(unit_name + ' ')
        f.write(';\n\n')    
    
    
####### generator sets by type
    # Biomass
    f.write('set Biomass_st :=\n')
    # pull relevant generators
    for gen in range(0,len(df_gen)):
        if df_gen.loc[gen,'typ'] == 'biomass_st':
            unit_name = df_gen.loc[gen,'name']
            unit_name = unit_name.replace(' ','_')
            f.write(unit_name + ' ')
    f.write(';\n\n')    
   
    # Coal
    f.write('set Coal_st :=\n')
    # pull relevant generators
    for gen in range(0,len(df_gen)):
        if df_gen.loc[gen,'typ'] == 'coal_st':
            unit_name = df_gen.loc[gen,'name']
            unit_name = unit_name.replace(' ','_')
            f.write(unit_name + ' ')
    f.write(';\n\n')        
   
    # Coal_import(HongsaLignite)
    f.write('set Coal_imp :=\n')
    # pull relevant generators
    for gen in range(0,len(df_gen)):
        if df_gen.loc[gen,'typ'] == 'coal_imp':
            unit_name = df_gen.loc[gen,'name']
            unit_name = unit_name.replace(' ','_')
            f.write(unit_name + ' ')
    f.write(';\n\n')        

    # Gas_cc
    f.write('set Gas_cc :=\n')
    # pull relevant generators
    for gen in range(0,len(df_gen)):
        if df_gen.loc[gen,'typ'] == 'gas_cc':
            unit_name = df_gen.loc[gen,'name']
            unit_name = unit_name.replace(' ','_')
            f.write(unit_name + ' ')
    f.write(';\n\n')  

    # Gas_st
    f.write('set Gas_st :=\n')
    # pull relevant generators
    for gen in range(0,len(df_gen)):
        if df_gen.loc[gen,'typ'] == 'gas_st':
            unit_name = df_gen.loc[gen,'name']
            unit_name = unit_name.replace(' ','_')
            f.write(unit_name + ' ')
    f.write(';\n\n')  

    # Gas_gt
    f.write('set Gas_gt :=\n')
    # pull relevant generators
    for gen in range(0,len(df_gen)):
        if df_gen.loc[gen,'typ'] == 'gas_gt':
            unit_name = df_gen.loc[gen,'name']
            unit_name = unit_name.replace(' ','_')
            f.write(unit_name + ' ')
    f.write(';\n\n')

    # Gas_ic
    f.write('set Gas_ic :=\n')
    # pull relevant generators
    for gen in range(0,len(df_gen)):
        if df_gen.loc[gen,'typ'] == 'gas_ic':
            unit_name = df_gen.loc[gen,'name']
            unit_name = unit_name.replace(' ','_')
            f.write(unit_name + ' ')
    f.write(';\n\n')  

    # Oil_gt
    f.write('set Oil_gt :=\n')
    # pull relevant generators
    for gen in range(0,len(df_gen)):
        if df_gen.loc[gen,'typ'] == 'oil_gt':
            unit_name = df_gen.loc[gen,'name']
            unit_name = unit_name.replace(' ','_')
            f.write(unit_name + ' ')
    f.write(';\n\n')  

    # Oil_ic
    f.write('set Oil_ic :=\n')
    # pull relevant generators
    for gen in range(0,len(df_gen)):
        if df_gen.loc[gen,'typ'] == 'oil_ic':
            unit_name = df_gen.loc[gen,'name']
            unit_name = unit_name.replace(' ','_')
            f.write(unit_name + ' ')
    f.write(';\n\n')  

    # Oil_st
    f.write('set Oil_st :=\n')
    # pull relevant generators
    for gen in range(0,len(df_gen)):
        if df_gen.loc[gen,'typ'] == 'oil_st':
            unit_name = df_gen.loc[gen,'name']
            unit_name = unit_name.replace(' ','_')
            f.write(unit_name + ' ')
    f.write(';\n\n')  

    # Wsth_st
    f.write('set Wsth_st :=\n')
    # pull relevant generators
    for gen in range(0,len(df_gen)):
        if df_gen.loc[gen,'typ'] == 'wsth_st':
            unit_name = df_gen.loc[gen,'name']
            unit_name = unit_name.replace(' ','_')
            f.write(unit_name + ' ')
    f.write(';\n\n')  


    # Slack
    f.write('set Slack :=\n')
    # pull relevant generators
    for gen in range(0,len(df_gen)):
        if df_gen.loc[gen,'typ'] == 'slack':
            unit_name = df_gen.loc[gen,'name']
            unit_name = unit_name.replace(' ','_')
            f.write(unit_name + ' ')
    f.write(';\n\n')  

######Set nodes, sources and sinks
    # nodes
    f.write('set nodes :=\n')
    for z in all_nodes:
        f.write(z + ' ')
    f.write(';\n\n')
    
    # sources
    f.write('set sources :=\n')
    for z in all_nodes:
        f.write(z + ' ')
    f.write(';\n\n')
    
    # sinks
    f.write('set sinks :=\n')
    for z in all_nodes:
        f.write(z + ' ')
    f.write(';\n\n')

    # hydro_nodes
    f.write('set h_nodes :=\n')
    for z in h_nodes:
        f.write(z + ' ')
    f.write(';\n\n')

    # hydro_nodes for import
    f.write('set h_imports :=\n')
    for z in h_imports:
        f.write(z + ' ')
    f.write(';\n\n')

    # solar_nodes
    f.write('set s_nodes :=\n')
    for z in s_nodes:
        f.write(z + ' ')
    f.write(';\n\n')

    # wind_nodes
    f.write('set w_nodes :=\n')
    for z in w_nodes:
        f.write(z + ' ')
    f.write(';\n\n')

    # all demand nodes
    f.write('set d_nodes :=\n')
    for z in d_nodes:
        f.write(z + ' ')
    f.write(';\n\n')

    # generator with demand nodes
    f.write('set gd_nodes :=\n')
    for z in gd_nodes:
        f.write(z + ' ')
    f.write(';\n\n')

    # generator without demand nodes
    f.write('set gn_nodes :=\n')
    for z in gn_nodes:
        f.write(z + ' ')
    f.write(';\n\n')

    # transformer with demand nodes
    f.write('set td_nodes :=\n')
    for z in td_nodes:
        f.write(z + ' ')
    f.write(';\n\n')

    # transformer without demand nodes
    f.write('set tn_nodes :=\n')
    for z in tn_nodes:
        f.write(z + ' ')
    f.write(';\n\n')

    
################
#  parameters  #
################
       
####### simulation period and horizon
    f.write('param SimHours := %d;' % SimHours)
    f.write('\n')
    f.write('param SimDays:= %d;' % SimDays)
    f.write('\n\n')   
    f.write('param HorizonHours := %d;' % HorizonHours)
    f.write('\n\n')
    f.write('param TransLoss := %0.3f;' % TransLoss)
    f.write('\n\n')
    f.write('param n1criterion := %0.3f;' % n1criterion)
    f.write('\n\n')
    f.write('param spin_margin := %0.3f;' % spin_margin)
    f.write('\n\n')

    
####### create parameter matrix for generators
    f.write('param:' + '\t')
    for c in df_gen.columns:
        if c != 'name':
            f.write(c + '\t')
    f.write(':=\n\n')
    for i in range(0,len(df_gen)):    
        for c in df_gen.columns:
            if c == 'name':
                unit_name = df_gen.loc[i,'name']
                unit_name = unit_name.replace(' ','_')
                f.write(unit_name + '\t')  
            else:
                f.write(str((df_gen.loc[i,c])) + '\t')               
        f.write('\n')
    f.write(';\n\n')     

####### create parameter matrix for transmission paths (source and sink connections)
    f.write('param:' + '\t' + 'linemva' + '\t' +'linesus :=' + '\n')
    for z in all_nodes:
        for x in all_nodes:           
            f.write(z + '\t' + x + '\t')
            match = 0
            for p in range(0,len(df_paths)):
                source = df_paths.loc[p,'source']
                sink = df_paths.loc[p,'sink']
                if source == z and sink == x:
                    match = 1
                    p_match = p
            if match > 0:
                f.write(str(df_paths.loc[p_match,'linemva']) + '\t' + str(df_paths.loc[p_match,'linesus']) + '\n')
            else:
                f.write('0' + '\t' + '0' + '\n')
    f.write(';\n\n')

####### Hourly load and hydro
    # load (hourly)
    f.write('param:' + '\t' + 'SimDemand:=' + '\n')      
    for z in d_nodes:
        for h in range(0,len(df_load)): 
            f.write(z + '\t' + str(h+1) + '\t' + str(df_load.loc[h,z]) + '\n')
    f.write(';\n\n')

    # hydro (hourly)
    f.write('param:' + '\t' + 'SimHydro:=' + '\n')      
    for z in h_nodes:
        for h in range(0,len(df_hydro)): 
            f.write(z + '\t' + str(h+1) + '\t' + str(df_hydro.loc[h,z]) + '\n')
    f.write(';\n\n')

    # hydro_import (hourly)
    f.write('param:' + '\t' + 'SimHydroImport:=' + '\n')      
    for z in h_imports:
        for h in range(0,len(df_hydro_import)): 
            f.write(z + '\t' + str(h+1) + '\t' + str(df_hydro_import.loc[h,z]) + '\n')
    f.write(';\n\n')

    # solar (hourly)
    f.write('param:' + '\t' + 'SimSolar:=' + '\n')      
    for z in s_nodes:
        for h in range(0,len(df_solar)): 
            f.write(z + '\t' + str(h+1) + '\t' + str(df_solar.loc[h,z]) + '\n')
    f.write(';\n\n')

    # wind (hourly)
    f.write('param:' + '\t' + 'SimWind:=' + '\n')      
    for z in w_nodes:
        for h in range(0,len(df_wind)): 
            f.write(z + '\t' + str(h+1) + '\t' + str(df_wind.loc[h,z]) + '\n')
    f.write(';\n\n')

    # Deratef (hourly) 
    f.write('param:' + '\t' + 'SimDeratef:=' + '\n')      
    for z in gen_units:
        for h in range(0,len(df_gen_deratef)): 
            f.write(z + '\t' + str(h+1) + '\t' + str(df_gen_deratef.loc[h,z]) + '\n')
    f.write(';\n\n')
    
###### System wide hourly reserve
    f.write('param' + '\t' + 'SimReserves:=' + '\n')
    for h in range(0,len(df_load)):
            f.write(str(h+1) + '\t' + str(df_reserves.loc[h,'Reserve']) + '\n')
    f.write(';\n\n')
    

print ('data ready for',yr)
