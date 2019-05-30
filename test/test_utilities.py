from yaml import load, FullLoader
from os.path import abspath, dirname, join

templates_root = abspath(join(dirname(dirname(__file__)), "templates", "yml"))


def get_path(root, filepath):
    return abspath(join(root, filepath))


def parse_template_yaml_file(filepath):
    return load(open(get_path(templates_root, filepath), "r"), Loader=FullLoader)
