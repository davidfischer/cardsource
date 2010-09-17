def game_input(message, values):
    """
    Prompts the user for input with the given message and only accepts the 
    input values in values
    """
    
    intxt = ''
    
    while intxt not in values:
        intxt = raw_input('%s [%s] ' %(message, '/'.join(values)))
        
    return intxt