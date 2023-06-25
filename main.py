import srt
from modules.filepath import FilePath

video_filepath = FilePath.read_video_filepath()
srt_filepath = FilePath.read_srt_filepath()

# read srt file contents
with open(srt_filepath, "r", encoding="utf-8") as file:
    srt_data = file.read()

# parse srt
parsed_subtitles = srt.parse(srt_data)

#create list of subtitles
subtitles_list = list(parsed_subtitles)