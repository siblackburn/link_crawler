import requests #to get info back from url
import json
from pprint import pprint
import argparse


class Uri():
    def __init__(self, scheme: str, host: str, port: int, path: str, params: dict, fragment_identifier: dict):
        self.__scheme = scheme
        self.__host = host
        self.__port = port
        self.__path = path
        self.__params = params
        self.__fragment_identifier = fragment_identifier

    @staticmethod
    def new():
        return URIbuilder()

    def to_string(self):
        parameter_string = '&'.join([f'{k}={v}' for k, v in self.__params.items()])
        if len(parameter_string) > 0:
            parameter_string = '?' + parameter_string

        fragment_string = '&'.join([f'{k}={v}' for k, v in self.__fragment_identifier.items()])
        if len(fragment_string) > 0:
            fragment_string = '#' + fragment_string

        port_string = f':{self.__port}'

        return f'{self.__scheme}://{self.__host}{port_string}/{self.__path or ""}{parameter_string or ""}{fragment_string or ""}'

    def get_request(self):
        base_url = Uri.to_string(self)
        response = requests.get(base_url)
        data = response.json()
        return json.dumps(data, indent=1)

class URIbuilder():

    def __init__(self, scheme="https", host=None, port=None, path=None, params={}, fragment_identifier={}):
        self.scheme = scheme
        self.host = host
        self.port = port
        self.path = path
        self.params = params
        self.fragment_identifier = fragment_identifier

    def with_scheme(self, scheme):
        return URIbuilder(scheme, host=self.host, port=self.port, path=self.path, params=self.params, fragment_identifier=self.fragment_identifier)

    def with_host(self, host):
        return URIbuilder(scheme=self.scheme, host=host, port=self.port, path=self.path, params=self.params, fragment_identifier=self.fragment_identifier)

    def with_port(self, port):
        return URIbuilder(scheme=self.scheme, host=self.host, port=port, path=self.path, params=self.params, fragment_identifier=self.fragment_identifier)

    def with_path(self, path):
        return URIbuilder(scheme=self.scheme, host=self.host, port=self.port, path=path, params=self.params, fragment_identifier=self.fragment_identifier)

    def with_params(self, key, value):
        new_params = dict(self.params, **{key: value})
        return URIbuilder(scheme=self.scheme, host=self.host, port=self.port, path=self.path, params=new_params, fragment_identifier=self.fragment_identifier)

    def with_fragment(self, key, value):
        fragment = dict(self.fragment_identifier, **{key: value})
        return URIbuilder(scheme=self.scheme, host=self.host, port=self.port, path=self.path, params=self.params, fragment_identifier=fragment)

    def to_url(self):
        return Uri(self.scheme, self.host, self.port, self.path, self.params, self.fragment_identifier)

'''
A couple of quick tests to ensure the uri builder is functioning properly
'''
# test = Uri.new().with_scheme("http").with_host("google.com").with_params("hi", "world").with_fragment("row", "4").to_url()
# print(test.to_string())

# test2 = Uri.new().with_scheme("http").with_host("demo.codingnomads.co").with_port(8080).with_path("/tasks_api/users").to_url()
# print(test2.to_string())
#
# output = Uri.get_request(test2)
# print(output)


'''
arg parser to make program work with command line. To use command line
1) Navigate to folder
2) run $ python uri_builder.py --scheme x --host x --port x --path x 
'''
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description="Welcome to my url tool!")
#     parser.add_argument("--scheme", default=None, type=str)
#     parser.add_argument("--host", default=None, type=str)
#     parser.add_argument("--port", default=None, type=int)
#     parser.add_argument("--path", default=None, type=str)
#     # parser.add_argument("--parameters", default=None, type=json.loads)
#     # parser.add_argument("--fragment", default=None, type=json.loads)
#     args = parser.parse_args()
#     # print(args)
#
#     output_url = Uri.new().with_scheme(args.scheme).with_host(args.host).with_port(args.port).with_path(args.path).to_url()
#     output = Uri.get_request(output_url)
#     print(output)
