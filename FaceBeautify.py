import requests
import base64
import json

url = "https://api-cn.faceplusplus.com/facepp/v2/beautify"
LvJingEn = ['black_white', 'calm', 'sunny', 'trip', 'beautify', 'wangjiawei', 'cutie', 'macaron', 'new_york', 'sakura',
            '17_years_old', 'clight', 'tea_time', 'whiten', 'chaplin', 'flowers', 'memory', 'ice_lady', 'paris',
            'times', 'lomo', 'old_times', 'spring', 'story', 'abao', 'wlight', 'warm', 'glitter', 'lavender', 'chanel',
            'prague', 'old_dream', 'blossom', 'pink', 'jiang_nan']
LvJingCh = ['黑白', '平静', '晴天', '旅程', '美肤', '王家卫', '唯美', '可人儿', '纽约', '樱花', '十七岁', '柔光灯', '下午茶', '亮肤', '卓别林', '花香', '回忆',
            '冰美人', '巴黎', '时光', 'LOMO', '旧时光', '早春', '故事', '阿宝色', '补光灯', '暖暖', '绚烂', '薰衣草', '香奈儿', '布拉格', '旧梦', '桃花',
            '粉黛', '江南']
LvJingDict = dict(zip(LvJingCh, LvJingEn))
with open("api帐号密码.txt","r") as f:
    p = f.readlines()
    apikey = p[0].strip("\n")
    apisecret = p[1].strip("\n")

def face_beautify(img1,whitening=50,smoothing=50,thinface=50,shrink_face=50,enlarge_eye=50,remove_eyebrow=50,filter_type='无滤镜'):
    with open(img1,'rb') as f:
        face1 = base64.b64encode(f.read())
    data = {
        "api_key":apikey,
        "api_secret":apisecret,
        "image_base64":face1,
        "whitening":whitening,
        "smoothing":smoothing,
        "thinface":thinface,
        "shrink_face":shrink_face,
        "enlarge_eye":enlarge_eye,
        "remove_eyebrow":remove_eyebrow
    }
    if filter_type!="无滤镜":
        #print(LvJingDict['平静'])
        data["filter_type"]=LvJingDict[filter_type]
    respose = requests.post(url,data)
    print(type(respose.text))
    content = json.loads(respose.text)
    print(content)
    newimg = img1.split(".")[0]
    print(newimg)
    with open(newimg+"美颜.jpg",'wb') as f:
        f.write(base64.b64decode(content["result"]))
    return newimg+"美颜.jpg"
# c:/ab/cd/ef.jpg
if __name__ == '__main__':
    face_beautify("img4.jpeg",filter_type = "王家卫")