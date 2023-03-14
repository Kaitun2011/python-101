Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def checkege(friend):
...     for f in friend.items():
...         if f[1] >= 20:
...             print(f[0], f[1])
... 
...             
>>> friend = {'edward': 15,'jacob': 30,'tiger': 29, 'rita': 17}
>>> checkege(friend)
jacob 30
tiger 29
