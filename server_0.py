from flask import Flask, render_template, request, send_file
from PIL import Image

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('test_upload.html')

@app.route('/upload',methods=['POST'])
def upload():
    file = request.files['image']
    image = Image.open(file)
    #  Process the image here
    processed_image = image.rotate(45)
    # save the processed image to a file
    processed_image.save('processed_image.png')
    # Return the processed image file as a response
    return render_template('upload_completed.html')

if __name__ == '__main__':
    app.run(debug=True)
