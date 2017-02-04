import json


def extract_dict_from_raw_mode_data(raw):
    try:
        return json.loads(raw)
    except json.decoder.JSONDecodeError:
        return {}


def extract_dict_from_raw_headers(raw):
    d = {}
    for header in raw.split('\n'):
        try:
            key, value = header.split(': ')
            d[key] = value
        except ValueError:
            continue

    return d


def format_dict(d, key_values):
    kwargs = {}
    for k, v in d.items():
        if isinstance(v, str):
            try:
                formatted = v.replace('{{', '{').replace('}}', '}').format(**key_values)
            except KeyError as e:
                raise KeyError("Except value %s in PostPython environment variables.\n Environment variables are %s" % (e, key_values))
            kwargs[k] = formatted
        elif isinstance(v, dict):
            kwargs[k] = format_dict(v, key_values)
        else:
            raise NotImplementedError('no format is developed for type %s. E' % type(v))
    return kwargs
