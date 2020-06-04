import sys 

def getUserArguments():
    USAGE = "Usage: build.py image=<your-image-stream> name=<service-name>"
    args = sys.argv[1:]

    if not args:
        sys.exit(USAGE)

    ap = [pair.split("=") for pair in args]
    ap = map(lambda n: (n[0], n[1]), ap) 
    ret = dict(ap)
    
    return ret 


