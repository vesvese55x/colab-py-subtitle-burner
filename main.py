import srt
import moviepy.editor as mp
from modules.filepath import FilePath

video_filepath = FilePath.read_video_filepath()
srt_filepath = FilePath.read_srt_filepath()

# read srt file contents
with open(srt_filepath, "r", encoding="utf-8") as file:
    srt_data = file.read()

# parse srt
parsed_subtitles = srt.parse(srt_data)

# create list of subtitles
subtitles_list = list(parsed_subtitles)

# create VideoClip object
video = mp.VideoFileClip(video_filepath, audio=True)


# create list of TextClip objetcs from the subtitles list
def create_subtitle_clips(subtitles_list):
    subtitle_clips = []

    for subtitle in subtitles_list:

        start_time = subtitle.start.total_seconds()  # subtitle start
        end_time = subtitle.end.total_seconds()  # subtitle end
        duration = end_time - start_time  # subtitle duration

        # video dimensions
        video_width, video_height = video.size

        # create TextClip object for the subtitle
        text_clip = mp.TextClip(subtitle.content, fontsize=40, font='Arial-bold', color="white", stroke_color='black', stroke_width=2, size=(
            video_width*1/2, None), method='caption')

        # set the TextClip start and duration
        text_clip = text_clip.set_start(start_time).set_duration(duration)

        # set the subtitle position
        subtitle_x_position = 'center'
        subtitle_y_position = video_height * 4 / 5
        text_position = (subtitle_x_position, subtitle_y_position)

        # add the new TextClip to the subtitle_clips list
        subtitle_clips.append(text_clip.set_position(text_position))

    return subtitle_clips


subtitle_clips = create_subtitle_clips(subtitles_list)
