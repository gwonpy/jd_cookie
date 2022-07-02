from layout import window_layout
import PySimpleGUI as sg
import images_base64
from playwright.sync_api import Playwright, sync_playwright
from threading import Thread
import pyperclip

def async_run(func):
    """
    通用异步执行装饰器

    Args:
        func: 运行的功能名称

    Returns:
        线程执行器

    """
    def wrapper(*args, **kwargs):
        thr = Thread(target=func, args=args, kwargs=kwargs)
        thr.start()
    return wrapper


'''
cookie字符串处理
'''
def get_cookie_str(cookies_ls: list) -> str:
    pt_key = ''
    pt_pin = ''
    for data in cookies_ls:
        if data.get('name') == 'pt_pin':
            pt_pin = data.get('value')
        if data.get('name') == 'pt_key':
            pt_key = data.get('value')
    return f'pt_key={pt_key};pt_pin={pt_pin}'

class JD:
    def __init__(self):
        sg.theme('Default1')
        self.window = sg.Window(title='jd获取cookie脚本  byZH', layout=window_layout, icon=images_base64.jd_icon)

    @async_run
    def jd_task(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto('https://bean.m.jd.com/bean/signIndex.action')
            page.wait_for_selector("text=签到日历", timeout=500000)
            cookies_ls = page.context.cookies()
            browser.close()
            jd_cookies = get_cookie_str(cookies_ls)
            self.window['cookie_info'].update(jd_cookies)
            return True

    def circle_event(self):
        while True:
            event, values = self.window.read(timeout=100)
            if event == '-run-':
                try:
                    if self.jd_task():
                        sg.popup_ok('获取cookie成功！')
                except Exception:
                    sg.popup_error('sorry！遇到了未知错误')
            if event == '-copy-':
                try:
                    if values['cookie_info']:
                        pyperclip.copy(values['cookie_info'])
                        sg.popup_quick_message('cookie已经复制到剪切板！', text_color='#2ecc71', font='3px')
                    else:
                        sg.popup_error('未检测到数据！')
                except Exception:
                    sg.popup_error('sorry！遇到了未知错误')
            if event in (sg.WIN_CLOSED, 'Exit'):
                break

if __name__ == '__main__':
    jd = JD()
    jd.circle_event()
