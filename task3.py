#saidali
import time

def decorator_1(func):
    def measure_runningtime(*values, **named_inputs):
        initial_time = time.time() 
        result = func(*values, **named_inputs)  
        recorded_time = time.time()  
        duration = recorded_time - initial_time 
        print(f"{func.__name__} call executed in {duration:.4f} sec") 
        return result
    return measure_runningtime
