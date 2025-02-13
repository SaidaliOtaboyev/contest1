#Saidali
def typeBasedTransformer(**argumentdetails):
    converteddata = {} 
    
    for identifier, data in argumentdetails.items():  
        if isinstance(data, (int, float)):
            converteddata[identifier] = data ** 2  
            
        elif isinstance(data, str):
            converteddata[identifier] = data[::-1]  
            
        elif isinstance(data, bool):
            converteddata[identifier] = not bool(data)            
        elif isinstance(data, (list, tuple)):
            converteddata[identifier] = data[::-1]  
            
        elif isinstance(data, dict):
            converteddata[identifier] = {v: k for k, v in data.items()}  
            
        else:
            converteddata[identifier] = data  
    
    return converteddata  
