import onnx
model = onnx.load('../../Combined/data/DeepFlavour_HLT_12X/model.onnx')
# model = onnx.load('DeepJet_test_online.onnx')
output =[node.name for node in model.graph.output]

input_all = [node.name for node in model.graph.input]
input_initializer =  [node.name for node in model.graph.initializer]
net_feed_input = list(set(input_all)  - set(input_initializer))

print('Inputs: ', net_feed_input)
print('Outputs: ', output)
