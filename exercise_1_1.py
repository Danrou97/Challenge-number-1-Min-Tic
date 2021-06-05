def expresion_intercambio(a:int, b: int, c: int, d: int, e: int, f:int ) ->float:

    x=(a+(b/c))/(d+(e/f))
    
    y=a-(b/(c-d))
    
    z=x
    x=y
    y=z
    str(x)
    str(y)
    return x, y




