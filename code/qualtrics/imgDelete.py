#!/Users/jonwang/miniconda3/bin/python
import http.client

conn = http.client.HTTPSConnection("iad1.qualtrics.com")

headers = {
    'Content-Type': "application/json",
    'X-API-TOKEN': "y938Vu56ku9UUnHRssFEnvnF6csQtkeTUA7WORfU"
    }

def delete(libid, imgid):
    conn.request("DELETE", "/API/v3/libraries/{}/graphics/{}".format(libid, imgid), headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

if __name__ == "__main__":
    libid = "UR_cTIvKxsmN7AzjL0"
    with open("deleteList.txt", "r") as deletefile:
        for line in deletefile:
            imgid = line.replace("\n", "")
            delete(libid, imgid)
