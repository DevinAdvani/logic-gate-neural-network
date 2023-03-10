import numpy as np

def createweight(number_of_rows,number_of_columns):
    return np.random.normal(0.5,1/20,(number_of_rows,number_of_columns))

def createcomplexweight(number_of_rows,number_of_columns):
    return createweight(number_of_rows,number_of_columns) + 1j * createweight(number_of_rows,number_of_columns)

def createcomplexweights(number_of_inputs,number_of_outputs,number_of_hidden_layers):
    output = []
    for i in range(0,number_of_hidden_layers):
        output.append(createcomplexweight(number_of_inputs,number_of_inputs))
    output.append(createcomplexweight(number_of_inputs,number_of_outputs))
    return output

