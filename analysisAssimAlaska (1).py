import os
import pytest
from urlgennwm import generate_urls

@pytest.fixture
def generated_urls():
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

    # Yield the generated 'filenamelist.txt' file
    yield

    # Optionally, you can add teardown code here if needed

def test_generate_urls_for_analysis_assim_alaska(generated_urls):
    # Check if the generated 'filenamelist.txt' file exists
    assert os.path.exists("filenamelist.txt")

    # Define the expected URLs or patterns for the "analysis_assim_alaska" folder
    expected_urls = [
        # Add expected URLs for the analysis_assim_alaska folder
    ]

    # Read the content of the file and check for the expected content
    with open("filenamelist.txt", "r") as file:
        content = file.read()
        for url in expected_urls:
            assert url in content
