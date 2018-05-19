# PythonGame

1. 需要先安装HomeBrew
    macOS安装过程：
        ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
2. 验证HomeBrew是否正常安装
    $brew doctor
    Your system is ready to brew
3. 开始安装 Pygame
    $brew install hg sdl sdl_image_sdl_ttf
    $brew install sdl_mixer_protmidi
    $pip3 install --user hg+http://bitbucket.org/pygame/pygame
