#!/usr/bin/python3

import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt


def create_scatter_plot_time_vs_messages(df, save_fig_name, title, figure_size):
    #saving images in a folder
    save_fig_name = 'pics/'+save_fig_name+'_scatter_plot'

    for i in range(len(df['Time'])):
        _tmp = df['Time'][i].split(':')
        df['Time'][i] = _tmp[0]
        _tmp = _tmp[1].split()[1]
        if _tmp == 'PM':
            df['Time'][i]= str(int(df['Time'][i]) + 12)


    #grouping wrt senders
    hist = df.groupby('Time', as_index=False).count()

    plt.bar(hist['Time'], hist['Message'], color="coral", alpha=0.9)

    #plt.scatter(df['Time'], df['Message'], color="blue", alpha=0.5)

    plt.xlabel("Time")
    plt.ylabel("Messages")

    #should make room for the xlabel.
    plt.tight_layout()

    #save the graph
    plt.savefig(fname=save_fig_name)


    plt.show()
    

def create_bar_chart_sender_vs_messages(df, save_fig_name, title, figure_size):
    #saving images in a folder
    save_fig_name = 'pics/'+save_fig_name + '_bar_chart'

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




df = pd.read_csv('data2.csv')

create_scatter_plot_time_vs_messages(df, 'design_lab', 'Messages sent in design lab group', (50,5))
#create_bar_chart_sender_vs_messages(df, 'cse_group', 'Messages sent in CSE group', (100,5))