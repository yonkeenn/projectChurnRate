
# detecting Outlier
# Inter Quartile Range is the distance between the 3rd Quartile and the first Qartile

def detect_outlier(X):
    """
    X: dataframe
    """
    #X = df_new.iloc[:, :-1]
    #for i in range(len(X.columns)):
    for i in range(5): # Only priny the firs 5
        first_q = np.percentile(X[X.columns[i]], 25)
        third_q = np.percentile(X[X.columns[i]], 75) 
        IQR = 1.5*(third_q - first_q)
        minimum = first_q - IQR 
        maximum = third_q + IQR
        
        if(minimum > np.min(X[X.columns[i]]) or maximum < np.max(X[X.columns[i]])):
            print(X.columns[i], "There is Outlier")

# 1. Removing outliers
def remove_outlier(X):
    """
    X: dataframe
    """
    #X = df_new.iloc[:, :-1]
    for i in range(len(X.columns)):
        first_q = np.percentile(X[X.columns[i]], 25)
        third_q = np.percentile(X[X.columns[i]], 75) 
        IQR = 1.5*(third_q - first_q)
        minimum = first_q - IQR 
        maximum = third_q + IQR
    
        median = X[X.columns[i]].median()
    
        X.loc[X[X.columns[i]] < minimum, X.columns[i]] = median 
        X.loc[X[X.columns[i]] > maximum, X.columns[i]] = median