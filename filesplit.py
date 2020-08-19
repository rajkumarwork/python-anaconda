import os
from pathlib import Path
import shutil


class FileSplit:

    def split(self, input_file, output_dir, lines_per_file):
        head = self.get_header(input_file)
        self.file_split(input_file, output_dir, lines_per_file, head)

    def get_header(self, file):
        f = None
        h = None
        try:
            f = open(file, 'r')
            h = f.readline()
        except OSError as e:
            print("Input file not found !")
        finally:
            if f:
                f.close()
        return h

    def create_dir(self, directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError as e:
            raise

    def move_file(self, original, target):
        try:
            shutil.move(original, target)
        except OSError as e:
            raise

    def remove_dir(self, directory):
        try:
            directory = Path(directory)
            for item in directory.iterdir():
                if item.is_dir():
                    self.remove_dir(item)
                else:
                    item.unlink()
            directory.rmdir()
        except OSError as e:
            raise

    def file_split(self, input_file, output_dir, lines_per_file, header):
        smallfile = None
        try:
            input_path, input_f = os.path.split(input_file)
            new_file_name = input_f.split(".")[0]
            new_file_ext = input_f.split(".")[1]
            new_output_dir = output_dir + new_file_name
            success_file = new_output_dir + "/success/" + input_f
            self.create_dir(new_output_dir)
            self.create_dir(new_output_dir + "/success")
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

            #self.move_file(input_file, success_file)

        except:
            print("File split issue")
            self.remove_dir(new_output_dir)
            pass


#fs = FileSplit()
#fs.split("/tmp/test_split_file3/innovators_19_8_20.csv", "/tmp/test_split_file5/", 10)
