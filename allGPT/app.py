from flask import Flask, redirect, request, jsonify
# 解决跨域
from flask_cors import CORS
# 导入语音模块
from base import client, client2, client3, client4, client5
# 导入时间
from time import time
import base64

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=['GET'])
def home():
    return redirect('./static/index.html')


# 语音转文字
@app.route('/text2voice', methods=['POST'])
def text2voice():
    timeStrap = str(time()).split('.')[0]
    text = request.get_json()['text']
    result = client.synthesis(text, 'zh', 1, {
        'vol': 5,
    })
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    filePath = './static/temp/audio/' + timeStrap + '.mp3'
    if not isinstance(result, dict):
        with open(filePath, 'wb') as f:
            f.write(result)
    return timeStrap + '.mp3'


# 通用搜过
@app.route('/wordSearch', methods=['POST'])
def wordSearch():
    timeStrap = str(time()).split('.')[0]
    data = request.files
    file = data['files']
    ret = {}
    if file.filename != '':
        # 将上传的文件保存在该目录下
        path = 'static/temp/img/' + timeStrap + '.png'
        file.save(path)
        # 读取文件，调用百度ai
        """ 读取文件 """

        def get_file_content(filePath):
            with open(filePath, "rb") as fp:
                return fp.read()

        image = get_file_content(path)
        # 调用通用文字识别（标准版）
        res_image = client2.basicGeneral(image)
        print(res_image)

        ret["code"] = 0
        ret["path"] = path
        ret["data"] = res_image
        ret["msg"] = "上传成功！"
    else:
        ret["code"] = 1
        ret["msg"] = "上传失败！"
        # 返回
    return ret


# 办公文档识别
@app.route('/workSearch', methods=['POST'])
def workSearch():
    timeStrap = str(time()).split('.')[0]
    data = request.files
    file = data['files']
    ret = {}
    if file.filename != '':
        # 将上传的文件保存在该目录下
        path = 'static/temp/img/' + timeStrap + '.png'
        file.save(path)
        # 读取文件，调用百度ai
        """ 读取文件 """

        def get_file_content(filePath):
            with open(filePath, "rb") as fp:
                return fp.read()

        image = get_file_content(path)

        res_image = client2.doc_analysis_office(image)
        print(res_image)

        ret["code"] = 0
        ret["path"] = path
        ret["data"] = res_image
        ret["msg"] = "上传成功！"
    else:
        ret["code"] = 1
        ret["msg"] = "上传失败！"
        # 返回
    return ret


@app.route('/perSearch', methods=['POST'])
def perSearch():
    timeStrap = str(time()).split('.')[0]
    data = request.files
    file = data['files']
    ret = {}
    if file.filename != '':
        # 将上传的文件保存在该目录下
        path = 'static/temp/img/' + timeStrap + '.png'
        file.save(path)
        # 读取文件，调用百度ai
        """ 读取文件 """

        def get_file_content(filePath):
            with open(filePath, "rb") as fp:
                return fp.read()

        image = get_file_content(path)

        res_image = client3.bodyAttr(image)
        print(res_image)

        ret["code"] = 0
        ret["path"] = path
        ret["data"] = res_image
        ret["msg"] = "上传成功！"
    else:
        ret["code"] = 1
        ret["msg"] = "上传失败！"
        # 返回
    return ret


@app.route('/goodSearch', methods=['POST'])
def goodSearch():
    timeStrap = str(time()).split('.')[0]
    data = request.files
    file = data['files']
    ret = {}
    if file.filename != '':
        # 将上传的文件保存在该目录下
        path = 'static/temp/img/' + timeStrap + '.png'
        file.save(path)
        # 读取文件，调用百度ai
        """ 读取文件 """

        def get_file_content(filePath):
            with open(filePath, "rb") as fp:
                return fp.read()

        image = get_file_content(path)

        res_image = client4.advancedGeneral(image)
        print(res_image)

        ret["code"] = 0
        ret["path"] = path
        ret["data"] = res_image
        ret["msg"] = "上传成功！"
    else:
        ret["code"] = 1
        ret["msg"] = "上传失败！"
        # 返回
    return ret


@app.route('/carSearch', methods=['POST'])
def carSearch():
    timeStrap = str(time()).split('.')[0]
    data = request.files
    file = data['files']
    ret = {}
    if file.filename != '':
        # 将上传的文件保存在该目录下
        path = 'static/temp/img/' + timeStrap + '.png'
        file.save(path)
        # 读取文件，调用百度ai
        """ 读取文件 """

        def get_file_content(filePath):
            with open(filePath, "rb") as fp:
                return fp.read()

        image = get_file_content(path)

        res_image = client4.carDetect(image)
        print(res_image)

        ret["code"] = 0
        ret["path"] = path
        ret["data"] = res_image
        ret["msg"] = "上传成功！"
    else:
        ret["code"] = 1
        ret["msg"] = "上传失败！"
        # 返回
    return ret


