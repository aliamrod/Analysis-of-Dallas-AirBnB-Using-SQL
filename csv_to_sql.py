# -*- coding: utf-8 -*-
""" 
Created on Fri Nov 10 19:41:34 2023

@author: alia
"""
import pandas as pd
import glob, os
from sqlalchemy import create_engine

for file in glob.glob("*.csv"):
  df = pd.read_csv(file)

  # Create SQLAlchemy engine to connect to MySQL Database.
  engine = create_engine("mysql
