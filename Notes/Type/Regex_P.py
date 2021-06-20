# 正则

import re
match = re.match('Hello[ \t]*(.*)world','Hello    Python world')
# re.match(正则条件,被匹配文本)
print(match.group(1)) # ——➤ Python (有一个空格)
# match.group(1)与正则规则一致，group(0)为全文
print(match.groups()) # ——➤ ('Python ',) | 列出所有的组，不包含全文，如果只有一个组，在后面加一个逗号来标识