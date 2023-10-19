import os
import unittest
from urlgennwm import generate_urls  # Import the generate_urls function from your script

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


if __name__ == '__main__':
    unittest.main()
