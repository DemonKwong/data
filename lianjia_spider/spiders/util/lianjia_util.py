import base64
import hashlib


def create_header(url):
    header = {
        "Page-Schema": "ershou%2Fhomepage",
        "Referer": "homepage",
        "extension": "lj_imei=860339913215340&lj_duid=DuZW1Cn2HyoGrSTKqUBjqjUjhLcjoNObSjFcKzWbC22FN4MUJePWUsYOr/se1CyTP+UhIw0HGPde2AtyfgYfrtEQ&lj_android_id=6056041830393841&lj_device_id_android=860339913215340&mac_id=02:00:00:00:00:02",
        "User-Agent": "HomeLink9.4.4;HUAWEI DUK-AL20; Android 5.1.1",
        "Lianjia-Channel": "Android_baidupinzhuannei_m",
        "Lianjia-Device-Id": "860339913215340",
        "Lianjia-Version": "9.4.4",
        "Lianjia-City-Id": "440100",
        "Authorization": get_authorization_str(url),
        "Lianjia-Im-Version": "2.35.0",
        "Host": "app.api.lianjia.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "lianjia_udid": "860339913215340",
        "lianjia_ssid": "ee19ce68-5c84-4d47-925c-5946de6f5bea",
        "lianjia_uuid": "2b756fe2-9bc5-4b12-8de3-4511945259a2"
    }
    return header


def get_authorization_str(url):
    param_array = url.split("?")[1].split("&")
    param_dict = {}
    for param in param_array:
        array = param.split("=")
        if len(array) == 2:
            param_dict[array[0]] = array[1]
        elif len(array) == 1:
            param_dict[array[0]] = ""
    param_key_list = list(param_dict.keys())
    param_key_list.sort()
    sb = "93273ef46a0b880faf4466c48f74878f"
    for key in param_key_list:
        sb = sb+key+"="+param_dict[key]
    md = hashlib.sha1()
    md.update(sb.encode())
    sb_byte_array = md.digest()
    sb = ""
    for b in sb_byte_array:
        hex_str = str(hex(b))[2:]
        if len(hex_str) < 2:
            sb += "0"
        sb += hex_str
    sb = "20170324_android:"+sb
    return base64.b64encode(sb.encode()).decode()


print(create_header("https://app.api.lianjia.com/house/ershoufang/detailpart1v1?house_code=108401258069&fb_expo_id=&is_hot=0"))


