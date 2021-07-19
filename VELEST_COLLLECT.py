#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 12:14:11 2021

@author: arhamze
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 19:21:24 2021

@author: arhamze
"""

"""
Code untuk mengambil analisis statistik hasil NonLinLoc
"""
import pandas as pd;import numpy as np;
from collections import defaultdict as dfdict
import glob
uniq_ID=input("Masukan ID gempa :")
file_name=glob.glob('*.loc.hyp')
file_name_skip_sum=[]
with open ("datavelest.cnv", "w") as file_cnv:
#with pd.ExcelWriter("Coleccting_statistic.xlsx", engine='xlsxwriter') as writer:
    for i in file_name:
        if i.startswith(str(uniq_ID)+".sum.grid0.loc.hyp"):continue
        file_name_skip_sum.append(i)
    data_pd_clt={}
    data_pd_res={}
    for i in file_name_skip_sum:
        data_collect=[]
        f=open(i)
        for n in f:
            n=str(n)
            data_collect.append(n)
        par_stop=0;par_stop1=0;par_stop2=0
        for n in data_collect:
            par_stop1+=1
            if n.startswith("GEOGRAPHIC"):break
        data_OT=data_collect[par_stop1-1]
        data_OT=data_OT.split()
        order=[2,3,4,5,6,7,9,11,13]
        data_OT=[data_OT[i] for i in order]
        data_OT=[float(k) for k in data_OT]
        data_OT2=[]
        h=0
        for v in data_OT:
            if h==0:
                v=str(v)
                v=v[2:]
                v=float(v)
                h+=1
            else :
                v=float(v)
            data_OT2.append(v)
        emag_ifx=[0.00,0]
        for z in emag_ifx:
            data_OT2.append(z)
        TT=data_OT2
        file_cnv.write("%2i%2i%2i %2i%2i %5.2f %7.4f%s %8.4f%s%7.2f %4.2f %1i\n" % (TT[0],TT[1],TT[2],TT[3],TT[4],TT[5],abs(TT[6]),"S",TT[7],"E",TT[8],TT[9],TT[10]))
        
        for n in data_collect:
            par_stop+=1
            if n.startswith("FOCALMECH"):break
        data_select=data_collect[par_stop:-2]; #print(data_select)
        header=data_select[0];data_saja=data_select[1:-1]
        header=header.split(); header_min_phase=header[1:]
        data_ae=[]
        for n in data_saja:
            n=n.split()
            data_ae.append(n)
        dictio={}
        random_l=[];
        dta_s=[0,1]
        for n in range(len(data_ae)):
            dictio[n]=data_ae[n]
            dta_s[0]=data_ae[n][0]
            dta_s[1]=data_ae[n][4]
            dta_s2=str(dta_s[0])+str(dta_s[1])
            random_l.append(dta_s2)
        i=i[-29:-14]
        data_pd_clt[i]=pd.DataFrame.from_dict(dictio, orient="index",columns=header_min_phase) #untuk versi statistik lengkap
        data_pd_res[i]=data_pd_clt[i]["Res"]
        data_pd_clt[i]["TTpred"]=data_pd_clt[i]["TTpred"].apply(pd.to_numeric)+data_pd_res[i].apply(pd.to_numeric)
        data_pd_clt[i]=data_pd_clt[i][["ID","Pha","TTpred"]]
        data_pd_clt[i].columns=range(data_pd_clt[i].shape[1])
        list_dt=data_pd_clt[i].values.tolist()
        h=0
        for p in list_dt:
            file_cnv.write("%4s%s%1i%6.2f   " % (p[0],p[1],1,p[2]))
            h+=1
            if h % 6 == 0:
                file_cnv.write("\n")
            if len(list_dt)==h:
                file_cnv.write("\n\n")
        file_cnv.write("%4i" % 9999)

                
