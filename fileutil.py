import os
from pathlib import Path
import shutil


class Fileutil:

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

    def files_to_process(self,directory):
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(directory):
            for file in f:
                input_path, input_f = os.path.split(file)
                new_file_ext = input_f.split(".")[1]
                if new_file_ext in file:
                    files.append(os.path.join(r, file))
        return files

    def create_dir(self, directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
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

    def move_file(self, original, target):
        try:
            shutil.move(original, target)
        except OSError as e:
            raise
