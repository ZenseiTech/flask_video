# Create a Python Video Streaming Server Using HLS

### From the command line run:

$ ffmpeg -i ${your_mp4_file} -codec: copy -start_number 0 -hls_time 10 -hls_list_size 0 -f hls ${your_output_m3u8_file}

- Run the server

- Test your video play by using a media client. You can find a free online client here:

https://hls-js-latest.netlify.com/demo/

- And copy the path to m3u8:

http://127.0.0.1:8080/static/videos/sample_1.m3u8

### Javascript player to run on browser

https://videojs.com/city

If running with port 8080 then in your browser you can do this:

http://localhost:8080

http://localhost:8080/sample_1

http://localhost:8080/sample_2
