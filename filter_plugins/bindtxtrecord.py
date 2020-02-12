from jinja2 import Environment, Undefined

def bindtxtrecord(txt):
    if txt is None or isinstance(txt, Undefined):
        return txt

    maxlen = 250

    if len(txt) < maxlen:
        return "\"" + txt + "\""

    curlen = 0

    splittxt = [txt[curlen-maxlen:curlen] for curlen in range(maxlen, len(txt)+maxlen,maxlen)]
    sep = '\" \"'
    merged = "( \"" + sep.join(splittxt) + "\" )"
    return merged

# ...

class FilterModule(object):
    """Filters for long bind txt records"""

    filter_map = {
        'bindtxtrecord': bindtxtrecord
    }

    def filters(self):
        return self.filter_map

