from moviepy.editor import concatenate_audioclips, AudioFileClip


def concatenate_audio(audio_clip_paths, output_path):
    clips = [AudioFileClip(path) for path in audio_clip_paths]
    final_clip = concatenate_audioclips(clips)
    final_clip.write_audiofile(output_path)
