def format_string_to_list(text) -> list:
    '''
    '''
    return text.splitlines()

def format_string_to_dict(text) -> dict:
    '''
    '''
    new_dict = {}
    for b in range(len(text)):
        new_dict[b] = text[b]
    return new_dict

