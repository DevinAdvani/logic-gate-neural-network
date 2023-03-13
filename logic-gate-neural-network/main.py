import first_order_functions as f
import second_order_functions as s
import datasets as d

GATE = d.ORGATE

def logic_gate_neural_network(dataset,number_of_hidden_layers):
    number_of_inputs, number_of_outputs = f.analyse_gate(GATE)

    weights = f.createweights(number_of_inputs,number_of_outputs,number_of_hidden_layers)

    for GATE_INDEX in GATE:
        outputs,error = s.produce_outputs_and_end_error(GATE_INDEX,weights)
        print("o",outputs,"e",error,"w",weights)
        print("space")
        for back_prop_index in range(len(weights)-1,0,-1):
            print(back_prop_index)
        
logic_gate_neural_network(GATE,1)

"hey"