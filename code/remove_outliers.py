import numpy as np

def RM_Outliers(data, threshold):
    new_data = data.copy()
    
    copy_data = np.append(data, data[-1])#padding 1 point for diff
    
    new_data[np.abs(np.diff(copy_data))>threshold] = None
    
    return new_data
    