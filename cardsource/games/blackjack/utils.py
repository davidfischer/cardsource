def game_input(message, values=[]):
    """
    Prompts the user for input with the given message and only accepts the 
    input values in ``values``. If ``values`` is empty, accept anything.
    """

    intxt = ''

    while intxt not in values:
        prompt = '%s '
        if len(values) > 0:
            prompt += '[%s] ' %'/'.join(values)
        intxt = raw_input(prompt %message)

        # accept anything
        if len(values) == 0:
            break

    return intxt
