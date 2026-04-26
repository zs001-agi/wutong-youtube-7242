import argparse
import json
import os
from pytube import YouTube

def download_youtube(url, output=None, json_flag=False):
    try:
        yt = YouTube(url)
        video_title = yt.title.replace(' ', '_')
        if not output:
            output = f"{video_title}.mp4"

        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=output)

        if json_flag:
            data = {
                "url": url,
                "title": yt.title,
                "output_file": output
            }
            print(json.dumps(data, indent=4))
        else:
            print(f"Downloaded: {yt.title} to {output}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube video/audio downloader")
    parser.add_argument("url", help="URL of the YouTube video to download")
    parser.add_argument("--output", help="Output file name for the downloaded video")
    parser.add_argument("--json", action='store_true', help="Output information in JSON format")

    args = parser.parse_args()
    download_youtube(args.url, output=args.output, json_flag=args.json)