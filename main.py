def main(S, d):

    a=(S-d**2)/2*d
    b=a+d
    x=b-a*a/2*b
    '''create a babylonian function.
    
    Args:
        S (int): number
        d (int): numnber
        
        
    Returns:
        float: result
    '''
    return float(x)
S=16
d=4
print(main(16,4))