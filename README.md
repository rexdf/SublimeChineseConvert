# SublimeChineseConvert

This is a Sublime Text plugin which implement the functionality of the Open Chinese Convert <https://github.com/BYVoid/OpenCC>. It provides translation between Traditional Chinese and Simplified Chinese.

Support multi selection.

![screenshot](https://raw.githubusercontent.com/rexdf/SublimeChineseConvert/readme/screenshot/SublimeChineseConvert.gif)

![screenshot](https://raw.githubusercontent.com/rexdf/SublimeChineseConvert/readme/screenshot/SublimeChineseConvert_OSX.gif)

![screenshot](https://raw.githubusercontent.com/rexdf/SublimeChineseConvert/readme/screenshot/SublimeChineseConvert_Linux.gif)

Install
-------
### Package Control
- See [here](http://wbond.net/sublime_packages/package_control) for instructions on installation of Package Control
- In Sublime Text, search for package 'ChineseOpenConvert'

### Manual
Clone this repository into `Sublime Text 3/Packages` using OS-appropriate location:

OSX:

    git clone https://github.com/rexdf/SublimeChineseConvert.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/ChineseOpenConvert

Windows:

    git clone https://github.com/rexdf/SublimeChineseConvert.git "%APPDATA%\Sublime Text 3\Packages\ChineseOpenConvert"

Linux:

    git clone https://github.com/rexdf/SublimeChineseConvert.git ~/.config/sublime-text-3/Packages/ChineseOpenConvert

Usage
-------

Press Ctrl+Shift+P to bring up the command input panel. Type in "Chinese" and you will see there are 10 commands provided.

    ChineseConvert: Simplified Chinese to Traditional Chinese
    ChineseConvert: Traditional Chinese to Simplified Chinese
    ChineseConvert: Simplified Chinese to Traditional Chinese (Taiwan Standard)
    ChineseConvert: Traditional Chinese (Taiwan Standard) to Simplified Chinese
    ChineseConvert: Simplified Chinese to Traditional Chinese (Hong Kong Standard)
    ChineseConvert: Traditional Chinese (Hong Kong Standard) to Simplified Chinese
    ChineseConvert: Simplified Chinese to Traditional Chinese (Taiwan Standard) with Taiwanese idiom
    ChineseConvert: Traditional Chinese (Taiwan Standard) to Simplified Chinese with Mainland Chinese idiom
    ChineseConvert: Traditional Chinese (OpenCC Standard) to Taiwan Standard
    ChineseConvert: Traditional Chinese (OpenCC Standard) to Hong Kong Standard

Choose the command that you want to run to perform the translation

Right click to get context menu or click on Main menu Click on menu Tools/Packages/繁简体转换:

    繁简体转换
        简体到繁體
        繁體到简体
        简体到臺灣正體
        臺灣正體到简体
        简体到香港繁體（香港小學學習字詞表標準）
        香港繁體（香港小學學習字詞表標準）到简体
        简体到繁體（臺灣正體標準）並轉換爲臺灣常用詞彙
        繁體（臺灣正體標準）到简体并转换为中国大陆常用词汇
        繁體（OpenCC 標準）到臺灣正體

Author & Contributors
---------------------
- [Rexdf](https://github.com/rexdf/SublimeChineseConvert)
- [Carbo Kuo](https://github.com/BYVoid/OpenCC)

## License

Copyright (C) 2015 Rexdf. MIT License.