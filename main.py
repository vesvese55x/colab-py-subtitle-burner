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
       text_clip = mp.TextClip(
    subtitle.content, 
    fontsize=32,  # Small-medium arasında bir büyüklük olarak 32 seçildi
    font='Arial-Bold-Italic',  # Kalın ve italik Arial yazı tipi
    color="yellow",  # Yazı rengi sarı
    stroke_color='black', 
    stroke_width=2, 
    size=(video_width * 1/2, None),  # Metin genişliği, videonun yarısı kadar
    method='caption'
)


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

# compose VideoClip and TextClips
final_video = mp.CompositeVideoClip([video] + subtitle_clips)

# the video path without extension
video_path_without_extension = FilePath.remove_file_extension(
    video_filepath)

# the video extension
video_extension = FilePath.get_file_extension(video_filepath)

# the file path of the subtitled video
new_video_path = video_path_without_extension+"[subtitled]"+video_extension

#write the subtitled video
final_video.write_videofile(new_video_path)
