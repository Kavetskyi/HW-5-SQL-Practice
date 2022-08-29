import re


print("===========  Task 1   ===========")
patt_1 = r"\+?[0-9\-\(\)]{7,20}"
text_1 = r"""
        Hello, my phone number is 251-65-23.
        Henry Ford was born July 30, 1863, on a farm in Springwells Township, Michigan.
        """

result_1 = re.findall(pattern=patt_1, string=text_1)
print(result_1)


print("===========  Task 2   ===========")
patt_2 = r"[a-zA-Z0-9_\.]{1,255}@[^\.][a-zA-Z0-9_\.]{1,255}[^\.\ ]"
text_2 = r"""
        Hello, my phone number is 251-65-23, e-mail: H.Ford@e_mail.com. 
        Code kfhkjhHgfJ8798@.kjfshgas.com
        """
result_2 = re.findall(pattern=patt_2, string=text_2)
print(result_2)


print("===========  Task 3   ===========")
patt_3 = r"\.0{1,2}"
text_3 = r"216.008.094.196"
result_3 = re.sub(pattern=patt_3, repl=".", string=text_3)
print(result_3)


print("===========  Task 4   ===========")
patt_4 = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
ip_adress = ["216.8.94.196", "0.0.0.0", "127.0.0.1", "216.8.94", "14.0..139", "153.192.392.84"]
for ip_adr in ip_adress:
    if len(re.findall(pattern=patt_4, string=ip_adr)) == 0:
        print(f"IP address {ip_adr} is invalid")
    else:
        str_ip_adr = re.split(r'\.+', ip_adr)
        if int(str_ip_adr[0]) < 256 and int(str_ip_adr[1]) < 256 and\
                int(str_ip_adr[2]) < 256 and int(str_ip_adr[3]) < 256:
            print(f"IP address {ip_adr} is valid")
        else:
            print(f"IP address {ip_adr} is invalid")


