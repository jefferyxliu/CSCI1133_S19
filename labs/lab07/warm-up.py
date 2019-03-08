Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = " There... are... a... lot ...of: delimiters,,, Ryan?!!!"
>>> for x in s:
	if x in '.:,?!':
		s = s.replace(x,'')

		
>>> s
' There are a lot of delimiters Ryan'
>>> s = s.rstrip()
>>> s
' There are a lot of delimiters Ryan'
>>> s = s.lstrip()
>>> s
'There are a lot of delimiters Ryan'
>>> s[:29]
'There are a lot of delimiters'
>>> s = s[:29] + ', Fred'
>>> s
'There are a lot of delimiters, Fred'
>>> s = s.split()
>>> s
['There', 'are', 'a', 'lot', 'of', 'delimiters,', 'Fred']
>>> 