@app.route('/logoSearch', methods=['POST'])
def logoSearch():
    timeStrap = str(time()).split('.')[0]
    data = request.files
    file = data['files']
    ret = {}
    if file.filename != '':
        # 将上传的文件保存在该目录下
        path = 'static/temp/img/' + timeStrap + '.png'
        file.save(path)
        # 读取文件，调用百度ai
        """ 读取文件 """

        def get_file_content(filePath):
            with open(filePath, "rb") as fp:
                return fp.read()

        image = get_file_content(path)

        res_image = client4.logoSearch(image)
        print(res_image)

        ret["code"] = 0
        ret["path"] = path
        ret["data"] = res_image
        ret["msg"] = "上传成功！"
    else:
        ret["code"] = 1
        ret["msg"] = "上传失败！"
        # 返回
    return ret


@app.route('/plantSearch', methods=['POST'])
def plantSearch():
    timeStrap = str(time()).split('.')[0]
    data = request.files
    file = data['files']
    ret = {}
    if file.filename != '':
        # 将上传的文件保存在该目录下
        path = 'static/temp/img/' + timeStrap + '.png'
        file.save(path)
        # 读取文件，调用百度ai
        """ 读取文件 """

        def get_file_content(filePath):
            with open(filePath, "rb") as fp:
                return fp.read()

        image = get_file_content(path)

        res_image = client4.plantDetect(image)
        print(res_image)

        ret["code"] = 0
        ret["path"] = path
        ret["data"] = res_image
        ret["msg"] = "上传成功！"
    else:
        ret["code"] = 1
        ret["msg"] = "上传失败！"
        # 返回
    return ret


@app.route('/pictureFix', methods=['POST'])
def pictureFix():
    timeStrap = str(time()).split('.')[0]
    data = request.files
    file = data['files']
    ret = {}
    if file.filename != '':
        # 将上传的文件保存在该目录下
        path = 'static/temp/fixImg/' + timeStrap + '.png'
        file.save(path)
        # 读取文件，调用百度ai
        """ 读取文件 """

        def get_file_content(filePath):
            with open(filePath, "rb") as fp:
                return fp.read()

        image = get_file_content(path)
        res_image = client5.imageDefinitionEnhance(image)
        img_base64 = res_image.get("image")
        path = 'static/temp/img/' + timeStrap + '.png'
        toHtml = './temp/img/' + timeStrap + '.png'

        with open(path, 'wb') as fp:
            # 需要做base64转码，将base64 字符串转换成 二进制数据，然后写入到 png 图片
            fp.write(base64.b64decode(img_base64))

        ret["code"] = 0
        ret["path"] = toHtml
        ret["data"] = res_image
        ret["msg"] = "上传成功！"
    else:
        ret["code"] = 1
        ret["msg"] = "上传失败！"
        # 返回
    return ret


@app.route('/blackWhite', methods=['POST'])
def blackWhite():
    timeStrap = str(time()).split('.')[0]
    data = request.files
    file = data['files']
    ret = {}
    if file.filename != '':
        # 将上传的文件保存在该目录下
        path = 'static/temp/fixImg/' + timeStrap + '.png'
        file.save(path)
        # 读取文件，调用百度ai
        """ 读取文件 """

        def get_file_content(filePath):
            with open(filePath, "rb") as fp:
                return fp.read()

        image = get_file_content(path)
        res_image = client5.colourize(image)
        img_base64 = res_image.get("image")
        path = 'static/temp/img/' + timeStrap + '.png'
        toHtml = './temp/img/' + timeStrap + '.png'

        with open(path, 'wb') as fp:
            # 需要做base64转码，将base64 字符串转换成 二进制数据，然后写入到 png 图片
            fp.write(base64.b64decode(img_base64))

        ret["code"] = 0
        ret["path"] = toHtml
        ret["data"] = res_image
        ret["msg"] = "上传成功！"
    else:
        ret["code"] = 1
        ret["msg"] = "上传失败！"
        # 返回
    return ret


@app.route('/dongman', methods=['POST'])
def dongman():
    timeStrap = str(time()).split('.')[0]
    data = request.files
    file = data['files']
    ret = {}
    if file.filename != '':
        # 将上传的文件保存在该目录下
        path = 'static/temp/fixImg/' + timeStrap + '.png'
        file.save(path)
        # 读取文件，调用百度ai
        """ 读取文件 """

        def get_file_content(filePath):
            with open(filePath, "rb") as fp:
                return fp.read()

        image = get_file_content(path)
        res_image = client5.selfieAnime(image)
        img_base64 = res_image.get("image")
        path = 'static/temp/img/' + timeStrap + '.png'
        toHtml = './temp/img/' + timeStrap + '.png'

        with open(path, 'wb') as fp:
            # 需要做base64转码，将base64 字符串转换成 二进制数据，然后写入到 png 图片
            fp.write(base64.b64decode(img_base64))

        ret["code"] = 0
        ret["path"] = toHtml
        ret["data"] = res_image
        ret["msg"] = "上传成功！"
    else:
        ret["code"] = 1
        ret["msg"] = "上传失败！"
        # 返回
    return ret


if __name__ == '__main__':
    app.run()
