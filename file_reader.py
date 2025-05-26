

def read_data(file):
    list_of_data = []
    with open(file, 'r') as f:

        for line in f.readlines():
            sentence = line.strip().split(',')
            sentence_tuple = tuple(sentence)
            list_of_data.append(sentence_tuple)
    
    return list_of_data




def read_data(file):
    list_of_data = []
    with open(file, 'r') as f:

        for line in f.readlines():
            sentence = line.strip().split(',')
            sentence_tuple = tuple(sentence)
            list_of_data.append(sentence_tuple)
    
    return list_of_data
 