import os


class FilePath:

    @staticmethod
    def read_filepath(message):
        while True:
            file_path = input(message)

            # check if the file exists
            if os.path.exists(file_path):
                return file_path
            else:
                print("Invalid path. Please try again.")
