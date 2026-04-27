# backend/services/video_builder.py

from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips


OUTPUT_VIDEO_FOLDER = "output/videos"


def build_final_video(frame_paths, audio_paths, output_file="final_video.mp4"):
    """
    Combine frames + audio into final video

    Example:
    frame_paths = ["output/frames/frame_1.png"]
    audio_paths = ["output/audio/audio_1.mp3"]

    Output:
    output/videos/final_video.mp4
    """

    clips = []

    for frame, audio in zip(frame_paths, audio_paths):
        audio_clip = AudioFileClip(audio)

        image_clip = (
            ImageClip(frame)
            .set_duration(audio_clip.duration)
            .set_audio(audio_clip)
        )

        clips.append(image_clip)

    final_video = concatenate_videoclips(clips, method="compose")

    output_path = f"{OUTPUT_VIDEO_FOLDER}/{output_file}"

    final_video.write_videofile(
        output_path,
        fps=24
    )

    return output_path