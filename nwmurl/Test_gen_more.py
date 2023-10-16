import os
import unittest
from urlgennwm import generate_urls  # Import the generate_urls function from your script

class TestGenerateURLs(unittest.TestCase):
    def test_generate_urls_for_analysis_assim(self):
        # Define test input values
        start_date = "202201120000"
        end_date = "202201130000"
        fcst_cycle = [0, 8]
        lead_time = [1, 18]
        varinput = 1
        geoinput = 1
        runinput = 5  # Set to 5 for the analysis_assim folder
        urlbaseinput = 2
        meminput = 1

        # Call the function to generate URLs
        generate_urls(start_date, end_date, fcst_cycle, lead_time, varinput, geoinput, runinput, urlbaseinput, meminput)

        # Check if the generated 'filenamelist.txt' file exists
        self.assertTrue(os.path.exists("filenamelist.txt"))

        # Define the expected URLs or patterns for the analysis_assim folder
       # Define the expected URLs or patterns for the analysis_assim folder
        expected_urls = [
            "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/post-processed/WMS/nwm.20220112/analysis_assim/nwm.t00z.analysis_assim.channel_rt.tm001.conus.nc",
            "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/post-processed/WMS/nwm.20220112/analysis_assim/nwm.t00z.analysis_assim.channel_rt.tm018.conus.nc",
            # Add more expected URLs here for the analysis_assim folder
        ]

        # Read the content of the file and check for the expected content
        with open("filenamelist.txt", "r") as file:
            content = file.read()
            for url in expected_urls:
                self.assertIn(url, content)
                
                
class TestGenerateURLsAnalysisAssimExtend(unittest.TestCase):
    def test_generate_urls_for_analysis_assim_extend(self):
        # Define test input values for the "analysis_assim_extend" folder
        start_date = "202201120000"
        end_date = "202201130000"
        fcst_cycle = [16]  # Set to the desired forecast cycle for this folder
        lead_time = [28]  # Set to the desired lead time for this folder
        varinput = 1  # Adjust if you're using a different variable
        geoinput = 1  # Adjust if you're using a different geography
        runinput = 6  # Set to 6 for the analysis_assim_extend folder
        urlbaseinput = 2  # Adjust if you're using a different URL base
        meminput = 1  # Adjust if you're using a different member

        # Call the function to generate URLs for the "analysis_assim_extend" folder
        generate_urls(start_date, end_date, fcst_cycle, lead_time, varinput, geoinput, runinput, urlbaseinput, meminput)

        # Check if the generated 'filenamelist.txt' file exists
        self.assertTrue(os.path.exists("filenamelist.txt"))

        # Define the expected URLs or patterns for the "analysis_assim_extend" folder
        expected_urls = [
            "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/post-processed/WMS/nwm.20220112/analysis_assim_extend/nwm.t16z.analysis_assim_extend.channel_rt.tm028.conus.nc",
            # Add more expected URLs here for the analysis_assim_extend folder
        ]

        # Read the content of the file and check for the expected content
        with open("filenamelist.txt", "r") as file:
            content = file.read()
            for url in expected_urls:
                self.assertIn(url, content)

                
class TestGenerateURLsForcingMediumRange(unittest.TestCase):
    def test_generate_urls_for_forcing_medium_range(self):
        # Define test input values for the "forcing_medium_range" folder
        start_date = "202201120000"
        end_date = "202201130000"
        fcst_cycle = [0, 12]  # Set to the desired forecast cycle for this folder
        lead_time = [6, 120]  # Set to the desired lead time for this folder
        varinput = 5  # Use the variable code for "forcing"
        geoinput = 1  # Adjust if you're using a different geography
        runinput = 2  # Set to 2 for the medium_range folder
        urlbaseinput = 1  # Correct the base URL to match your expectation
        meminput = 1  # Adjust if you're using a different member
    
        # Call the function to generate URLs for the "forcing_medium_range" folder
        generate_urls(start_date, end_date, fcst_cycle, lead_time, varinput, geoinput, runinput, urlbaseinput, meminput)
    
        # Check if the generated 'filenamelist.txt' file exists
        self.assertTrue(os.path.exists("filenamelist.txt"))

class TestGenerateURLsAnalysisAssimAlaska(unittest.TestCase):
    def test_generate_urls_for_analysis_assim_alaska(self):
        # Define test input values for the "analysis_assim_alaska" folder
        start_date = "202201120000"
        end_date = "202201130000"
        fcst_cycle = [0, 8]
        lead_time = [1, 18]
        varinput = 1
        geoinput = 2  # Set to 2 for Alaska
        runinput = 5  # Set to 5 for the analysis_assim folder
        urlbaseinput = 2  # Adjust the URL base as needed
        meminput = 1  # Adjust if you're using a different member

        # Call the function to generate URLs for the "analysis_assim_alaska" folder
        generate_urls(start_date, end_date, fcst_cycle, lead_time, varinput, geoinput, runinput, urlbaseinput, meminput)

        # Check if the generated 'filenamelist.txt' file exists
        self.assertTrue(os.path.exists("filenamelist.txt"))

        # Define the expected URLs or patterns for the "analysis_assim_alaska" folder
        expected_urls = [
            # Add expected URLs for the analysis_assim_alaska folder
        ]

        # Read the content of the file and check for the expected content
        with open("filenamelist.txt", "r") as file:
            content = file.read()
            for url in expected_urls:
                self.assertIn(url, content)



if __name__ == '__main__':
    unittest.main()
