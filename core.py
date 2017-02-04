import json

import re

import requests

from extractors import extract_dict_from_raw_headers, extract_dict_from_raw_mode_data, format_dict


class CaseInsensitiveDict(dict):
    def __setitem__(self, key, value):
        super(CaseInsensitiveDict, self).__setitem__(key.upper(), value)

    def __getitem__(self, key):
        return super(CaseInsensitiveDict, self).__getitem__(key.upper())

    def update(self, d=None, **kwargs):
        d = d or {}
        for k, v in d.items():
            self[k] = v


class PostPython:
    def __init__(self, postman_collection_file_path):
        with open(postman_collection_file_path) as postman_collection_file:
            self.__postman_collection = json.load(postman_collection_file)

        self.__folders = {}
        self.environments = CaseInsensitiveDict()
        self.load()

    def load(self):
        id_to_request = {}
        for req in self.__postman_collection['requests']:
            id_to_request[req['id']] = req

        for fol in self.__postman_collection['folders']:
            requests_list = {}

            for req_id in fol['order']:
                req_data = id_to_request[req_id]
                requests_list[normalize_func_name(req_data['name'])] = PostRequest(self, req_data)

            col_name = normalize_class_name(fol['name'])
            self.__folders[col_name] = PostCollection(col_name, requests_list)

    def __getattr__(self, item):
        if item in self.__folders:
            return self.__folders[item]
        else:
            raise AttributeError('%s folder does not exist in Postman collection.' % item)

    def help(self):
        print('Collection:')
        for fol in self.__folders.values():
            fol.help()


class PostCollection:
    def __init__(self, name, requests_list):
        self.name = name
        self.__requests = requests_list

    def __getattr__(self, item):
        if item in self.__requests:
            return self.__requests[item]
        else:
            raise AttributeError('%s request does not exist in %s folder.' % (item, self.name))

    def help(self):
        print(self.name)
        for req in self.__requests.keys():
            print('\t', req)


class PostRequest:
    def __init__(self, post_python, data):
        self.post_python = post_python
        self.request_kwargs = dict()
        self.request_kwargs['url'] = data['url']
        if data['dataMode'] == 'raw' and 'rawModeData' in data:
            self.request_kwargs['json'] = extract_dict_from_raw_mode_data(data['rawModeData'])
        self.request_kwargs['headers'] = extract_dict_from_raw_headers(data['headers'])
        self.request_kwargs['method'] = data['method']

    def __call__(self, *args, **kwargs):
        formatted_kwargs = format_dict(self.request_kwargs, self.post_python.environments)
        print(self.request_kwargs)
        print(formatted_kwargs)
        return requests.request(**formatted_kwargs)


def normalize_class_name(string):
    string = re.sub(r'[!@#$%^&*()_\-+=,./\'\\\"|:;{}\[\]]', ' ', string)
    return string.title().replace(' ', '')


def normalize_func_name(string):
    string = re.sub(r'[!@#$%^&*()_\-+=,./\'\\\"|:;{}\[\]]', ' ', string)
    return '_'.join(string.lower().split())
