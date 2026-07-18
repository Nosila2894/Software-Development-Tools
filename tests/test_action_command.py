import unittest
from utility import ActionCommand 

class TestActionCommand(unittest.TestCase):

    def test_action_command_init_with_data_defaults(self):
        good_data = [
            None,
            {},
            {"part_1" : "Phantom Blood"},
            {"part_2" : "Battle Tendency", "part_3" : "Stardust Crusaders"}
            ]

        for data in good_data:
            with self.subTest(value_test=data):
                action_command_instance = ActionCommand("JoJo", data)
                self.assertEqual(action_command_instance.action, "JoJo")
                self.assertEqual(action_command_instance.action_data, data if data is not None else {})

    def test_action_command_init_with_invalid_action_parameter(self):
        bad_data = [
            123,
            ["Poorly", "Packaged"],
            False,
            42.24,
            {"insert_joke" : "DATA NOT FOUND"},
            None
            ]

        for data in bad_data:
            with self.subTest(value_test=data):
                with self.assertRaises(TypeError):
                    ActionCommand(data, {"no strings": "ULTRON"})

    def test_action_command_init_with_invalid_action_data_parameter(self):
        bad_data = [
            123,
            ["Package", "Broken", "Return to Sender"],
            False,
            42.24,
            "Postal",
            ]
        for data in bad_data:
            with self.subTest(value_test=data):
                with self.assertRaises(TypeError):
                    ActionCommand("Wack", data)

    def test_action_command_repr(self):
        cmd = ActionCommand("Repression", {"trauma": "Childhood"})
        
        actual_repr = repr(cmd)

        expected_repr = "ActionCommand(type='Repression', data={'trauma': 'Childhood'})"

        self.assertEqual(actual_repr, expected_repr)

if __name__ == '__main__':
    unittest.main()
