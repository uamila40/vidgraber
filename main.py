from flask import Flask , request
import yt_dlp

app = Flask(__name__)

# Yowza


ydl_opts = {}


@app.route("/")
def hello_world():
    return "Hello from the Flask server!"

@app.route("/reqest", methods = ["POST"])
def reqest():
    videourl = (request.form["videourl"])

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Replace 'VIDEO_URL' with the URL of the video you want to get the title of
        video_info = ydl.extract_info(videourl, download=False)

        # Extract the video title from the video_info dictionary
        video_title = video_info.get('title', None)

        if video_title:
            title = str(video_title)
        else:
            title = str("Unable to retrieve the video title.")

    return title

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
