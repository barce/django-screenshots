import selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
import argparse


# This little function make screen size to maximum for better screenshot result
def save_screenshot(driver, path):
    original_size = driver.get_window_size()
    required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(required_width, required_height)
    try:
        driver.find_element_by_tag_name('body').screenshot(path)  # Avoids scrollbar
    except Exception as e:
        print(e)
    driver.set_window_size(original_size['width'], original_size['height'])

parser = argparse.ArgumentParser()
parser.add_argument("--url",
                    required=True)  # usage: python3 screenshot.py --url https://www.google.com/ --output /tmp/google.png
parser.add_argument("--output", required=True)
args = parser.parse_args()

if args.url:

    capabilities = webdriver.DesiredCapabilities().FIREFOX
    capabilities['acceptSslCerts'] = True  # This is for accepting self signed SSl certificates.
    opts = Options()
    driver = webdriver.Firefox(options=opts, executable_path="/usr/local/bin/geckodriver")
    driver.capabilities = capabilities
    driver.get(args.url)
    out_path = args.output
    save_screenshot(driver, out_path)  # Saving the screenshot
    driver.close()
else:
    parser.print_help()
