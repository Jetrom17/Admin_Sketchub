import webview

class Api:
    def __init__(self):
        webview.settings['ALLOW_DOWNLOADS'] = True
        webview.settings['OPEN_EXTERNAL_LINKS_IN_BROWSER'] = False
        webview.settings['OPEN_DEVTOOLS_IN_DEBUG'] = False

    def read_cookies(self, window):
        cookies = window.get_cookies()
        for c in cookies:
            print(c.output())

    def on_close(self, window):
        result = window.create_confirmation_dialog('Question', 'Are you ok with this?')
        if result:
            print('User clicked OK')
        else:
            print('User clicked Cancel')

if __name__ == '__main__':
    api = Api()

    window = webview.create_window(
        'Admin',
        'https://admin.sketchub.in/',
        confirm_close=True
    )

    webview.start(user_agent='Chrome/51.0.2704.103', private_mode=False)
