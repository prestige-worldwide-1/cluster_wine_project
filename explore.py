import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib import patches

def plot_key_features(train):
    
    plt.figure(figsize=(1.5,5))
    ax = sns.heatmap(train[abs(train.corr()['quality']).sort_values(ascending=False).index].corr()['quality'].to_frame()[1:],
                        annot=True, cmap='RdYlGn', vmin=-1, vmax=1)
    cbar = ax.collections[0].colorbar
    cbar.ax.tick_params(right=False, labelsize=8) 
    cbar.set_ticks([-1, -.5, 0, .5, 1])
    plt.tick_params(axis='both', left=False, bottom=False)

    rectangle = patches.Rectangle((0, 0), 1, 4, linewidth=1.5,
                                  edgecolor='#C40000', facecolor='none')
    ax.add_patch(rectangle)

    plt.title('4 Strongest Drivers of Quality')
    plt.show()
    
    
def plot_alcohol_by_quality(train):
    
    fig, axes = plt.subplots(2, 1, figsize=(6,6))
    sns.barplot(data=train, x='quality', y='alcohol', color='green',
                errorbar=None, ax=axes[0])

    for p in axes[0].patches:
        axes[0].annotate(f'{str(round(p.get_height(), 1))}%', 
                    (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=8)

    axes[0].set_xlabel('')

    sns.stripplot(data=train, x='quality', y='alcohol', size=1, 
                  color='green', jitter=.2, ax=axes[1])

    axes[1].set_xlabel('Quality', fontsize=10, labelpad=5)

    plt.suptitle('Higher Quality Wines Have More Alcohol')

    for ax in axes:
        ax.set_ylabel('Alcohol', rotation=0, fontsize=10, labelpad=20)
        ax.tick_params(axis='both', left=False, bottom=False, labelsize=8)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f'{round(x)}%'))

    sns.despine()
    plt.tight_layout()
    plt.show()