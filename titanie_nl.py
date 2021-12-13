# Databricks notebook source
import pandas as pd
import numpy as np

# COMMAND ----------

x1=np.arange(10)
y1=np.random.random(10)
x2=np.arange(4,12)
y2=np.random.random(8)
df1 = pd.DataFrame({'x':x1,'y1':y1})
df2 = pd.DataFrame({'x':x2,'y2':y2})
df1.head(3)

# COMMAND ----------

df1.to_csv('df1.csv')

# COMMAND ----------

# new changes

# COMMAND ----------



# COMMAND ----------


