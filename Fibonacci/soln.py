def fib(n):
    
    def fibonacci(key, track):
        
        # improve dp - memoization
        if key in track:
            return track[key]
        
        # base case(s)
        if key < 0 or key == 0:
            return 0
        
        elif key == 1:
            return 1
        
        #                first preceding number +    second preceding number 
        track[key] = fibonacci(key-1, track) + fibonacci(key-2, track)
        
        return track[key]
    
    
    return fibonacci(n, {})