import unittest
import sys
import os

# Add the Netflixer directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Netflixer')))

from user_agent.user_agent import UserAgentGenerator

class TestUserAgentGenerator(unittest.TestCase):

    def setUp(self):
        self.ua_generator = UserAgentGenerator()

    def test_get_random_user_agent(self):
        ua = self.ua_generator.get_random_user_agent()
        self.assertIsInstance(ua, str)
        self.assertGreater(len(ua), 0)

    def test_get_user_agents(self):
        ua_list = self.ua_generator.get_user_agents()
        self.assertIsInstance(ua_list, list)
        self.assertGreater(len(ua_list), 0)
        for ua in ua_list:
            self.assertIsInstance(ua, dict)
            self.assertIn('user_agent', ua)
            self.assertIsInstance(ua['user_agent'], str)
            self.assertGreater(len(ua['user_agent']), 0)

    def test_user_agent_uniqueness(self):
        ua_list = self.ua_generator.get_user_agents()
        unique_ua = set(ua['user_agent'] for ua in ua_list)
        self.assertEqual(len(ua_list), len(unique_ua), "User agents should be unique")

    def test_user_agent_content(self):
        ua = self.ua_generator.get_random_user_agent()
        self.assertTrue(any(browser in ua.lower() for browser in ['chrome', 'firefox', 'edge']),
                        "User agent should contain a known browser name")

if __name__ == '__main__':
    unittest.main()