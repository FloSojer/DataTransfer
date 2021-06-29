import shutil
import os

import FolderDirectories as foldDir

def mAm():
    for f in  os.listdir(foldDir.source):
        if(f[0:2] == 'AM'):
            shutil.move(foldDir.source + f, foldDir.am)
            os.rename(foldDir.am + f, foldDir.am+f[3:])

def mBWM_Geig():
    for f in  os.listdir(foldDir.source):
        if(f[0:8] == 'BWM_Geig'):
            shutil.move(foldDir.source + f, foldDir.bwm_geig)
            os.rename(foldDir.bwm_geig + f, foldDir.bwm_geig+f[9:])

def mBWM_Schuh():
    for f in  os.listdir(foldDir.source):
        if(f[0:9] == 'BWM_Schuh'):
            shutil.move(foldDir.source + f, foldDir.bwm_schuh)
            os.rename(foldDir.bwm_schuh + f, foldDir.bwm_schuh+f[10:])

def mCopr():
    for f in  os.listdir(foldDir.source):
        if(f[0:4] == 'Copr'):
            shutil.move(foldDir.source + f, foldDir.copr)
            os.rename(foldDir.copr + f, foldDir.copr+f[5:])

def mDbi1():
    for f in  os.listdir(foldDir.source):
        if(f[0:4] == 'DBI1'):
            shutil.move(foldDir.source + f, foldDir.dbi1)
            os.rename(foldDir.dbi1 + f, foldDir.dbi1+f[5:])

def mNvs1_pr():
    for f in  os.listdir(foldDir.source):
        if(f[0:6] == 'NVS_Pr'):
            shutil.move(foldDir.source + f, foldDir.nvs1_pr)
            os.rename(foldDir.nvs1_pr + f, foldDir.nvs1_pr+f[7:])

def mNvs_th():
    for f in  os.listdir(foldDir.source):
        if(f[0:6] == 'NVS_Th'):
            shutil.move(foldDir.source + f, foldDir.nvs_th)
            os.rename(foldDir.nvs_th + f, foldDir.nvs_th+f[7:])

def mPos_pra():
    for f in  os.listdir(foldDir.source):
        if(f[0:6] == 'POS_Pr'):
            shutil.move(foldDir.source + f, foldDir.pos_pr)
            os.rename(foldDir.pos_pr + f, foldDir.pos_pr+f[7:])

def mPos_the():
    for f in  os.listdir(foldDir.source):
        if(f[0:6] == 'POS_Th'):
            shutil.move(foldDir.source + f, foldDir.pos_th)
            os.rename(foldDir.pos_th + f, foldDir.pos_th+f[7:])

def mSyp_nemi():
    for f in  os.listdir(foldDir.source):
        if(f[0:8] == 'SYP_Nemi'):
            shutil.move(foldDir.source + f, foldDir.syp_nemi)
            os.rename(foldDir.syp_nemi + f, foldDir.syp_nemi+f[9:])

def mSyp_prax():
    for f in  os.listdir(foldDir.source):
        if(f[0:6] == 'SYP_Prax'):
            shutil.move(foldDir.source + f, foldDir.syp_prax)
            os.rename(foldDir.syp_prax + f, foldDir.syp_prax+f[7:])

def mTinf_sal():
    for f in  os.listdir(foldDir.source):
        if(f[0:8] == 'TINF_Sal'):
            shutil.move(foldDir.source + f, foldDir.tinf_sal)
            os.rename(foldDir.tinf_sal + f, foldDir.tinf_sal+f[9:])

def mTinf_Stolz():
    for f in  os.listdir(foldDir.source):
        if(f[0:10] == 'TINF_Stolz'):
            shutil.move(foldDir.source + f, foldDir.tinf_stol)
            os.rename(foldDir.tinf_stol + f, foldDir.tinf_stol+f[11:])

def mWir_Schuh():
    for f in  os.listdir(foldDir.source):
        if(f[0:9] == 'WIR_Schuh'):
            shutil.move(foldDir.source + f, foldDir.wir_schuh)
            os.rename(foldDir.wir_schuh + f, foldDir.wir_schuh+f[10:])