# ctl = LayoutCtl.quick(TableLayout,
#                       [
#                           [TextView('t1', 'Hello World!', width=Width.fill, back=Back.blue, style=Style.bright)],
#                           [TextView('t2', '', fore=Fore.magenta)],
#                       ],
#                       )
# # TextView('','style',style=Style.dim)

# layout = ctl.find_view_by_id('root')
# layout.set_width(20)

# ctl.draw(auto_re_draw=False)

# ctl.find_view_by_id('t2').set_text('你好,世界!')
# ctl.re_draw()

# time.sleep(0.5)
# row3 = TableRow.quick_init('', [TextView('t3', 'こんにちは、世界!')])
# layout.add_view(row3)
# ctl.re_draw()

# @click.group(invoke_without_command=True)
# @click.pass_context
# def main():
#     pass

# @main.command()
# def test():
#     print("Test")

# @click.command()
# def default():
#     print("default")

# # @click.command()
# # def main():
# #     print("test")

# if __name__ == '__main__':
#     default()
#     main()