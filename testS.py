# from terminal_layout.extensions.choice import *
# from terminal_layout import *

# c = Choice('Which is the Best Programming Language?',
#            ['Python', 'C/C++', 'Java', 'PHP', 'Go', 'JS', '...'],
#            icon_style=StringStyle(fore=Fore.blue),
#            selected_style=StringStyle(fore=Fore.blue),default_index=2)

# choice = c.get_choice()
# if choice:
#     index, value = choice
#     print(value, 'is the Best Programming Language')
print('导入nb_log之前的print是普通的')

from nb_log import get_logger

logger = get_logger('lalala',)   # get_logger 只有一个name是必传递的，其他的参数不是必传。
# logger = get_logger('lalala',log_filename='lalala.log',formatter_template=5,log_file_handler_type=2) # get_logger有很多其他入参可以自由定制logger。


logger.debug(f'debug是绿色，说明是调试的，代码ok ')
logger.info('info是天蓝色，日志正常 ')
logger.warning('黄色yello，有警告了 ')
logger.error('粉红色说明代码有错误 ')
logger.critical('血红色，说明发生了严重错误 ')

print('导入nb_log之后的print是强化版的可点击跳转的')