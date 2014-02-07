

def retrieve_param(request, param_name, default=None, method="GET"):
    if method not in ("GET", "POST"): raise AttributeError("Only accepted GET or POST")
    
    source = getattr(request, method)
    if param_name in source and source[param_name] is not None:
        return source[param_name]
    return default
    