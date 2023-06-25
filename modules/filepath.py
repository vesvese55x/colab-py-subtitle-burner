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
