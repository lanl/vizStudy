#import http.client
#import urllib.parse
#import json
#
#conn = http.client.HTTPSConnection("iad1.qualtrics.com")
#
#payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\npic1.png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"\r\n\r\n@/Users/jonwang/Desktop/pic_1.png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"contentType\"\r\n\r\nimage/png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"folder\"\r\n\r\ntesting_folder\r\n-----011000010111000001101001--\r\n\r\n"
#
#headers = {
#    'Content-Type': "multipart/form-data; boundary=---011000010111000001101001",
#    'X-API-TOKEN': "A3BEG5Jxu8jX4ZEFnQtTokBatIyFXpt2gAz1UizM"
#    }
#
#conn.request("POST", "/API/v3/libraries/UR_cTIvKxsmN7AzjL0/graphics", payload, headers)
#
#res = conn.getresponse()
#data = res.read()
#
#print(data.decode("utf-8"))

#
#curl --request POST \
#  --url https://iad1.qualtrics.com/API/v3/libraries/UR_cTIvKxsmN7AzjL0/graphics \
#  --header 'Content-Type: multipart/form-data; boundary=---011000010111000001101001' \
#  --header 'X-API-TOKEN: A3BEG5Jxu8jX4ZEFnQtTokBatIyFXpt2gAz1UizM' \
#  --form file=@/Users/jonwang/Desktop/pic_1.png \
#  --form folder=foldername
