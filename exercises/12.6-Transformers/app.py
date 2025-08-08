incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]

# Your code here
def data_transformer(input_list):
    new_list = list(map(lambda item: f'{item["name"]} {item["last_name"]}', input_list))
    return new_list


print(data_transformer(incoming_ajax_data))