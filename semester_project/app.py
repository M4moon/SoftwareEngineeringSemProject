from flask import Flask, render_template, request
from googleapiclient.discovery import build

app = Flask(__name__)

# Enter your YouTube API key here
YOUTUBE_API_KEY = 'AIzaSyBOgxaAAGrKj81soJ_Zm0_sp5O15Zk41u0'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    
    # Make a request to the YouTube API
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    search_response = youtube.search().list(
        q=query,
        type='video',
        part='id,snippet'
    ).execute()

    videos = []
    for search_result in search_response.get('items', []):
        video_id = search_result['id']['videoId']
        video_title = search_result['snippet']['title']
        videos.append({'id': video_id, 'title': video_title})

    return render_template('search_results.html', videos=videos)

if __name__ == '__main__':
    app.run(debug=True)
