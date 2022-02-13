import logging
import os

from flask import Flask, request, render_template, jsonify
from flask_jsglue import \
    JSGlue  # this is use for url_for() working inside javascript which is help us to navigate the url
from werkzeug.utils import secure_filename

from application import util
from flaskmine.application.toggles import get_toggle_save_images, get_toggle_save_images_per_category
from flaskmine.application.util import allowed_file

application = Flask(__name__)
logger = logging.getLogger()
logger.propagate = True
# JSGlue is use for url_for() working inside javascript which is help us to navigate the url
jsglue = JSGlue()  # create a object of JsGlue
jsglue.init_app(application)  # and assign the app as a init app to the instance of JsGlue

util.load_artifacts()

TOGGLE_SAVE_IMAGES = get_toggle_save_images()
TOGGLE_SAVE_IMAGES_PER_CATEGORY = get_toggle_save_images_per_category()
# home page
@application.route("/")
def home():
    return render_template("index.html")


@application.route("/classification")
def classification():
    return render_template("classification.html")


@application.route("/about")
def about():
    return render_template("about.html")


@application.route("/info")
def info():
    return render_template("info.html")


@application.route("/api-call")
def api_call():
    return render_template("api-call.html")


@application.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if 'files[]' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp

    files = request.files.getlist('files[]')

    errors = {}
    success = False

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            basepath = os.path.dirname(__file__)
            image_path = os.path.join(basepath, "uploads", secure_filename(file.filename))
            file.save(image_path)
            file.save(os.path.join(application.config['/static/new-uploads'], filename))

            success = True
        else:
            errors[file.filename] = 'File type is not allowed'

    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
    if success:
        resp = jsonify({'message': 'Files successfully uploaded'})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp


# classify waste
@application.route("/classifywaste", methods=["GET", "POST"])
def classifywaste():
    logger.info("here we are")
    image_data = request.files["file"]
    # save the image to upload
    basepath = os.path.dirname(__file__)
    image_path = os.path.join(basepath, "static/new_uploads", secure_filename(image_data.filename))
    image_path_category = os.path.join(basepath, "static/cath_uploads", secure_filename(image_data.filename))
    logger.info("before save image--")
    image_data.save(image_path)

    predicted_value, romanian_translation, details, video1, video2, probability = util.classify_waste(image_path)

    if TOGGLE_SAVE_IMAGES:
        logger.warning("Image Saved")
    elif TOGGLE_SAVE_IMAGES_PER_CATEGORY:
        image_data.save(image_path_category.replace("/cath_uploads", "/cath_uploads/" + predicted_value))
        logger.warning("Image Saved in category: " + predicted_value)
        os.remove(image_path)
    else:
        os.remove(image_path)

    return jsonify(predicted_value=predicted_value, romanian_translation=romanian_translation, details=details,
                   video1=video1, video2=video2, probability=probability)


@application.route('/api/classifywaste', methods=['GET', 'POST'])
def classifywaste_api():
    if 'files[]' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp

    files = request.files.getlist('files[]')

    errors = {}
    success = False

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            basepath = os.path.dirname(__file__)
            image_path = os.path.join(basepath, "static/new_uploads", secure_filename(file.filename))
            file.save(image_path)
            success = True
        else:
            errors[file.filename] = 'File type is not allowed'

    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
    if success:
        predicted_value, romanian_translation, details, video1, video2, probability = util.classify_waste(image_path)
        return jsonify(predicted_value=predicted_value, romanian_translation=romanian_translation,
                       probability=probability)

    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp


# here is route of 404 means page not found error
@application.errorhandler(404)
def page_not_found(e):
    # here i created my own 404 page which will be redirect when 404 error occured in this web app
    logging.warning("404 page found")
    return render_template("404.html"), 404


if __name__ == "__main__":
    # context = ('local.crt', 'local.key')
    application.run(host="gbgselection.ro", port=80)  # ssl_context=context)
