# Functions to manipulate the graphics on Qualtrics libaray
import json
import http.client

def delete(img_id):
    conn = http.client.HTTPSConnection("iad1.qualtrics.com")

    headers = {
        'Content-Type': "application/json",
        'X-API-TOKEN': "A3BEG5Jxu8jX4ZEFnQtTokBatIyFXpt2gAz1UizM"
        }

    conn.request("DELETE", "/API/v3/libraries/UR_cTIvKxsmN7AzjL0/graphics/{}".format(img_id), headers=headers) # My library

    res = conn.getresponse()
    data = res.read()
    status = json.loads(data.decode("utf-8"))["meta"]
    print(status)

delete("IM_d6AqilZjM2DFEBU")
delete("IM_eG1puGDeZZi2m90")

#curl --request POST \
#  --url https://iad1.qualtrics.com/API/v3/libraries/UR_cTIvKxsmN7AzjL0/graphics \
#  --header 'Content-Type: multipart/form-data; boundary=---011000010111000001101001' \
#  --header 'X-API-TOKEN: A3BEG5Jxu8jX4ZEFnQtTokBatIyFXpt2gAz1UizM' \
#  --form file=@/Users/jonwang/Desktop/pic_1.png \
#  --form folder=foldername
