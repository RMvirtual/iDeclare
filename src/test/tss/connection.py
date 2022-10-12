import unittest
from src.main.tss import connection
from src.main.file_system.credentials import user_credentials


class TestTssApi(unittest.TestCase):
    def test_should_read_consignment_eori(self):
        consignment = "DEC000000001010576"
        eori_number = connection.read_consignment(consignment)
        correct_eori_number = user_credentials().graylaw_eori_number

        self.assertEqual(correct_eori_number, eori_number)


if __name__ == '__main__':
    unittest.main()
