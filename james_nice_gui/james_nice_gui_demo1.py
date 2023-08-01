from nicegui import ui
from ex4nicegui.reactive import rxui
from ex4nicegui import to_ref

# 定义数据
input = to_ref('')

# 界面
rxui.input('输入内容', value=input)
rxui.label(input).bind_color(input)
ui.run()
