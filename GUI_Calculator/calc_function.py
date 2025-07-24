import re
import shared_variables

def remove_leading_zeros(string):
    return re.sub(r'(?<![\d.])0+(?=\d+)', '', string)
    
def division():
    if(shared_variables.calculation != "None"):
        shared_variables.calculation += "/"
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation
    else:
        shared_variables.calculation="0"
        shared_variables.value.set(shared_variables.calculation+ "/")
        return shared_variables.calculation
    
def seven():
    if(shared_variables.calculation != "None"):
        shared_variables.calculation += "7"
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation
    else:
        shared_variables.calculation="7"
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation

def eight():
    if(shared_variables.calculation != "None"):
        shared_variables.calculation += "8"
        shared_variables.value.set(shared_variables.calculation)
    else:
        shared_variables.calculation="8"
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation

def nine():
    if(shared_variables.calculation != "None"):
        shared_variables.calculation += "9"
        shared_variables.value.set(shared_variables.calculation)
    else:
        shared_variables.calculation="9"
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation

def times():
    if(shared_variables.calculation != "None"):
        shared_variables.calculation += "*"
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation
    else:
        shared_variables.calculation = "0"
        shared_variables.value.set(shared_variables.calculation + "*")
        return shared_variables.calculation
    
def four():
    if(shared_variables.calculation != "None"):
        shared_variables.calculation += "4"
        shared_variables.value.set(shared_variables.calculation)
    else:
        shared_variables.calculation="4"
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation

def five():
    if(shared_variables.calculation != "None"):
        shared_variables.calculation += "5"
        shared_variables.value.set(shared_variables.calculation)
    else:
        shared_variables.calculation="5"
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation

def six():
    if(shared_variables.calculation != "None"):
        shared_variables.calculation += "6"
        shared_variables.value.set(shared_variables.calculation)
    else:
        shared_variables.calculation="6"
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation

def minus():
    if(shared_variables.calculation != "None"):
        shared_variables.calculation += "-"
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation
    else:
        shared_variables.calculation="-"
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation
    
def one():
    if(shared_variables.calculation != "None"):
        shared_variables.calculation += "1"
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation
    else:
        shared_variables.calculation="1"
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation

def two():
    if(shared_variables.calculation != "None"):
        shared_variables.calculation += "2"
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation
    else:
        shared_variables.calculation="2"
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation

def three():
    if(shared_variables.calculation != "None"):
        shared_variables.calculation += "3"
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation
    else:
        shared_variables.calculation="3"
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation

def plus():
    if(shared_variables.calculation != "None"):
        shared_variables.calculation += "+"
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation
    else:
        shared_variables.calculation="+"
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation

def dot():
    if(shared_variables.calculation != "None"):
        test = shared_variables.calculation
        test += "."
        if(float(eval(test)) != SyntaxError and shared_variables.calculation[-1] != "."):
            shared_variables.calculation += "."
            shared_variables.value.set(shared_variables.calculation)
            return shared_variables.calculation
        else:
            return shared_variables.calculation
    else:
        shared_variables.calculation="0."
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation

def zero():
    if(shared_variables.calculation != "None"):
        shared_variables.calculation += "0"
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation
    else:
        shared_variables.calculation="0"
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation 

def equal():
    right_par_count = 0
    left_par_count = 0
    
    if(shared_variables.calculation != "None"):
        if(shared_variables.calculation[0] == "0"):
            shared_variables.calculation = shared_variables.calculation.replace(shared_variables.calculation[0], "")
            equal()
            
        for i in range(len(shared_variables.calculation)):
            if(shared_variables.calculation[i] == "("):
                left_par_count += 1
            elif(shared_variables.calculation[i] == ")"):
                right_par_count += 1
                
        
        for i in range(len(shared_variables.calculation)):
            if(shared_variables.calculation[i] == "("):
                if(i > 0 and (shared_variables.calculation[i-1].isdigit() == True)):
                        shared_variables.calculation = shared_variables.calculation[:i] + "*" + shared_variables.calculation[i:]
                        
        if(left_par_count > right_par_count):
            for i in range(left_par_count - right_par_count):
                shared_variables.calculation += ")"  
                
        shared_variables.calculation = remove_leading_zeros(shared_variables.calculation)
        
        shared_variables.prev_cal = shared_variables.calculation
        shared_variables.value.set(shared_variables.calculation)
        result = round(float(eval(shared_variables.calculation)), 3)
        shared_variables.calculation = str(result)
        shared_variables.value.set(shared_variables.calculation)
        shared_variables.prev_result.set(shared_variables.prev_cal + " = " + shared_variables.calculation)
        shared_variables.calculation = "None"
        
    else:
        shared_variables.calculation="0"
        shared_variables.value.set(shared_variables.calculation)
        return round(float(eval(shared_variables.calculation)), 3)
    
def AllClear():
    shared_variables.calculation = "None"
    shared_variables.value.set(shared_variables.calculation )
    return shared_variables.calculation 

def left_par():
    if (shared_variables.calculation == "None"):
        shared_variables.calculation = "("
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation 
    else:
        shared_variables.calculation += "("
        shared_variables.value.set(shared_variables.calculation)
        return shared_variables.calculation 

def right_par():
    right_par_count = 0
    left_par_count = 0
    if(shared_variables.calculation == "None"):
        shared_variables.calculation = "("
    for i in range(len(shared_variables.calculation)):
        if(shared_variables.calculation[i] == "("):
            left_par_count += 1
        elif(shared_variables.calculation[i] == ")"):
            right_par_count += 1
    if(left_par_count > right_par_count):
        shared_variables.calculation += ")"
    shared_variables.value.set(shared_variables.calculation)
    return shared_variables.calculation 

def percent():
    if (shared_variables.calculation == "None"):
        shared_variables.calculation = "0/100"
    else:
        shared_variables.calculation += "/100"
    shared_variables.value.set(shared_variables.calculation)
    return shared_variables.calculation 