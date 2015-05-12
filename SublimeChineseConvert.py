'''
@name     SublimeChineseConvert
@package  sublime_plugin
@author   Rexdf

This Sublime Text 3 plugin adds Traditional/Simplified Chinese convert
features to the right click context menu.

Usage: Make a selection (or not), Choose menu
from the context menu.

'''

import sublime
import sublime_plugin
import os

OpenCC = None


BASE_PATH = os.path.abspath(os.path.dirname(__file__))
OPENCC_PATH = os.path.join(BASE_PATH, "OpenCC")


def get_opencc_path():
    """Return zipfile path according to platform."""
    platform = sublime.platform()
    arch = sublime.arch()
    version = sublime.version()
    if int(version) < 3000:
        sublime.message_dialog("Don't support Sublime Text 2")
    path = None
    if platform == "windows":
        if arch == "x32":
            path = "OpenCC_Win32.zip"
        elif arch == "x64":
            path = "OpenCC_Win64.zip"
    elif platform == "linux":
        if arch == "x32":
            path = "OpenCC_Linux32.zip"
        elif arch == "x64":
            path = "OpenCC_Linux64.zip"
    elif platform == "osx":
        path = "OpenCC_OSX.zip"
    return os.path.join(BASE_PATH, path)


def get_dict_arch_path():
    """Return Dict_arch.zip path."""
    arch = sublime.arch()
    if arch == "x32":
        return os.path.join(BASE_PATH, "Dict32.zip")
    elif arch == "x64":
        return os.path.join(BASE_PATH, "Dict64.zip")


def get_dict_path():
    """Return Dict.zip path."""
    return os.path.join(BASE_PATH, "Dict.zip")


def init():
    """Load or unzip OpenCC."""
    # PACKAGES_PATH = sublime.packages_path()
    # PACKAGE_NAME = __name__.split('.')[0]
    try:
        from .OpenCC import OpenCC
    except ImportError:
        import zipfile
        # mkdir if OPENCC_PATH not exist
        if not os.path.isdir(OPENCC_PATH):
            os.mkdir(OPENCC_PATH)
        # unzip Dict.zip
        DICT_PATH = get_dict_path()
        if os.path.isfile(DICT_PATH):
            with zipfile.ZipFile(DICT_PATH, "r") as f:
                f.extractall(OPENCC_PATH)
        # unzip Dict_arch.zip
        DICT_ARCH_PATH = get_dict_arch_path()
        if os.path.isfile(DICT_ARCH_PATH):
            with zipfile.ZipFile(DICT_ARCH_PATH, "r") as f:
                f.extractall(OPENCC_PATH)
        # unzip OpenCC pre-build binary
        ZIP_FILE_PATH = get_opencc_path()
        if os.path.isfile(ZIP_FILE_PATH):
            with zipfile.ZipFile(ZIP_FILE_PATH, "r") as f:
                f.extractall(OPENCC_PATH)
        try:
            from .OpenCC import OpenCC
        except ImportError:
            raise Exception("Can not load OpenCC, return")
            return
    globals()['OpenCC'] = OpenCC


class ChineseConvertCommand(sublime_plugin.TextCommand):

    def run(self, edit, to):
        view_size = self.view.size()
        regions = self.view.sel()
        num = len(regions)
        x = len(self.view.substr(regions[0]))
        if num <= 1 and x == 0:
            regions.clear()
            regions.add(sublime.Region(0, view_size))

        # support multi selection
        cc = Tradsim(to)
        for region in regions:
            input_string = self.view.substr(region)
            output_string = cc.convert(input_string)
            self.view.replace(edit, region, output_string)

        # self.view.end_edit(edit)


class Tradsim():

    def __init__(self, config="s2t.json"):
        config = os.path.join(OPENCC_PATH, config)
        self._handle = OpenCC.opencc_open(config)

    def convert(self, text):
        result = OpenCC.opencc_convert_utf8(self._handle, text,
                                            len(text.encode("utf-8")))
        return result

    def __del__(self):
        OpenCC.opencc_close(self._handle)


def plugin_loaded():
    """Load and unzip the pre-build binary files."""
    sublime.set_timeout(init, 200)
