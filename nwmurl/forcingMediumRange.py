import os
import unittest
from urlgennwm import generate_urls  # Import the generate_urls function from your script
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

if __name__ == '__main__':
    unittest.main()
