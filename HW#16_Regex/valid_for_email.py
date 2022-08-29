import re


def valid_email(email_):
    patt_01 = r"[a-zA-Z0-9_\.\-\+/!%]{1,64}@[^\.][a-zA-Z0-9\.\-\:\[\]]{1,255}[^\.\ ]"
    res_01 = re.findall(pattern=patt_01, string=email_)
    result = res_01[0] if len(res_01) > 0 else ''
    if result != email_:
        patt_12 = r' "@[^\.][a-zA-Z0-9\.]{1,255}[^\.\ ]'
        res_12 = re.findall(pattern=patt_12, string=email_)
        result = res_12[0] if len(res_12) > 0 else ''
        if result != email_:
            patt_14 = r'\"[\w]{1,64}\.{2}[\w]{1,64}\"@[^\.][a-zA-Z0-9\.]{1,255}[^\.\ ]'
            res_14 = re.findall(pattern=patt_14, string=email_)
            result = res_14[0] if len(res_14) > 0 else ''
            if result != email_:
                patt_15 = r'\"[a-zA-Z0-9_\.\\\"\ \W]{1,64}\"@[^\.][a-zA-Z0-9\.]{1,255}[^\.\ ]'
                res_15 = re.findall(pattern=patt_15, string=email_)
                result = res_15[0] if len(res_15) > 0 else ''
    return result


list_email = [
    r'simple@example.com', r'very.common@example.com', r'disposable.style.email.with+symbol@example.com',
    r'other.email-with-hyphen@example.com', r'fully-qualified-domain@example.com', r'user.name+tag+sorting@example.com',
    r'x@example.com', r'example-indeed@strange-example.com', r'test/test@test.com', r'admin@mailserver1',
    r'example@s.example', r'" "@example.org', r'"john..doe"@example.org', r'mailhost!username@example.org',
    r'"very.(),:;<>[]\".VERY.\"very@\\ \"very\".unusual"@strange.example.com', r'user%example.com@example.org',
    r'user-@example.org', r'postmaster@[123.123.123.123]', r'postmaster@[IPv6:2001:0db8:85a3:0000:0000:8a2e:0370:7334]',
    r'Abc.example.com', r'A@b@c@example.com', r'a"b(c)d,e:f;g<h>i[j\k]l@example.com', r'just"not"right@example.com ',
    r'this is"not\allowed@example.com', r'this\ still\"not\\allowed@example.com',
    r'1234567890123456789012345678901234567890123456789012345678901234+x@example.com',
    r'i_like_underscore@but_its_not_allowed_in_this_part.example.com', r'QA[icon]CHOCOLATE[icon]@test.com'
]

for email in list_email:
    val_inval = valid_email(email)
    if val_inval == email:
        print(f"E-mail: {email} is valid")
    else:
        print(f"E-mail: {email} is INVALID")
