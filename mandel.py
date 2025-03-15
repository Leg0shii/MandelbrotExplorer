
def is_diverging(c) -> int:
    MAX_ITERATIONS = 50
    THRESHOLD = 2

    new_z = complex(0,0)

    try:
        for iteration_number in range(MAX_ITERATIONS):
            if abs(new_z) >= THRESHOLD:
                return iteration_number
            
            new_z = new_z**2 + c
        
        return 0
    except:
        return 0
