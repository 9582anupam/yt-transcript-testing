from flask import Flask, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# testing api
@app.route('/', methods=['GET'])
def test_api():
    return jsonify({
        "message": "API is running /"
    })

@app.route('/api/transcript/<video_id>', methods=['GET'])
def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(
            video_id, 
            languages=['en', 'hi', 'en', 'en-US', 'en-GB', 'en-IN', 'en-CA', 'en-AU',  # English variants
            'hi', 'hi-IN', 'ta', 'af', 'am', 'ar', 'as', 'az', 'bn', 'be', 'bs', 'bg', 'ca', 
            'ceb', 'zh-CN', 'zh-TW', 'co', 'hr', 'cs', 'da', 'dv', 'nl', 
            'en', 'eo', 'et', 'eu', 'fa', 'fil', 'fi', 'fr', 'fy', 'ga', 
            'gd', 'gl', 'de', 'el', 'gu', 'ha', 'iw', 'hi', 'hu', 'id', 
            'it', 'ja', 'kn', 'kk', 'ko', 'ky', 'lv', 'lt', 'lb', 'mk', 
            'ml', 'mt', 'mr', 'ne', 'no', 'or', 'pl', 'pt', 'pa', 'ro', 
            'ru', 'sr', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'sw', 'sv', 
            'tg', 'ta', 'te', 'th', 'tr', 'tk', 'uk', 'ur', 'uz', 'vi', 
            'cy', 'yi', 'zh'],
            cookies='cookies.txt'  # Use cookies for authentication
        )
        return jsonify({
            "success": True,
            "transcript": transcript
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
