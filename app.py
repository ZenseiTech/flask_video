from flask import Flask, render_template, request, send_from_directory
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ThIs v3ry S3crat'

port = 8080

video_dict = {
    "Default": "static/videos/ocean/sample_2.m3u8",
    "sample_1": "static/videos/coast_line/sample_1.m3u8",
    "sample_2": "static/videos/ocean/sample_2.m3u8"
}


def get_filename(filename):
    return video_dict.get(
        filename, "static/videos/coast_line/sample_1.m3u8")


@app.route('/')
def index():
    return render_template('index.html', filename=get_filename("Default"))


@app.route('/<path:filename>')
def file(filename):
    return render_template('index.html', filename=get_filename(filename))


@app.after_request
def add_headers(response):
    '''Add CORS support'''
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    app.logger.setLevel(logging.INFO)
    app.run(port=port)
