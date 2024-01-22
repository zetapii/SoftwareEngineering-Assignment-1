import unittest
from User import User
from IdentificationMethod import IdentificationMethod
from AuthenticationSystem import AuthenticationSystem, HashingAlgorithm
from enum import Enum

class TestAuthenticationSystem(unittest.TestCase):
    def setUp(self):
        self.auth_system_md5 = AuthenticationSystem(HashingAlgorithm.MD5)
        self.auth_system_sha5 = AuthenticationSystem(HashingAlgorithm.SH5)

    def test_register_user(self):
        user_md5 = self.auth_system_md5.register_user("user_md5", "password123", IdentificationMethod.StudentId, "")
        user_sha5 = self.auth_system_sha5.register_user("user_sha5", "password456", IdentificationMethod.StudentId, "")
        self.assertIsNotNone(user_md5)
        self.assertIsNotNone(user_sha5)

    def test_register_duplicate_user(self):
        self.auth_system_md5.register_user("user_md5", "password123", IdentificationMethod.StudentId, "")
        duplicate_user = self.auth_system_md5.register_user("user_md5", "password456", IdentificationMethod.StudentId, "")
        self.assertIsNone(duplicate_user)

    def test_login_user(self):
        self.auth_system_md5.register_user("user_md5", "password123", IdentificationMethod.StudentId, "")
        logged_in_user_md5 = self.auth_system_md5.login_user("user_md5", "password123")
        self.assertIsNotNone(logged_in_user_md5)

        self.auth_system_sha5.register_user("user_sha5", "password456", IdentificationMethod.AadharCard, "")
        logged_in_user_sha5 = self.auth_system_sha5.login_user("user_sha5", "password456")
        self.assertIsNotNone(logged_in_user_sha5)

    def test_login_invalid_user(self):
        self.auth_system_md5.register_user("user_md5", "password123", IdentificationMethod.PANCard, "")
        logged_in_user_md5 = self.auth_system_md5.login_user("user_md5", "wrong_password")
        self.assertIsNone(logged_in_user_md5)

if __name__ == '__main__':
    unittest.main()
