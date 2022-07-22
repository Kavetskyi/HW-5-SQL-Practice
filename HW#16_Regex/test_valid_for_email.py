import unittest
from valid_for_email import valid_email


class TestValidForEmail(unittest.TestCase):
    def test_valid_email_01(self):
        e_mail = r'simple@example.com'
        self.assertEqual(valid_email(e_mail), e_mail)

    def test_valid_email_02(self):
        e_mail = r'very.common@example.com'
        self.assertEqual(valid_email(e_mail), e_mail)

    def test_valid_email_03(self):
        e_mail = r'disposable.style.email.with+symbol@example.com'
        self.assertEqual(valid_email(e_mail), e_mail)

    def test_valid_email_04(self):
        e_mail = r'other.email-with-hyphen@example.com'
        self.assertEqual(valid_email(e_mail), e_mail)

    def test_valid_email_05(self):
        e_mail = r'fully-qualified-domain@example.com'
        self.assertEqual(valid_email(e_mail), e_mail)

    def test_valid_email_06(self):
        e_mail = r'user.name+tag+sorting@example.com'
        self.assertEqual(valid_email(e_mail), e_mail)

    def test_valid_email_07(self):
        e_mail = r'x@example.com'
        self.assertEqual(valid_email(e_mail), e_mail)

    def test_valid_email_08(self):
        e_mail = r'example-indeed@strange-example.com'
        self.assertEqual(valid_email(e_mail), e_mail)

    def test_valid_email_09(self):
        e_mail = r'test/test@test.com'
        self.assertEqual(valid_email(e_mail), e_mail)

    def test_valid_email_10(self):
        e_mail = r'admin@mailserver1'
        self.assertEqual(valid_email(e_mail), e_mail)

    def test_valid_email_11(self):
        e_mail = r'example@s.example'
        self.assertEqual(valid_email(e_mail), e_mail)

    def test_valid_email_12(self):
        e_mail = r'" "@example.org'
        self.assertEqual(valid_email(e_mail), e_mail)

    def test_valid_email_13(self):
        e_mail = r'"john..doe"@example.org'
        self.assertEqual(valid_email(e_mail), e_mail)

    def test_valid_email_14(self):
        e_mail = r'mailhost!username@example.org'
        self.assertEqual(valid_email(e_mail), e_mail)

    def test_valid_email_15(self):
        e_mail = r'"very.(),:;<>[]\".VERY.\"very@\\ \"very\".unusual"@strange.example.com'
        self.assertEqual(valid_email(e_mail), e_mail)

    def test_valid_email_16(self):
        e_mail = r'user%example.com@example.org'
        self.assertEqual(valid_email(e_mail), e_mail)

    def test_valid_email_17(self):
        e_mail = r'user-@example.org'
        self.assertEqual(valid_email(e_mail), e_mail)

    def test_valid_email_18(self):
        e_mail = r'postmaster@[123.123.123.123]'
        self.assertEqual(valid_email(e_mail), e_mail)

    def test_valid_email_19(self):
        e_mail = r'postmaster@[IPv6:2001:0db8:85a3:0000:0000:8a2e:0370:7334]'
        self.assertEqual(valid_email(e_mail), e_mail)

    def test_wvalid_email_01(self):
        e_mail = r'Abc.example.com'
        self.assertNotEqual(valid_email(e_mail), e_mail)

    def test_wvalid_email_02(self):
        e_mail = r'A@b@c@example.com'
        self.assertNotEqual(valid_email(e_mail), e_mail)

    def test_wvalid_email_03(self):
        e_mail = r'a"b(c)d,e:f;g<h>i[j\k]l@example.com'
        self.assertNotEqual(valid_email(e_mail), e_mail)

    def test_wvalid_email_04(self):
        e_mail = r'just"not"right@example.com'
        self.assertNotEqual(valid_email(e_mail), e_mail)

    def test_wvalid_email_05(self):
        e_mail = r'this is"not\allowed@example.com'
        self.assertNotEqual(valid_email(e_mail), e_mail)

    def test_wvalid_email_06(self):
        e_mail = r'this\ still\"not\\allowed@example.com'
        self.assertNotEqual(valid_email(e_mail), e_mail)

    def test_wvalid_email_07(self):
        e_mail = r'1234567890123456789012345678901234567890123456789012345678901234+x@example.com'
        self.assertNotEqual(valid_email(e_mail), e_mail)

    def test_wvalid_email_08(self):
        e_mail = r'i_like_underscore@but_its_not_allowed_in_this_part.example.com'
        self.assertNotEqual(valid_email(e_mail), e_mail)

    def test_wvalid_email_09(self):
        e_mail = r'QA[icon]CHOCOLATE[icon]@test.com'
        self.assertNotEqual(valid_email(e_mail), e_mail)


if __name__ == '__main__':
    unittest.main()
