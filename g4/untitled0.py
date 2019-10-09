#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:16:05 2019

@author: lynn
"""
import plotly 
# only for offline
import plotly.graph_objects as go
import pandas as pd
path_meta = 'Group_4_meta.csv'
#movie_data =pd.read_csv(path, sep='\t', head = 0)
result_meta_data = pd.read_csv(path_meta)

path_video = 'Group_4_video_predictions92.csv'
#movie_data =pd.read_csv(path, sep='\t', head = 0)
result_video_data = pd.read_csv(path_video)


g4_result = pd.merge(result_meta_data,result_video_data,how='outer')
