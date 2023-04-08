from moviepy.editor import AudioFileClip, VideoFileClip
from wrappers.vidgear_wrapper import create_writer_instance
from tqdm import tqdm
import cv2


def create_image_video(image_path, output_path, video_length, fps=30):
    image = cv2.imread(image_path)
    writer = create_writer_instance(output_path, fps)

    FRAMES = video_length * fps

    for _ in tqdm(range(FRAMES)):
        writer.write(image)

    writer.close()


def combine_video_audio_file(video_path, audio_path, output_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)
    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(output_path)


def create_image_video_of_audio_length(image_path, audio_path, output_path, fps=30):
    audio = AudioFileClip(audio_path)
    duration = int(audio.duration)
    create_image_video(
        image_path=image_path,
        output_path=output_path,
        video_length=duration,
        fps=fps
    )
