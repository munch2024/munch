# %% [markdown]
# # Assignment #3 - Linear Regression Implementation

# %%
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold

data = pd.read_fwf("auto-mpg.data",names=["mpg","cylinders","displacement","horsepower","weight","acceleration","model year","origin","car name"])
data = data.iloc[:,:8]                  # remove car name

# Data preprocessing

# Filling in missing values with average
horsepower = data.iloc[:,3]
sum = 0                                 # sum of valid horsepower values
count = 0                               # count of valid horsepower values
missingValIndices = []                  # list of index locations of invalid horsepower values
for i in range(data.iloc[:,3].shape[0]):# calculate average horsepower
    if horsepower[i] != '?':
        sum += float(horsepower[i])                     # running sum
        count += 1                                      # running count
    else:
        missingValIndices.append(i)
average = sum/count

for i in range(len(missingValIndices)): # replace missing values with average horsepower
    data.at[missingValIndices[i],'horsepower'] = average

data = data.astype('float')                   # cast dataframe to float

def linearRegress(train_indices,test_indices):
    
    foldResults = []                        # to be returned: b coefficients and RMSE
    
    data_train = data.iloc[train_indices]   # train folds
    data_test = data.iloc[test_indices]     # test fold
    raw_yte = data_test.iloc[:,0]           # keep raw values for RMSE
    raw_ytr = data_train.iloc[:,0]          # keep to save mean and std for denormalize predicted value
    
    scaler = StandardScaler()

    # Normalize train data
    scaledDatatr = pd.DataFrame(scaler.fit_transform(data_train))
    # Normalize test data using u and s from training normalization
    scaledDatate = pd.DataFrame(scaler.transform(data_test))

    # Split train and test data into respective X's
    Xtr = scaledDatatr.iloc[:,1:8]
    Xte = scaledDatate.iloc[:,1:8]

    # Prepend a column of 1s to Xtr and Xte to prepare for calculations
    temp = np.empty(Xtr.shape[0])              
    temp.fill(1)
    temp = pd.DataFrame(temp,columns=list('h'))
    Xtr1 = pd.concat([temp,Xtr],axis=1)
    temp = np.empty(Xte.shape[0])              
    temp.fill(1)
    temp = pd.DataFrame(temp,columns=list('h'))
    Xte1 = pd.concat([temp,Xte],axis=1)

    Xt = Xtr1.transpose()                       # transposed X, for calculation
    # Calculate coefficients using the normal equation
    inverse_product = np.linalg.inv(np.dot(Xt, Xtr1))
    # Coefficients (b) are obtained by multiplying the inverse of (X^T * X) with X^T and then with raw_ytr
    b = np.dot(np.dot(inverse_product, Xt), raw_ytr)
    foldResults.extend(b[1:8])                  # save coefficients to fold results

    # Predict y
    yHat = np.dot(Xte1,b)                       # ŷ = Xb
    raw_yte = raw_yte.to_numpy()                # make compatible for matrix operation
    
    # Calculate RMSE
    squared_diff = np.square(raw_yte - yHat)
    # Mean Squared Error (MSE) is the sum of squared differences divided by the number of samples
    mse = np.sum(squared_diff) / raw_yte.shape[0]
    # RMSE is the square root of MSE
    rmse = np.sqrt(mse)
    foldResults.append(rmse)                    # save RMSE

    return foldResults
    
    


# %%
# K-Fold Cross Validation

results = []
foldLabel = pd.DataFrame(data=["Fold 1", "Fold 2", "Fold 3", "Fold 4", "Fold 5", "Fold 6", "Fold 7", "Fold 8", "Fold 9", "Fold 10"],columns=["folds"])  # Fold labels

kf = KFold(n_splits=10) # K fold splits (10 Fold)
for train_index, test_index in kf.split(data):
    results.extend(linearRegress(train_index, test_index))

# Format results# Reshape results array and create a DataFrame
results_shape = (10, 8)
results_reshaped = np.reshape(results, results_shape)
# Define column names for the DataFrame
columns = ["cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin", "RMSE"]
# Create a DataFrame with reshaped results and appropriate column names
results_df = pd.DataFrame(results_reshaped, columns=columns)
results_df





# %%
