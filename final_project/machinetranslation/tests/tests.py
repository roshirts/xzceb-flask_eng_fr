import unittest
from translator import english_to_french, french_to_english


class TestTranslatorFunctions(unittest.TestCase):
    def test_nul(self):
        self.assertEqual(english_to_french(None), None)
        self.assertEqual(french_to_english(None), None)

    def test_untranslatable(self):
        self.assertEqual(english_to_french("Viel Brot"), "Viel Brot")
        self.assertEqual(french_to_english("Viel Brot"), "Viel Brot")

    def test_space(self):
        self.assertEqual(english_to_french('  '), '  ')
        self.assertEqual(french_to_english('  '), '  ')

    def test_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_wrong(self):
        self.assertNotEqual(english_to_french('Frogs'), 'Myrtille')
        self.assertNotEqual(french_to_english('Myrtille'), 'Frogs')

    def test_newLine(self):
        self.assertEqual(english_to_french(
            "I like bread.\nStrawberry jam"),
            "J'aime le pain.\nConfiture de fraise"
        )
        self.assertEqual(french_to_english(
            "J'aime le pain.\nConfiture de fraise"),
            "I like bread.\nStrawberry jam"
        )


if __name__ == '__main__':
    unittest.main()
