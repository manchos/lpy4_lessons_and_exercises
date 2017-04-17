import httpie
import re
# http api.openweathermap.org/data/2.5/weather?q=London
expr  = '2113'
try:
    m2 = re.search(r'201\d+', expr)
    print(m2.group(0))
except:
    print('2016')
# '(\s*(\d+\s*[+-\\*\\/]\s*\d+\s*)=)'