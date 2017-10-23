
import unittest

from machinebox_api import MachineboxApi

class MachineBoxApiTest(unittest.TestCase):
    """
    Test case class
    """

    machinebox_url = "http://localhost:8080/"

    def test_create_machinebox_api(self):
        """Can create a the class without error
        """
        api = MachineboxApi(self.machinebox_url)

    def test_sample_image_can_be_posted(self):
        api = MachineboxApi(self.machinebox_url)
        api.check_tagbox("/home/glenn/Pictures/golf1.jpg")


    @unittest.skip
    def test_post_monkey_url_tagbox(self):
        api = MachineboxApi(self.machinebox_url)
        response = api.teach_tagbox("https://machinebox.io/samples/images/monkey.jpg", 'monkey.jpg', 'monkeys')
        json_data = response.json()
        self.assertTrue(json_data["success"])

if(__name__ == '__main__'):
    unittest.main()