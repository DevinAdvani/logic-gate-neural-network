import first_order_functions as f 

def produce_outputs_and_end_error(single_piece_of_gate_data,weights):
    inputs_before_conversion = single_piece_of_gate_data[0]
    expected_before_conversion = single_piece_of_gate_data[1]
    input = f.convert_text_to_list(inputs_before_conversion)
    expected = f.convert_text_to_list(expected_before_conversion)
    outputs = f.propagate_signals(weights,input)
    error = f.copy_list_form(outputs)
    final_output = outputs[-1]
    error[-1] = f.minus_one_list_from_another(final_output,expected)
    outputs.remove(outputs[0])
    error.remove(error[0])
    return outputs,error

def back_propagate_error(error,weights):
    for back_prop_index in range(0,len(error)-1):
        error[len(error)-2-back_prop_index] = f.error_back_prop_matrix(f.transpose_matrix(weights[-(back_prop_index+1)]),error[-(back_prop_index+1)])
    return error