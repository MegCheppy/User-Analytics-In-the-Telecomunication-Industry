# %% [markdown]
# # Exploratory Data Analysis

# %% [markdown]
# The goal of this step is to understand the dataset, identify the missing values & outliers if any using visual and quantitative methods to get a sense of the story it tells. It suggests the next logical steps, questions, or areas of research for your project.

# %%
%load_ext autoreload
%autoreload 2


# %%
#import libraries and modules needed.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys

# %%
import warnings
warnings.filterwarnings('ignore')

# %%
sys.path.append(os.path.abspath(os.path.join('../scripts')))
from PreProcessing import PreProcess

# %%
PreProcess

# %% [markdown]
# ### Data Extraction

# %% [markdown]
# Here, we intend to have an overview of the data,understand what is in the columns and their sample values. The data was collected over a period of one month, as seen on the start and end dates.

# %%
#to read the data
db = pd.read_csv('../data/Tellco_data.csv', na_values=['?', None])
db

# %%
# column names
db.columns.tolist()

# %% [markdown]
# A description of the columns can be found here (https://docs.google.com/spreadsheets/d/1QUOXuXK-W_DOovwgB6DO6-MtNSBQ62gc/edit#gid=497912695).How information is stored in a DataFrame or a Python object affects what we can do with it and the outputs of calculations as well. There are two data types, float(numeric data) and object(text data.)

# %%
#properties of the columns
db.dtypes

# %%
# number of data points
print(f" There are {db.shape[0]} rows and {db.shape[1]} columns")

# %% [markdown]
# ### Data Cleaning

# %% [markdown]
# Checking for missing values in the data and fixing outliers.

# %%
#number of missing values for each column.
db.isnull().sum()

# %%
# how many missing values exist or better still what is the % of missing values in the dataset?
def percent_missing(db):

    # Calculate total number of cells in dataframe
    totalCells = np.product(db.shape) #multiplication of rows and columns from np.product function

    # Count number of missing values per column
    missingCount = db.isnull().sum() #return no of missing rows for each column

    # Calculate total number of missing values
    totalMissing = missingCount.sum() 

    # Calculate percentage of missing values
    print("TellCo's data contains", round(((totalMissing/totalCells) * 100), 2), "%", "missing values.")

percent_missing(db)

# %% [markdown]
# We need to handle missing values with the help of the data types ouput above. From the rule of thumb, for any object/text data type,we use the mode function , we will need to use the mode function(most appearing) to fill the missing values. For numeric data, we use the mean and median functions to approximate values to fill in. To choose which method to use, we need to check for skewness of data. Skewness refer to the distortion of a symmetrical curve. If the curve shifts to the left(-vely skewed) or right(+vely skewed), it is skewed,if symmetric, the data is not skewed. If the data is not skewed, then we assign the missing values with the mean or median. If skewed, we just use the median value.

# %%
#to calculate skewness,
db.skew(axis=0)

# %% [markdown]
# From the output, the +ve values shows the data in the columns is +vely skewed and the negative values, -vely skewed.To confirm this, we can use plots for each columns to visualize the skewness.

# %%
#to visualize skewness for every column,
db.hist(bins=80, figsize=(30,25))


# %% [markdown]
# ## Exploratory Data Analsis

# %%
all = db['Handset Type'].value_counts().head(10)
print(all)
all.plot(kind="pie", title="The top 10 handset used by customers")

# %%
# top 3 handset manufacturers
mode= db['Handset Manufacturer'].mode()
db['Handset Manufacturer'].fillna(mode,inplace=True)
x = db['Handset Manufacturer'].value_counts().head(3)
print(x)
x.plot(kind="pie", title="The top 3 Handset manufacturers");

# %%
#top 5 Huawei handset types
top3 = db.groupby('Handset Manufacturer')['Handset Type'].value_counts()['Huawei'].head(5)
print(top3)
top3.plot(kind="pie" , title=" top 5 Huawei handset")

# %%
#top 5 Apple handset types.
apple = db.groupby('Handset Manufacturer')['Handset Type'].value_counts()['Apple'].head()
print(apple)
apple.plot(kind="pie",  title = 'top 5 Apple handset')

# %%
#top 5 Samsung handset types.
samsung = db.groupby('Handset Manufacturer')['Handset Type'].value_counts()['Samsung'].head()
print(samsung)
samsung.plot(kind="pie", title = 'top 5 Samsung handset')

# %%
handset_manufacturer = db['Last Location Name'].value_counts()
print(len(handset_manufacturer), "users")
print("Number of posts per user")
handset_manufacturer[:3].plot(
    kind='bar', color=['pink', 'purple', 'blue'])


# %% [markdown]
# Aggregate per user the following information in the column  
# number of xDR sessions
# Session duration
# the total download (DL) and upload (UL) data
# the total data volume (in Bytes) during this session for each application
# 

# %%
def aggregation_cols(db,col_1,col_2,trim=False):
    
    grouped = db.groupby(col_1).agg({col_2: [min, max, sum]})  
    grouped.columns = ["_".join(x) for x in grouped.columns.ravel()]
    if trim:
        return grouped.describe()
    return grouped

# %%
aggregation_cols(db,'MSISDN/Number','Bearer Id',True)


# %%
aggregation_cols(db,'MSISDN/Number',"Dur. (ms)",True)


# %%
aggregation_cols(db,'MSISDN/Number','Total UL (Bytes)',True)


# %%
aggregation_cols(db,'MSISDN/Number','Total UL (Bytes)',True)['Total UL (Bytes)_sum']


# %%
aggregation_cols(db,'MSISDN/Number','Total DL (Bytes)',True)


# %%
aggregation_cols(db,'MSISDN/Number','Total DL (Bytes)',True)['Total DL (Bytes)_sum']


# %%
#Check the frequency of user sessions. The results should show a total duration for each user in ms.
sessionsCountData=db['msisdn/number'].value_counts().head()

sessionsCount=sessionsCountData.values.tolist()

msisdn=sessionsCountData.index.values

sessionPerUserDictionary = dict(zip(msisdn, sessionsCount))

print(sessionPerUserDictionary)
db.groupby('msisdn/number')['dur._(ms)'].sum()

# %% [markdown]
# ## Data Formating 

# %%
#Clean the data using Preprocessing script.
preprocess = PreProcess(db)

# %%
db.info()

# %%
db = preprocess.clean_feature_name(db)


# %%
db.columns

# %%


# %% [markdown]
# Since we have a lot of rows, an easy way to deal with the missing values will be to drop the rows with duplicates.

# %%
db = preprocess.drop_duplicates(db)


# %%
# drop columns with more than 30% missing values
db_c, db_before_filling, missing_cols = preprocess.drop_variables(db)


# %%
print(missing_cols)


# %% [markdown]
# Notice that the columns that don't have a count of 150,001 are printed as the missing columns. We then replace these missing values with 

# %% [markdown]
# Since there are numerous missing values and outliers, we replace them will median.

# %%
cols, df_single, num_cols = preprocess.fill_numerical_variables(db)


# %%
print(len(missing_cols))


# %% [markdown]
# ## Data Transformation


