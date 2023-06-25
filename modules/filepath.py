import os

class FilePath:
    @staticmethod
    def sanitize_filepath(file_path):

        file_path = file_path.strip("&")

        # Remove leading and trailing whitespace
        file_path = file_path.strip()

        # Remove leading and trailing quotes
        file_path = file_path.strip("'\"")

        return file_path

    @staticmethod
    def read_filepath(message):
        while True:
            file_path = input(message)
            file_path = FilePath.sanitize_filepath(file_path)

            # check if the file exists
            if os.path.exists(file_path):
                return file_path
            else:
                print("Invalid path. Please try again.")
