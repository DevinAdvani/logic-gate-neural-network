import first_order_functions as f
import second_order_functions as s
import datasets as d

GATE = d.ORGATE

def logic_gate_neural_network(dataset,number_of_hidden_layers):
    number_of_inputs, number_of_outputs = f.analyse_gate(GATE)

    weights = f.createweights(number_of_inputs,number_of_outputs,number_of_hidden_layers)
    transpose_weights = f.transpose_matrices(weights)

    for GATE_INDEX in GATE:
        outputs,error = s.produce_outputs_and_end_error(GATE_INDEX,weights)
        """
        print("o",outputs,"e",error,"w",weights)
        print("space")
        """
        print(weights[1])
        print(error[1])
        print(f.error_back_prop_matrix(f.transpose_matrix([[(0.6+0.2j), (0.1+0.9j)]]),error[1]))
        break
        
logic_gate_neural_network(GATE,1)