from moviepy.editor import concatenate_audioclips, AudioFileClip
from wrappers.vidgear_wrapper import create_writer_instance
import cv2
from tqdm import tqdm


def concatenate_audio(audio_clip_paths, output_path):
    clips = [AudioFileClip(path) for path in audio_clip_paths]
    final_clip = concatenate_audioclips(clips)
    final_clip.write_audiofile(output_path)


def create_image_video(image_path, output_path, video_length, fps=30):
    image = cv2.imread(image_path)
    writer = create_writer_instance(output_path, fps)

    FRAMES = video_length * fps

    for _ in tqdm(range(FRAMES)):
        writer.write(image)

    writer.close()
