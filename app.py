from flask import Flask, request, send_file
import yt_dlp, os, uuid

app = Flask(__name__)
os.makedirs("downloads", exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        filename = f"{uuid.uuid4()}.mp4"
        path = f"downloads/{filename}"

        ydl_opts = {
            "outtmpl": path,
            "format": "mp4",
            "quiet": True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return send_file(path, as_attachment=True)

    return """
    <h2>TikTok Downloader (No Watermark)</h2>
    <form method="post">
        <input name="url" placeholder="Paste link TikTok" required style="width:300px">
        <button>Download</button>
    </form>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
