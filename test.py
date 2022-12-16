import unittest

import database


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(1, 1)

    def test_database(self):
        db = database.Database()
        self.assertGreaterEqual(len(db.data["users"]), 3)

    def test_get_user(self):
        db = database.Database()
        user = db.get_user("admin")
        self.assertEqual(user["username"], "admin")

    def test_login(self):
        db = database.Database()
        self.assertTrue(db.login("admin", "password"))
        self.assertFalse(db.login("admin", "admin1"))
        self.assertFalse(db.login("admin1", "admin"))


if __name__ == '__main__':
    unittest.main()
