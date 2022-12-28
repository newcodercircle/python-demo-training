import glob
import PySimpleGUI as sg
from cnocr import CnOcr
from threading import Thread

running = False


def make_window():
    layouts = [
        [
            sg.Input(key="-path-", size=(40, 8), disabled=True),
            sg.FolderBrowse("选择文件夹")
        ],
        [sg.Button("开始识别", key="-start-")],
        [sg.ProgressBar(max_value=100, key="-pregress-")]
    ]
    return sg.Window("批量图片文本识别工具", layouts, finalize=True)


def ocr(path):
    files = sum([glob.glob(path + "/" + i) for i in ["*.jpg", "*.jpeg", "*.png"]], [])
    n = len(files)
    ocr_model = CnOcr()
    out_file = path + "/" + "output.txt"
    for i in range(n):
        out = ocr_model.ocr(files[i])
        with open(out_file, "a+") as f:
            f.write(files[i])
            f.write(str(out))
    global running
    running = False


#
#
# files = sum([glob.glob(path + "/" + i) for i in ["*.jpg", "*.jpeg", "*.png"]], [])


if __name__ == '__main__':
    window = make_window()
    while True:
        event, values = window.read(timeout=50)
        if event == sg.WINDOW_CLOSED:
            break
        if event == "-start-" and not running:
            running = True
            path = window["-path-"].get()
            Thread(target=ocr, args=(path,), daemon=True).start()
