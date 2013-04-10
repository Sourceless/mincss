mincss
======

A small project to minify css by removing repeated rules.

Usage
-----

Inside a python script, with mincss.py in the same dir or one on your PATH:
```python
import mincss

print mincss.minify("body{a:b;c:d;e:f;}head{a:b;e:f;g:h;}")
# => body{c:d;}head{g:h;}body,head{e:f;a:b;}
```

Or from the command line:
```
$ python mincss.py "body{a:b;c:d;e:f;}head{a:b;e:f;g:h;}"
body{c:d;}head{g:h;}body,head{e:f;a:b;}
```

Limitations
-----------

At the moment mincss only supports single selectors (if some are chained together with ',', they are taken as one big selector block). It'll also not cope well with SASS or LESS.

In addition it currently does not keep the rules in the order they're written, since it uses and iterates over dictionaries.
