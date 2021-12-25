import re

scripts = {
  "пауза any" : "playerctl --player=firefox%any,mpv%any,tdesktop%any,%any play-pause",
  "пауза браузер" : "playerctl --player=firefox%any,%any play-pause",
  "пауза телеграмм" : "playerctl --player=tdesktop%any,%any play-pause",
  "пауза видео" : "playerctl --player=mpv%any,%any play-pause",
}

script = ("пауза dsf")
