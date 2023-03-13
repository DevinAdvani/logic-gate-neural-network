def createweight(numberofrows,numberofcolumns):
    output = []
    outputrow = []
    for index_of_columns in range(0,numberofcolumns):
        outputrow.append(0.5 + 0.5j)
    for index_of_rows in range(0,numberofrows):
        output.append(outputrow)
    return output

def createweights(numberofinputs,numberofoutputs,numberofhiddenlayers):
    output = []
    for i in range(0,numberofhiddenlayers):
        output.append(createweight(numberofinputs,numberofinputs))
    output.append(createweight(numberofoutputs,numberofinputs))
    return output

def multiply(weight,input):
    output = []
    for i in range(0,len(weight)):
        sum = 0
        for k in range(0,len(weight[0])):
            sum += weight[i][k].imag * ( weight[i][k].real * (-input[k] + 1) + (1 - weight[i][k].real) * input[k])
            if sum >= 1:
                break
        if sum >= 1:
            output.append(1)
        else:
            output.append(sum)
    return output

def convert_text_to_list(data):
    output = []
    for index in range(0,len(data)):
        output.append(int(data[index]))
    return output

def propagate_signals(weights,input):
    output = [input]
    for weight_index in range(0,len(weights)):
        output.append(multiply(weights[weight_index],output[-1]))
    return output

def create_list_of_zeros_of_length_n(n):
    output = []
    for i in range(0,n):
        output.append(0)
    return output

def copy_list_form(list_to_be_copied):
    copy = []
    for i in range(0,len(list_to_be_copied)):
        copy.append(create_list_of_zeros_of_length_n(len(list_to_be_copied[i])))
    return copy

def minus_one_list_from_another(A,B):# A - B
    output = []
    for i in range(0,len(A)):
        output.append(A[i]-B[i])
    return output

def analyse_gate(gate):
    num_of_inputs = len(gate[0][0])
    num_of_outputs = len(gate[0][1])
    return num_of_inputs, num_of_outputs

def single_error_back_prop(singular_weight,error_at_k):
    error_at_j = singular_weight.imag * (1 - 2 * singular_weight.real) * error_at_k
    return error_at_j

def error_back_prop_matrix()

def change_in_imaginary_weight(learning_rate,error_at_k):
    if -error_at_k > 0:
        return learning_rate
    else:
        return -learning_rate
    
def change_in_real_weight(input,learning_rate,error_at_k):
    if error_at_k * (2 * input - 1) > 0:
        return learning_rate
    else:
        return -learning_rate
    
def change_in_weight(input,learning_rate,error_at_k):
    return change_in_real_weight(input,learning_rate,error_at_k) + 1j * change_in_imaginary_weight(learning_rate,error_at_k)