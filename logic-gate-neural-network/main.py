import first_order_functions as f
import second_order_functions as s
import datasets as d

GATE = d.ORGATE

def logic_gate_neural_network(dataset,number_of_hidden_layers,number_of_repeats,learning_rate):
    number_of_inputs, number_of_outputs = f.analyse_gate(GATE)

    weights = f.createweights(number_of_inputs,number_of_outputs,number_of_hidden_layers)
    weights = [[[(0.3+0.56j), (0.53+0.54j)], [(0.58+0.59j), (0.55+0.51j)]],[[(0.3+0.56j), (0.53+0.54j)], [(0.58+0.59j), (0.55+0.51j)]],[[(0.3+0.56j), (0.53+0.54j)], [(0.58+0.59j), (0.55+0.51j)]], [[(0.15+0.35j), (0.45+0.65j)]]]
    change = f.copy_matrices_form(weights)

    for index_of_repeats in range(0,number_of_repeats):
        for GATE_INDEX in GATE:
            outputs,error = s.produce_outputs_and_end_error(GATE_INDEX,weights)
            error = s.back_propagate_error(error,weights)
            print("error",error)
            print("weights",weights)
            print("output",outputs)
            print("change",change)
            for matrix_index in range(0,len(weights)):
                for matrix_row_index in range(0,len(weights[matrix_index])):
                    for matrix_column_index in range(0,len(weights[matrix_index][matrix_row_index])):
                        change[matrix_index][matrix_row_index][matrix_column_index] = f.change_in_weight(outputs[matrix_index][matrix_column_index],learning_rate,error[matrix_index][matrix_row_index])
            print(change)
            break

        
logic_gate_neural_network(GATE,0,1,0.01)