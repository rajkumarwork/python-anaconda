class ErrorHandler:

    def error_handle(self,new_output_dir,failure_file,input_file):
        print("File split issue")
        self.futil.remove_dir(new_output_dir)
        self.futil.move_file(input_file, failure_file)