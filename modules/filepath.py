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

    @staticmethod
    # validate that the file path is for a video
    def read_video_filepath():
        video_extensions = ['.mp4', '.avi', '.mkv', '.mov']

        while True:
            video_filepath = FilePath.read_filepath(
                "Video file path: ")

            file_extension = os.path.splitext(video_filepath)[1].lower()

            # check if the file extension is for a video
            if (file_extension in video_extensions):
                return video_filepath
            else:
                print("This file is not a video. Please try again.")

    @staticmethod
    # validate that the file path is for a srt file
    def read_srt_filepath():
        while True:
            srt_filepath = FilePath.read_filepath(
                "Srt file path: ")

            file_extension = FilePath.get_file_extension(srt_filepath)

            # check if the file extension is .srt
            if (file_extension == ".srt"):
                return srt_filepath
            else:
                print("This file is not a srt file. Please try again.")

    @staticmethod
    # get the file path without the file extension
    def remove_file_extension(file_path):
        return os.path.splitext(file_path)[0]

    @staticmethod
    # get the file extension from the file path
    def get_file_extension(file_path):
        return os.path.splitext(file_path)[1]
