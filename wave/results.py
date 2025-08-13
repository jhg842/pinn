import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def wave1D(t, pred_u, true_u):
    # plt.plot(t, true_u, 
    #          color='blue', 
    #          linestyle='-', 
    #          linewidth=2.5, 
    #          label='True Value')

    # 예측값 (Predicted) 플로팅: 빨간색 점선
    plt.plot(t, pred_u, 
             color='red', 
             linestyle='--', 
             linewidth=2, 
             label='Predicted Value')

    # 그래프 제목 및 축 레이블 추가
    plt.title("Wave Prediction vs True Value", fontsize=16)
    plt.xlabel("Time (t)", fontsize=12)
    plt.ylabel("Amplitude (u)", fontsize=12)

    # 범례(legend) 표시
    plt.legend()
    
    plt.savefig('./2d.png', dpi = 300)
    
def wave2D(x, t, pred_u, true_u):
    X, Y = np.meshgrid(x,t)
    fig, axes = plt.subplots(1, 2, figsize=(16, 7), subplot_kw={'projection': '3d'})

# --- 3. 첫 번째 그래프 그리기 (axes[0]) ---
    ax1 = axes[0]
    surf1 = ax1.plot_surface(X, Y, pred_u, cmap='viridis', edgecolor='none')
    ax1.set_title("3D Surface Plot (Sinc Function)")
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_zlabel('z')
    fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=10)

    # --- 4. 두 번째 그래프 그리기 (axes[1]) ---
    ax2 = axes[1]
    surf2 = ax2.plot_surface(X, Y, true_u, cmap='plasma', edgecolor='none')
    ax2.set_title("3D Surface Plot (Cosine Function)")
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_zlabel('z')
    fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=10)

    # --- 5. 전체 레이아웃 조정 및 보여주기 ---
    plt.tight_layout() # 그래프들이 겹치지 않게 자동으로 간격 조절
    plt.savefig('./3d.png', dpi=300)
    
files = pd.read_csv('/home/work/physics/models/results_valid.csv')

x_unique = np.unique(files['Points_0'])
t_unique = np.unique(files['t'])

Nx = len(x_unique)
Nt = len(t_unique)

pred_u = files['pred_u'].to_numpy().reshape(Nt, Nx)
true_u = files['true_u'].to_numpy().reshape(Nt, Nx)

wave2D(x_unique, t_unique, pred_u, true_u)