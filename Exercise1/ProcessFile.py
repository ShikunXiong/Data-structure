def processLine(str):
    """
    Process row Line
    :param str: A line sentence
    :return: List contains " "
    """
    tmp = list(str)
    result = ""
    for i in range(len(tmp)):
        if tmp[i].isalnum() is False:
            tmp[i] = " "
    for i in tmp:
        result += i
    return result.split(" ")


