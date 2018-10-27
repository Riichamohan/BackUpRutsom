import os
from flask import Flask, request, jsonify

from keras.preprocessing import image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'Uploads'


def prepare_image(img):
    # Convert the image to a numpy array
    img = image.img_to_array(img)
    # Scale from 0 to 255
    img /= 255
    # Invert the pixels
    img = 1 - img
    # Flatten the image to an array of pixels
    image_array = img.flatten().reshape(-1, 28 * 28)
    # Return the processed feature array
    return image_array


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request)

        if request.files.get('file'):
            # read the file
            # @TODO: YOUR CODE HERE!

            # read the filename
            # @TODO: YOUR CODE HERE!

            # create a path to the uploads folder
            # @TODO: YOUR CODE HERE!

            # Save the file to the uploads folder
            # @TODO: YOUR CODE HERE!

            # Load the saved image using Keras and resize it to the mnist format of 28x28 pixels
            # @TODO: YOUR CODE HERE!

            # Convert the 2D image to an array of pixel values
            image_array = prepare_image(im)
            print(image_array)

            return "Data Pre-processing Complete!"
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


if __name__ == "__main__":
    app.run(debug=True)