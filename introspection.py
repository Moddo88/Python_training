def introspection_info(obj):
    obj_type = type(obj).__name__


    attributes = [at for at in dir(obj) if not callable(getattr(obj, at))]
    methods = [m for m in dir(obj) if callable(getattr(obj, m))]


    module = getattr(obj.__class__, '__module__', None)


    doc = getattr(obj, '__doc__', None)


    dict_int = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
        'doc': doc
    }

    return dict_int

# Пример использования
number_info = introspection_info(42)
print(number_info)
