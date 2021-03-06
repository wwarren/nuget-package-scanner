import csv
import os
import unittest

import app
import nuget
from nuget import PackageContainer
from nuget import NetCoreProject
from nuget import PackageConfig

class TestApp(unittest.TestCase):
    TEST_CSV_PATH = os.path.join(os.path.dirname(__file__),'testoutput\\test-report.csv')

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.TEST_CSV_PATH)
        return super().tearDownClass()

    def test_write_to_csv(self):        
        csproj = open(os.path.join(os.path.dirname(__file__), 'sampledata\\sample.csproj')).read()
        config1 = NetCoreProject(csproj, "sample.csproj", "csproj-repo", "path/to/the/proj")

        pc = open(os.path.join(os.path.dirname(__file__), 'sampledata\\sample_packages.config')).read()
        config2 = PackageConfig(pc, "sample-package.config", "config-repo", "path/to/the/proj2")

        package_containers = [config1, config2] #type: List[PackageContainer]
                
        app.write_to_csv(package_containers, self.TEST_CSV_PATH)

        #Very naive testing. Essentially just making sure it's actually writing out a non-empty file
        with open(self.TEST_CSV_PATH) as csvfile:
            contents = csvfile.read()
            self.assertIsInstance(contents,str)
            self.assertTrue(contents)
        
if __name__ == '__main__':
    unittest.main()