#!flask/bin/python
################################################################################################################################
# ------------------------------------------------------------------------------------------------------------------------------
# This file implements the REST layer. It uses flask micro framework for server implementation. Calls from front end reaches 
# here as json and being branched out to each projects. Basic level of validation is also being done in this file. #                                                                                                                                  	       
# -------------------------------------------------------------------------------------------------------------------------------
################################################################################################################################
import json

from flask import Flask, jsonify, abort, request, make_response, url_for, redirect, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.utils import secure_filename
import os
import glob
import re
import shutil
import numpy as np
from search import recommend
import tarfile
from datetime import datetime
from scipy import ndimage

# from scipy.misc import imsave

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
from tensorflow.python.platform import gfile

app = Flask(__name__, static_url_path="")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
auth = HTTPBasicAuth()

# ==============================================================================================================================
#                                                                                                                              
#    Loading the extracted feature vectors for image retrieval                                                                 
#                                                                          						        
#                                                                                                                              
# ==============================================================================================================================
extracted_features = np.zeros((10000, 2048), dtype=np.float32)
with open('saved_features_recom.txt') as f:
    for i, line in enumerate(f):
        extracted_features[i, :] = line.split()
print("loaded extracted_features")


# ==============================================================================================================================
#                                                                                                                              
#  This function is used to do the image search/image retrieval
#                                                                                                                              
# ==============================================================================================================================
@app.route('/imgUpload', methods=['GET', 'POST'])
# def allowed_file(filename):
#    return '.' in filename and \
#           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_img():
    print("image upload")
    result = 'static/result'
    if not gfile.Exists(result):
        os.mkdir(result)
    shutil.rmtree(result)

    if request.method == 'POST' or request.method == 'GET':
        print(request.method)
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)

        file = request.files['file']
        print(file.filename)
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file:  # and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            inputloc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            recommend(inputloc, extracted_features)
            os.remove(inputloc)
            image_path = "/result"
            image_list = [os.path.join(image_path, file) for file in os.listdir(result)
                          if not file.startswith('.')]

            imgdes = []
            des = set()
            dirPath = 'database/tags/'
            file_list = os.listdir(dirPath)
            for item in image_list:
                index = re.findall(r"\d+", item)
                for file in file_list:
                    s = open(dirPath + file, 'r').readlines()
                    if index[0] + "\n" in s:
                        if "_r1" in file:
                            des.add(file.replace("_r1.txt", ""))
                        else:
                            des.add(file.replace(".txt", ""))
                imgdes.append(list(des))
                des.clear()

            fav=[]
            fPath='static/favourites'
            favourites = os.listdir(fPath)
            for image in image_list:
                if image.split("\\")[1] in favourites:
                    fav.append("true")
                else:
                    fav.append("false")

            images = {
                'image0': image_list[0],
                'image0des': ','.join(imgdes[0]),
                'image1': image_list[1],
                'image1des': ','.join(imgdes[1]),
                'image2': image_list[2],
                'image2des': ','.join(imgdes[2]),
                'image3': image_list[3],
                'image3des': ','.join(imgdes[3]),
                'image4': image_list[4],
                'image4des': ','.join(imgdes[4]),
                'image5': image_list[5],
                'image5des': ','.join(imgdes[5]),
                'image6': image_list[6],
                'image6des': ','.join(imgdes[6]),
                'image7': image_list[7],
                'image7des': ','.join(imgdes[7]),
                'image8': image_list[8],
                'image8des': ','.join(imgdes[8]),
                'fav':fav
            }
            return jsonify(images)


# ==============================================================================================================================
#
#  This function is used to select images according to tags
#
# ==============================================================================================================================
@app.route('/tag', methods=['GET', 'POST'])
def tag():
    tagPath = 'static/tag_result'
    if gfile.Exists(tagPath):
        shutil.rmtree(tagPath)
    os.mkdir(tagPath)

    if request.method == 'POST' or request.method == 'GET':
        # print("tags:")
        tags = request.form.get("tags")
        # print(tags)

        tags = json.loads(tags)

        s = set()
        dirPath = 'database/tags/'
        for item in tags:
            if os.path.exists(dirPath + item + '_r1.txt'):
                s1 = set(open(dirPath + item + '.txt', 'r').readlines())
                s2 = set(open(dirPath + item + '_r1.txt', 'r').readlines())
                s1 = s1.union(s2)
            else:
                s1 = set(open(dirPath + item + '.txt', 'r').readlines())

            if len(s) != 0:
                s = s.intersection(s1)
            else:
                s = s.union(s1)

        s = [x.replace("\n", "") for x in s]

        dataPath = 'database/dataset/im'

        result = [x for x in s if int(x) <= 3000 and os.path.exists(dataPath + x + '.jpg')]

        for item in result:
            if os.path.exists(dataPath + item + '.jpg'):
                shutil.copyfile(dataPath + item + '.jpg', tagPath + '/im' + item + '.jpg')

        result = ['tag_result/im' + x + '.jpg' for x in result]

        fav = []
        fPath = 'static/favourites'
        favourites = os.listdir(fPath)
        for image in result:
            if image.split("/")[1] in favourites:
                fav.append("true")
            else:
                fav.append("false")

        response = {'len': len(result),
                    'path': result,
                    'fav':fav
                    }

        return jsonify(response)


# ==============================================================================================================================
#
#  This function is used to manage favourites
#
# ==============================================================================================================================
@app.route('/favourite', methods=['GET', 'POST'])
def favourite():
    fPath = 'static/favourites/'
    if not gfile.Exists(fPath):
        os.mkdir(fPath)

    if request.method == 'POST' or request.method == 'GET':
        method = request.form.get("method").replace("\"","")
        imgPath = request.form.get("path").replace("\"","")

        dataPath = 'database/dataset/'

        if method=="star":
            if not os.path.exists(fPath + imgPath):
                shutil.copyfile(dataPath + imgPath, fPath + imgPath)
        else:
            if os.path.exists(fPath + imgPath):
                os.remove(fPath + imgPath)

        return jsonify('success')

# ==============================================================================================================================
#
#  This function is used to return favourites
#
# ==============================================================================================================================
@app.route('/getfavourite', methods=['GET', 'POST'])
def getFavourite():
    fPath = 'static/favourites/'
    if not gfile.Exists(fPath):
        os.mkdir(fPath)

    if request.method == 'POST' or request.method == 'GET':
        file_list = os.listdir(fPath)
        return jsonify(file_list)

# ==============================================================================================================================
#                                                                                                                              
#                                           Main function                                                        	            #						     									       
#  				                                                                                                
# ==============================================================================================================================
@app.route("/")
def main():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
