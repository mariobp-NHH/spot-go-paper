# -*- coding: utf-8 -*-
"""
Created on Mon May  2 13:37:58 2022

@author: s14761
"""


if __name__=='__main__': 
    
    #Colors
    '''
    colors = {
        "charcoal": "#264653ff",
        "persian-green": "#2a9d8fff",
        "orange-yellow-crayola": "#e9c46aff",
        "sandy-brown": "#f4a261ff",
        "burnt-sienna": "#e76f51ff"}
    '''
    colors = {
        "c": "#264653ff",
        "p-g": "#2a9d8fff",
        "o-y-c": "#e9c46aff",
        "s-b": "#f4a261ff",
        "b-s": "#e76f51ff"}
    
    ##Plot the functions
    import matplotlib.pyplot as plt
    #Spot market
    fig, ax = plt.subplots(ncols = 2, figsize = (20, 9))
    #Axes1. pns<pss
    x1=[0, 0, 2, 2]
    y1=[0, 12, 10, 0]
    x2=[0, 0, 10, 14, 2, 0]
    y2=[12, 14, 14, 10, 10, 12]
    x3=[2, 2, 14, 14]
    y3=[0, 10, 10, 0]
    x4=[7, 8]
    y4a=[7, 7]
    y4b=[8, 8]
    ax[0].fill_between(x1,y1, edgecolor='black', facecolor='white', alpha=1)
    ax[0].fill_between(x2,y2, edgecolor='black', facecolor='white', alpha=1)
    ax[0].fill_between(x3,y3, edgecolor='black', facecolor='white', alpha=1)
    #ax[0].fill_between(x4,y4a,y4b, edgecolor='black', facecolor='white', alpha=1)
    ax[0].text(1, 0.3, "$q_2^{s1}=0$", fontsize=18)
    ax[0].text(1, 1.3, "$q_1^{s1}=a_2^s+a_1^s$", fontsize=18)
    ax[0].text(5, 4, "$q_2^{s1}=a_2^s-T$", fontsize=18)
    ax[0].text(5, 5, "$q_1^{s1}=a_1^s+T$", fontsize=18)
    ax[0].text(1, 12, "$q_2^{s1}=a_2^s+a_1^s-k_1^s$", fontsize=18)
    ax[0].text(1, 13, "$q_1^{s1}=k_1^s$", fontsize=18)
    ax[0].set_xlim(0, 15)
    ax[0].set_ylim(0, 15)
    ax[0].set(xticks=[2, 10, 12, 14], xticklabels=['T', '$k-T$', 'k', 'k+T'],
              yticks=[2, 10, 12, 14], yticklabels=['T', '$k-T$', 'k', 'k+T'])
    ax[0].set_xticklabels(['T', '$k-T$', 'k', 'k+T'], fontsize=16)
    ax[0].set_yticklabels(['T', '$k-T$', 'k', 'k+T'], fontsize=16)
    ax[0].set_ylabel('$a_1^{s}$', fontsize=18)
    ax[0].set_xlabel('$a_2^{s}$', fontsize=18)
    ax[0].set_title("Spot market (S1) $(p_1^{s}\leq p_2^{s})$", fontsize=20)
    right_side = ax[0].spines["right"]
    top_side = ax[0].spines["top"]
    right_side.set_visible(False)
    top_side.set_visible(False)
    
    #Axes2. pns>pss
    x1=[0, 0, 10, 12]
    y1=[0, 2, 2, 0]
    x2=[0, 0, 10, 10, 0]
    y2=[2, 14, 14, 2, 2]
    x3=[12,10, 10, 14, 14, 12]
    y3=[0, 2, 14, 10, 0, 0]
    x4=[7, 8]
    y4a=[7, 7]
    y4b=[8, 8]
    ax[1].fill_between(x1,y1, edgecolor='black', facecolor='white', alpha=1)
    ax[1].fill_between(x2,y2, edgecolor='black', facecolor='white', alpha=1)
    ax[1].fill_between(x3,y3, edgecolor='black', facecolor='white', alpha=1)
    #ax[1].fill_between(x4,y4a,y4b, edgecolor='black', facecolor='white', alpha=1)
    ax[1].text(1, 0.3, "$q_2^{s2}=a_2^s+a_1^s$", fontsize=18)
    ax[1].text(1, 1.3, "$q_1^{s2}=0$", fontsize=18)
    ax[1].text(5, 4, "$q_2^{s2}=a_2^s+T$", fontsize=18)
    ax[1].text(5, 5, "$q_1^{s2}=a_1^s-T$", fontsize=18)
    ax[1].text(10.1, 8, "$q_2^{s2}=k_2^s$", fontsize=18)
    ax[1].text(10.1, 9, "$q_1^{s2}=a_2^s+a_1^s-k_2^s$", fontsize=18)
    ax[1].set_xlim(0, 15)
    ax[1].set_ylim(0, 15)
    ax[1].set(xticks=[2, 10, 12, 14], xticklabels=['T', '$k-T$', 'k', 'k+T'],
              yticks=[2, 10, 12, 14], yticklabels=['T', '$k-T$', 'k', 'k+T'])
    ax[1].set_xticklabels(['T', '$k-T$', 'k', 'k+T'], fontsize=16)
    ax[1].set_yticklabels(['T', '$k-T$', 'k', 'k+T'], fontsize=16)
    ax[1].set_ylabel('$a_1^{s}$', fontsize=18)
    ax[1].set_xlabel('$a_2^{s}$', fontsize=18)
    ax[1].set_title("Spot market (S2) $(p_1^{s}> p_2^{s})$", fontsize=20)
    right_side = ax[1].spines["right"]
    top_side = ax[1].spines["top"]
    right_side.set_visible(False)
    top_side.set_visible(False)
    
    #GO market
    fig, ax = plt.subplots(ncols = 2, figsize = (20, 9))
    #Axes1. pns<pss
    x1=[0, 0, 2, 2]
    y1=[0, 5, 3, 0]
    x2=[0, 0, 7, 11, 2, 0]
    y2=[5, 7, 7, 3, 3, 5]
    x3=[2, 11]
    y3a=[0, 0]
    y3b=[3, 3]
    x4=[2, 3]
    y4a=[2, 2]
    y4b=[3, 3]     
    ax[0].fill_between(x1,y1, edgecolor='black', facecolor='white', alpha=1)
    ax[0].fill_between(x2,y2, edgecolor='black', facecolor='white', alpha=1)
    ax[0].fill_between(x3,y3a,y3b, edgecolor='black', facecolor='white', alpha=1)
    #ax[0].fill_between(x4,y4a,y4b, edgecolor='black', facecolor='white', alpha=1)

    ax[0].text(0.3, 0.3, "$q_2^{go21}=0$", fontsize=18)    
    ax[0].text(0.3, 0.8, "$q_1^{go21}=a_2^{go}+a_1^{go}$", fontsize=18)
    
    ax[0].text(4.2, 1.7, "$q_2^{go21}=max \{0, a_2^{go}-a_1^{go}-k_1^{go2}\}$", fontsize=18)
    ax[0].text(4.2, 2.2, "$q_1^{go21}=min \{a_2^{go}-a_1^{go},k_1^{go2}\}$", fontsize=18)
    ax[0].text(4.2, 2.7, "design 1 (GO2, no-constraint):", fontsize=18)
    
    ax[0].text(4.2, 0.2, "$q_2^{go21}=a_2^{go}-T$", fontsize=18)
    ax[0].text(4.2, 0.7, "$q_1^{go21}=a_1^{go}+T$", fontsize=18)
    ax[0].text(4.2, 1.2, "design 2 (GO2, constraint):", fontsize=18)    
    
    ax[0].text(0.3, 5, "$q_2^{go21}=a_2^{go}+a_1^{go}-k_1^{go2}$", fontsize=18)
    ax[0].text(0.3, 5.5, "$q_1^{go21}=k_1^{go2}$", fontsize=18)
    
    ax[0].set_xlim(0, 12)
    ax[0].set_ylim(0, 8)
    ax[0].set(xticks=[2, 5, 9, 11], xticklabels=['T', '$k_1^{go2}$', '$k_2^{go2}$', '$k_2^{go2}+T$'],
              yticks=[2, 5, 7], yticklabels=['T', '$k_1^{go2}$', '$k_1^{go2}+T$'])
    ax[0].set_xticklabels(['T', '$k_1^{go2}$', '$k_2^{go2}$', '$k_2^{go2}+T$'], fontsize=16)
    ax[0].set_yticklabels(['T', '$k_1^{go2}$', '$k_1^{go2}+T$'], fontsize=16)
    ax[0].set_ylabel('$a_1^{go}$', fontsize=18)
    ax[0].set_xlabel('$a_2^{go}$', fontsize=18)
    ax[0].set_title("Spot market (S2) $(p_1^{s}>p_2^{s})$, GO21 market $(p_1^{go2}\leq p_2^{go2})$", fontsize=20)
    right_side = ax[0].spines["right"]
    top_side = ax[0].spines["top"]
    right_side.set_visible(False)
    top_side.set_visible(False)
    
    #Axes2. pns>pss
    x1=[0, 7, 9]
    y1a=[0, 0, 0]
    y1b=[2, 2, 0]
    x2=[0, 7]
    y2a=[2,2]
    y2b=[7,7]
    x3=[7,9, 11]
    y3a=[2, 0, 0]
    y3b=[7,5,3]
    x4=[2, 3]
    y4a=[2, 2]
    y4b=[3, 3]     
    ax[1].fill_between(x1,y1a,y1b, edgecolor='black', facecolor='white', alpha=1)
    ax[1].fill_between(x2,y2a,y2b, edgecolor='black', facecolor='white', alpha=1)
    ax[1].fill_between(x3,y3a,y3b, edgecolor='black', facecolor='white', alpha=1)
    #ax[1].fill_between(x4,y4a,y4b, edgecolor='black', facecolor='white', alpha=1)

    ax[1].text(0.3, 0.3, "$q_2^{go22}=a_2^{go}+a_1^{go}$", fontsize=18)    
    ax[1].text(0.3, 0.8, "$q_1^{go22}=0$", fontsize=18)
    
    ax[1].text(0.3, 5.7, "$q_2^{go22}=min \{a_2^{go}-a_1^{go},k_2^{go2}\}$", fontsize=18)
    ax[1].text(0.3, 6.2, "$q_1^{go22}=max \{0, a_2^{go}-a_1^{go}-k_2^{go2}\}$", fontsize=18)
    ax[1].text(0.3, 6.7, "design 1 (GO2, no-constraint):", fontsize=18)
    
    ax[1].text(0.3, 3.7, "$q_2^{go22}=a_2^{go}+T$", fontsize=18)
    ax[1].text(0.3, 4.2, "$q_1^{go22}=a_1^{go}-T$", fontsize=18)
    ax[1].text(0.3, 4.7, "design 2 (GO2, constraint):", fontsize=18)    
    
    ax[1].text(7.3, 2, "$q_2^{go22}=k_2^{go2}$", fontsize=18)
    ax[1].text(7.3, 2.5, "$q_1^{go22}=a_2^{go}+a_1^{go}-k_2^{go2}$", fontsize=18)
    
    ax[1].set_xlim(0, 12)
    ax[1].set_ylim(0, 8)
    ax[1].set(xticks=[2, 5, 9, 11], xticklabels=['T', '$k_1^{go2}$', '$k_2^{go2}$', '$k_2^{go2}+T$'],
              yticks=[2, 5, 7], yticklabels=['T', '$k_1^{go2}$', '$k_1^{go2}+T$'])
    ax[1].set_xticklabels(['T', '$k_1^{go2}$', '$k_2^{go2}$', '$k_2^{go2}+T$'], fontsize=16)
    ax[1].set_yticklabels(['T', '$k_1^{go2}$', '$k_1^{go2}+T$'], fontsize=16)
    ax[1].set_ylabel('$a_1^{go}$', fontsize=18)
    ax[1].set_xlabel('$a_2^{go}$', fontsize=18)
    ax[1].set_title("Spot market (S2) $(p_1^{s}>p_2^{s})$, GO22 market $(p_1^{go2}> p_2^{go2})$", fontsize=20)
    right_side = ax[1].spines["right"]
    top_side = ax[1].spines["top"]
    right_side.set_visible(False)
    top_side.set_visible(False)
    
    ##Equilibrium areas Spot market
    fig, ax = plt.subplots(ncols = 1, figsize = (10, 10))
    #Axes1. pns<pss
    x1=[0, 2]
    y1a=[0, 0]
    y1b=[2, 2]
    x2=[0, 2]
    y2a=[2,2]
    y2b= [14,14]
    x3=[2, 14]
    y3a=[0, 0]
    y3b=[2,2]
    x4=[2, 10, 14]
    y4a=[2, 2, 2]
    y4b=[14,14, 10]
    x5=[7, 8]
    y5a=[7, 7]
    y5b=[8, 8]
    ax.fill_between(x1,y1a, y1b, edgecolor='black', facecolor='white', alpha=1)
    ax.fill_between(x2,y2a,y2b, edgecolor='black', facecolor='white', alpha=1)
    ax.fill_between(x3,y3a,y3b, edgecolor='black', facecolor='white', alpha=1)
    ax.fill_between(x4,y4a,y4b, edgecolor='black', facecolor='white', alpha=1)
    ax.fill_between(x5,y5a,y5b, edgecolor='black', facecolor='white', alpha=1)
    ax.plot([8], [8], marker="o", markersize=10, markeredgecolor="black", markerfacecolor="black")
    ax.text(8.3, 8, "$(a_1^{s}=8,a_2^{s}=8) $", fontsize=18)
    ax.plot([7], [8], marker="o", markersize=10, markeredgecolor="black", markerfacecolor="black")
    ax.text(3.7, 8, "$(a_1^{s}=8,a_2^{s}=7) $", fontsize=18)
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 15)
    ax.set(xticks=[2, 10, 12, 14], xticklabels=['T', '$k-T$', 'k', 'k+T'],
              yticks=[2, 10, 12, 14], yticklabels=['T', '$k-T$', 'k', 'k+T'])
    ax.set_xticklabels(['T', '$k-T$', 'k', 'k+T'], fontsize=16)
    ax.set_yticklabels(['T', '$k-T$', 'k', 'k+T'], fontsize=16)
    ax.set_ylabel('$a_1^{s}$', fontsize=18)
    ax.set_xlabel('$a_2^{s}$', fontsize=18)
    ax.set_title("Spot market (equilibrium areas)", fontsize=20)
    right_side = ax.spines["right"]
    top_side = ax.spines["top"]
    right_side.set_visible(False)
    top_side.set_visible(False)
    
    ##Equilibrium areas GO market
    fig, ax = plt.subplots(ncols = 2, figsize = (20, 9))
    #Axes1. a1s=a2s=8
    x1=[0, 4, 12]
    y1a=[0, 0, 0]
    y1b=[12, 12, 4]
    x2=[2, 4]
    y2a=[2, 2]
    y2b=[4, 4]
    ax[0].fill_between(x1,y1a, y1b, edgecolor='black', facecolor='white', alpha=1)
    ax[0].fill_between(x2,y2a,y2b, edgecolor='black', facecolor='white', alpha=1)
    ax[0].plot([4], [4], marker="o", markersize=10, markeredgecolor="black", markerfacecolor="black")
    ax[0].text(4.3, 4, "$(a_1^{go}=4,a_2^{go}=4) $", fontsize=18)
    #ax[0].plot([3], [4], marker="o", markersize=10, markeredgecolor="black", markerfacecolor="black")
    #ax[0].text(0.7, 4.5, "$(a_1^{go}=4,a_2^{go}=3) $", fontsize=18)
    ax[0].set_xlim(0, 13)
    ax[0].set_ylim(0, 13)
    ax[0].set(xticks=[6, 10, 12], xticklabels=['$k_2^{go1}$', '$k_2^{go2}$', '$k_2^{go2}+T$'],
              yticks=[6, 10, 12], yticklabels=['$k_1^{go2}$', '$k_1^{go1}$', '$k_1^{go1}+T$'])
    ax[0].set_xticklabels(['$k_2^{go1}$', '$k_2^{go2}$', '$k_2^{go2}+T$'], fontsize=16)
    ax[0].set_yticklabels(['$k_1^{go2}$', '$k_1^{go1}$', '$k_1^{go1}+T$'], fontsize=16)
    ax[0].set_ylabel('$a_1^{s}$', fontsize=18)
    ax[0].set_xlabel('$a_2^{s}$', fontsize=18)
    ax[0].set_title("GO market (equilibrium areas), $a_1^s=a_2^s=8$", fontsize=20)
    right_side = ax[0].spines["right"]
    top_side = ax[0].spines["top"]
    right_side.set_visible(False)
    top_side.set_visible(False)
    #Axes1. a1s=8,a2s=7
    x1=[0, 3, 9]
    y1a=[0, 0, 0]
    y1b=[12, 12, 6]
    x2=[2, 3]
    y2a=[2, 2]
    y2b=[4, 4]
    ax[1].fill_between(x1,y1a, y1b, edgecolor='black', facecolor='white', alpha=1)
    ax[1].fill_between(x2,y2a,y2b, edgecolor='black', facecolor='white', alpha=1)
    ax[1].plot([3], [4], marker="o", markersize=10, markeredgecolor="black", markerfacecolor="black")
    ax[1].text(3.3, 4, "$(a_1^{go}=4,a_2^{go}=3) $", fontsize=18)
    ax[1].plot([3], [3], marker="o", markersize=10, markeredgecolor="black", markerfacecolor="black")
    ax[1].text(3.3, 3, "$(a_1^{go}=3,a_2^{go}=3) $", fontsize=18)
    ax[1].set_xlim(0, 13)
    ax[1].set_ylim(0, 13)
    ax[1].set(xticks=[5, 7, 9], xticklabels=['$k_2^{go1}$', '$k_2^{go2}$', '$k_2^{go2}+T$'],
              yticks=[6, 10, 12], yticklabels=['$k_1^{go2}$', '$k_1^{go1}$', '$k_1^{go1}+T$'])
    ax[1].set_xticklabels(['$k_2^{go1}$', '$k_2^{go2}$', '$k_2^{go2}+T$'], fontsize=16)
    ax[1].set_yticklabels(['$k_1^{go2}$', '$k_1^{go1}$', '$k_1^{go1}+T$'], fontsize=16)
    ax[1].set_ylabel('$a_1^{s}$', fontsize=18)
    ax[1].set_xlabel('$a_2^{s}$', fontsize=18)
    ax[1].set_title("GO market (equilibrium areas), $a_1^s=8;a_2^s=7$", fontsize=20)
    right_side = ax[1].spines["right"]
    top_side = ax[1].spines["top"]
    right_side.set_visible(False)
    top_side.set_visible(False)
    
    
    
    
    