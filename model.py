#!/usr/bin/python3

import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt


def create_bar_chart_sender_vs_messages(df, save_fig_name, title, figure_size):
    #saving images in a folder
    save_fig_name = 'pics/'+save_fig_name

    #grouping wrt senders
    hist = df.groupby('Sender', as_index=False).count()

    fig, ax = plt.subplots(figsize=figure_size)

    #barchart
    ax.bar(hist['Sender'], hist['Message'], width=0.2, color="coral")

    ax.set_alpha(0.8)
    ax.set_title(title)
    ax.set_xlabel("Sender Names")
    ax.set_ylabel("Message Count")

    #rotate x-labels to 45 deg
    plt.xticks(rotation="45")


    # set individual bar lables using above list
    for i in ax.patches:
        # get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.03, i.get_height()+2, \
                round(i.get_height()), fontsize=10,
                    color='dimgrey')


    #should make room for the xlabel.
    plt.tight_layout()

    #save the graph
    plt.savefig(fname=save_fig_name)


    plt.show()




df = pd.read_csv('data.csv')

create_bar_chart_sender_vs_messages(df, 'cse_group', 'Messages sent in CSE group', (100,5))
