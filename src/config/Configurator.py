import configparser
import os
from pathlib import Path

class Configurator:
    cwd = os.getcwd()
    parent_dir = Path(cwd).parent.parent
    config_path = os.path.abspath(str(parent_dir))
    file = '/config.ini'
    config_file = config_path + file

    @staticmethod
    def get_config(section):
        config = configparser.ConfigParser()
        config.read(Configurator.config_file)
        d = dict(config.items(section))
        return d

    @staticmethod
    def show_config():
        config = configparser.ConfigParser()
        config.read(Configurator.config_file)
        for section_name in config.sections():
            print('Section:', section_name)
            print('  Options:', config.options(section_name))
            for name, value in config.items(section_name):
                print('  {} = {}'.format(name, value))
            print()

    @staticmethod
    def get(section, line):
        config = configparser.ConfigParser()
        config.read(Configurator.config_file)
        d = dict(config.items(section))
        return d.get(line)
