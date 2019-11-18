import configparser

class Configurator:
    config_file = "../../config.ini"

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
