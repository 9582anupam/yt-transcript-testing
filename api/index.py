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
        # Define high priority languages (English variants + Hindi variants)
        high_priority_languages = [
            'en', 'en-US', 'en-GB', 'en-IN', 'en-CA', 'en-AU',  # English variants
            'hi', 'hi-IN'  # Hindi variants
        ]
        
        # Define comprehensive list of supported languages
        supported_languages = [
            'af', 'am', 'ar', 'as', 'az', 'bn', 'be', 'bs', 'bg', 'ca', 
            'ceb', 'zh-CN', 'zh-TW', 'co', 'hr', 'cs', 'da', 'dv', 'nl', 
            'en', 'eo', 'et', 'eu', 'fa', 'fil', 'fi', 'fr', 'fy', 'ga', 
            'gd', 'gl', 'de', 'el', 'gu', 'ha', 'iw', 'hi', 'hu', 'id', 
            'it', 'ja', 'kn', 'kk', 'ko', 'ky', 'lv', 'lt', 'lb', 'mk', 
            'ml', 'mt', 'mr', 'ne', 'no', 'or', 'pl', 'pt', 'pa', 'ro', 
            'ru', 'sr', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'sw', 'sv', 
            'tg', 'ta', 'te', 'th', 'tr', 'tk', 'uk', 'ur', 'uz', 'vi', 
            'cy', 'yi', 'zh'
        ]
        
        # Get list of available transcripts
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        selected_transcript = None
        
        # First try high priority languages
        for lang in high_priority_languages:
            try:
                selected_transcript = transcript_list.find_transcript([lang])
                break
            except:
                continue
        
        # If no high priority language found, try other supported languages
        if not selected_transcript:
            for lang in supported_languages:
                try:
                    selected_transcript = transcript_list.find_transcript([lang])
                    break
                except:
                    continue
        
        # If still no match, get any available transcript
        if not selected_transcript:
            # Get the first available transcript
            for transcript in transcript_list:
                selected_transcript = transcript
                break
        
        # Get the actual transcript
        transcript = selected_transcript.fetch()
        
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
