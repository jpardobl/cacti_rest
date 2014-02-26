import hashlib, time, random, math

def microtime(get_as_float = False) :
    if get_as_float:
        return time.time()
    else:
        return '%f %d' % math.modf(time.time())

def retrieve_param(request, param_name, default=None, method="GET"):
    if method not in ("GET", "POST"): raise AttributeError("Only accepted GET or POST")
    
    source = getattr(request, method)
    if param_name in source and source[param_name] is not None:
        return source[param_name]
    return default
    
def generate_hash(request):
    m = hashlib.md5()
    
    #m.update(request.session._session_key)
    m.update(microtime())
    m.update(str(random.randint(0,1000)))
    return m.hexdigest()