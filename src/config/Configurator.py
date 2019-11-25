import configparser
import os

class Configurator:
    cwd = os.getcwd()
    #config_file = r'../FACEID/config.ini'
    # TODO fix this path error for tests so it gets:
    config_file = r'/home/maik/FaceID/FACEID/config.ini'

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
