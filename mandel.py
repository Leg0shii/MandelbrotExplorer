
def is_diverging(c) -> bool:
    MAX_ITERATIONS = 10 
    THRESHOLD = 10

    new_z = complex(0,0)

    try:
        for _ in range(MAX_ITERATIONS):
            new_z = new_z**2 + c

        if abs(new_z) >= THRESHOLD:
            return True
        else: 
            return False
        
    except:
            return True
