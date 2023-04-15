from flask import Flask, request
from src import summary, video_id
from src import transcription

app = Flask('app')


@app.route('/api', methods=['POST'])
def make_summary_2():
    video_url = request.args.get('video_url')
    id = video_id.get_from_url(video_url)
    _, transcript = transcription.get_english_transcription(id)
    return summary.make(transcript)


app.run(host='0.0.0.0', port=8080)
