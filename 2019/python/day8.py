from aoc_lib import file_utils


if __name__ == '__main__':
    raw_in = file_utils.read_file_into_str('inputs/day8input.txt')

    width, height = 25, 6

    layers = [
    	[
    		list(map(int, list(raw_layer[w*width:(w+1)*width]))) 
    		for w in range(len(raw_layer)//width)
    	] 
    	for raw_layer in [
	    	raw_in[l_index*(width*height):(l_index+1)*(width*height)] 
	    	for l_index in range(len(raw_in)//(width*height))
	    ]
    ]

    zero_layer_index = 0
    min_zero_count = width*height
    for index, layer in enumerate(layers):
    	zero_count = sum([row.count(0) for row in layer])
    	if zero_count < min_zero_count:
    		zero_layer_index = index
    		min_zero_count = zero_count

    zero_layer = layers[zero_layer_index]

    print(f'Part 1: {sum([row.count(1) for row in zero_layer])*sum([row.count(2) for row in zero_layer])}')

    final_layer = []

    for h in range(height):
    	row = []
    	for w in range(width):
    		for layer in layers:
    			if layer[h][w] == 2:
    				continue
    			else:
    				row.append(layer[h][w])
    				break
    	final_layer.append(row)

    print('Part 2:')
    picture = [''.join(map(lambda x: '#' if x==1 else '.', row)) for row in final_layer]
    for r in picture:
    	print(r)


