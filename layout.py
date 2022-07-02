import PySimpleGUI as sg
import images_base64
sg.theme('Default1')

def GraphicButton(text:str, key:str, image_data):
    text = text.replace('_', ' ')
    button = sg.Button('', image_data=image_data, button_color=('white', '#F1F1F1'), font='Any 15', key=key,
                       border_width=1)
    text = sg.Text(text, font='10px', size=(15, 1), justification='center', )
    return sg.Column([[button], [text]], element_justification='c')



window_layout = [
    [sg.Sizer(60, 0), GraphicButton('点击运行', key='-run-', image_data=images_base64.run_icon)],
    [sg.Text('cookie输出框', font='2px')],
    [sg.Multiline(size=(40, 3), key='cookie_info')],
    [sg.Sizer(60, 0), GraphicButton('点击复制', key='-copy-', image_data=images_base64.copy)]]


