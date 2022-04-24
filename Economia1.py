# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 20:21:23 2022

@author: figue
"""

import matplotlib.pyplot as plt
import numpy as np
coeficienteEnergiaNoRenovable = 0.9
coeficienteEnergiaRenovable = 0.6
ALPHA = 1 - coeficienteEnergiaRenovable   # capital share in Energia Renovable
BETA = 1 - coeficienteEnergiaNoRenovable   # capital share in Energia No Renovable
KBAR = 45798 # Total capital supply
LBAR = 35693 # Total labor supply
def FuncionProduccionEnergiaRenovable(capital, labour, alpha):
    
    return (capital**alpha)*(labour**(1 - alpha))

def FuncionProduccionEnergiaNoRenovable(capital, labour, beta):
    
    return (capital**beta)*(labour**(1 - beta))

def edgeworth(L, Kbar=KBAR, Lbar=LBAR,alpha=ALPHA, beta=BETA):
    """efficiency locus: """
    a = (1-alpha)/alpha
    b = (1-beta)/beta
    return b*L*Kbar/(a*(Lbar-L)+b*L)
def FPP(LA,Kbar=KBAR, Lbar=LBAR,alpha=ALPHA,beta=BETA):
    KA = edgeworth(LA, Kbar, Lbar, alpha, beta)
    RTS = (alpha/(1-alpha))*(KA/LA)
    QA = FuncionProduccionEnergiaRenovable(KA, LA, alpha)
    QM = FuncionProduccionEnergiaNoRenovable(Kbar-KA, Lbar-LA, beta)
    La = np.arange(0,Lbar)
    Ka = edgeworth(La, Kbar, Lbar, alpha, beta)
    Qa = FuncionProduccionEnergiaRenovable(Ka, La, alpha)
    Qm = FuncionProduccionEnergiaNoRenovable(Kbar-Ka, Lbar-La, beta)
    ax.set_xlim(0, Lbar)
    ax.set_ylim(0, Kbar)
    ax.plot(Qa, Qm, 'k-')
    ax.set_xlabel(r'$NORenovable$', fontsize=20)
    ax.set_ylabel(r'$Renovable$', fontsize=20)
    plt.show()
fig, ax = plt.subplots(figsize=(6,4))
FPP(1)