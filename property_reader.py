import configparser


class PropertyReader:
    config = None
    SOURCE_DIR = None
    DEST_DIR = None
    NO_OF_LINES = 0
    FILE_TYPES = None
    SUCCESS_DIR = None
    FAILURE_DIR = None

    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read('config.properties')
        self.read_properties()

    def read_properties(self):
        self.SOURCE_DIR = self.config.get('split.properties', 'SOURCE_DIR')
        self.DEST_DIR = self.config.get('split.properties', 'DEST_DIR')
        self.NO_OF_LINES = self.config.getint('split.properties', 'NO_OF_LINES')
        self.FILE_TYPES = self.config.get('split.properties', 'PROCESSING_FILE_TYPE')
        self.SUCCESS_DIR = self.config.get('split.properties', 'SUCCESS_ARCHIVE_DIR')
        self.FAILURE_DIR = self.config.get('split.properties', 'FAILURE_ARCHIVE_DIR')

    def source_dir(self):
        return self.SOURCE_DIR

    def dest_dir(self):
        return self.DEST_DIR

    def no_of_lines(self):
        return self.NO_OF_LINES

    def file_types(self):
        return self.FILE_TYPES

    def success_dir(self):
        return self.SUCCESS_DIR

    def failure_dir(self):
        return self.FAILURE_DIR
