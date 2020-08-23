import os
from fileutil import Fileutil
from error_handler import ErrorHandler
from property_reader import PropertyReader


class FileSplit:
    property_reader = None
    futil = None

    def __init__(self):
        self.property_reader = PropertyReader()
        self.futil = Fileutil()

    def split(self):
        SOURCE_DIR = self.property_reader.source_dir()
        DEST_DIR = self.property_reader.dest_dir()
        NO_OF_LINES = self.property_reader.no_of_lines()
        files = self.futil.files_to_process(SOURCE_DIR)
        for input_file in files:
            self.process(input_file, DEST_DIR, NO_OF_LINES)

    def process(self, input_file, output_dir, lines_per_file):
        head = self.futil.get_header(input_file)
        self.file_split(input_file, output_dir, lines_per_file, head)

    def file_split(self, input_file, output_dir, lines_per_file, header):
        smallfile = None
        try:
            input_path, input_f = os.path.split(input_file)
            new_file_name = input_f.split(".")[0]
            new_file_ext = input_f.split(".")[1]
            file_types = self.property_reader.file_types()
            file_type_extn = file_types.split(",")
            if new_file_ext in file_type_extn:
                new_output_dir = output_dir + "/" + new_file_name
                success_dir = self.property_reader.success_dir()
                success_file = success_dir + "/" + input_f
                self.futil.create_dir(new_output_dir)
                self.futil.create_dir(success_dir)
                filecount = 0
                with open(input_file) as bigfile:
                    for line_number, line in enumerate(bigfile):
                        if line_number % lines_per_file == 0:
                            if smallfile:
                                smallfile.close()
                                filecount = filecount + 1
                            small_filename = (new_file_name + '_{}.' + new_file_ext).format(filecount)
                            smallfile = open(new_output_dir + "/" + small_filename, "w")
                        if line_number % lines_per_file == 0:
                            smallfile.write(header)
                        if line_number > 0:
                            smallfile.write(line)
                    if smallfile:
                        smallfile.close()
                self.futil.move_file(input_file, success_file)
            else:
                print("file extension not supported")

        except:
            failure_dir = self.property_reader.failure_dir()
            failure_file = failure_dir + "/" + input_f
            eh = ErrorHandler()
            eh.error_handle(new_output_dir, failure_file, input_file)
            pass


fs = FileSplit()
fs.split()
