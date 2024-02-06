import os

from dotenv import load_dotenv

import utils
from utils import file, allure


load_dotenv()

remote_url = os.getenv('remote_url', 'http://127.0.0.1:4723/wb/hub')
appWaitActivity = os.getenv('appWaitActivity', 'org.wikipedia.*')
app = os.getenv('app', './app-alpha-universal-release.apk')
runs_on_bstack = app.startswith('bs://')
if runs_on_bstack:
    deviceName = os.getenv('deviceName')
    remote_url = 'http://hub.browserstack.com/wd/hub'
    app = 'bs://sample.app'
bstack_userName = os.getenv('LOGIN')
bstack_accessKey = os.getenv('PASSWORD')


def to_driver_options():
    from appium.options.android import UiAutomator2Options
    options = UiAutomator2Options()

    # if deviceName:
    #     options.set_capability('deviceName', deviceName)
    if runs_on_bstack:
        options.set_capability('deviceName', deviceName)

    if appWaitActivity:
        options.set_capability('appWaitActivity', appWaitActivity)

    options.set_capability('app', (
        app if (app.startswith('/') or runs_on_bstack)
        else utils.file.abs_path_from_project(app)
        # else ut
    ))

    if runs_on_bstack:
        options.set_capability('platformVersion', '9.0')
        options.set_capability(
            'bstack:options', {
                'projectName': 'First Python project',
                'buildName': 'browserstack-build-1',
                'sessionName': 'BStack first_test',

                'userName': bstack_userName,
                'accessKey': bstack_accessKey,
            },
        )

    return options