# PROJNAME

PROJdesc

<!-- /!\ Alpha, work in progress -->

**[Download latest](https://github.com/Pullusb/REPO_NAME/archive/master.zip)**

<!-- ### [Demo Youtube]() -->

---  

## Description

Quick usage description

**tool action** : `SHORTCUT`


### Where ?

Where is the stuff in UI or shortcut


---

# How to use this template

Make some case sensitive search and replace at folder level (`Ctrl + Shift + F` in _VScode_):
`PROJNAME` : The name of the addon, contain spaces, preferably in `Title Case`, This is in the `bl_info` for legacy addon and in `manifest.toml` the title of the readme
`PROJdesc` : Short Description of what the addon does. in bl_info, manifest.toml and below title in readme 

---

# Blender multifile-addon development tips

> those are just my own tips from experience, not considered good or recommended practice

### Split in sub-modules for big things
If it's a mutli-purpose addon and there are clear modules separation:
Create a folder per _modules_ as if those were separated addons, with following structure

```
Addon_folder/
|- a_module/
|    |- __init__.py
|    |- ops.py
|    |- ui.py
|
|- another_module/
     |- __init__.py
     |- ops.py
     |- ui.py
     |- props.py
     |- something_specific.py
```

That way it's easier to work on that part of the addon  
It can easily become a full standalone one (not that much useful, but still get a point)  


### Prefer relative imports against absolute

What's bests often comes down to project needs and personal preferences, but Blender extension specify that the imports have to be relative.


### import shared resources from library files

Whether you use sub-folders or not in your hierarchy, at the root it's always practical to have resources that are shared by everything

ex: If you have some hardcoded values you want to reuse over multiple files, like `GP = GREASEPENCIL` (bad example, but hey... better than nothing)  
create a `constants.py` containing those, then in other files, use `from .constant import GP` (`from ..constant import GP` if the file is in a subfolder).

Same things for the reused functions, you can create a `utils.py` and import function from them.  

Avoid importing everything with wildcard `from .utils import *`, as it can become really confusing not knowing the source of an import. If not for you, at list for the linter ;)  
Better to use `from .utils import compute_range, invert_lists`

I personnally prefer to directly import the source itself, so I know exactly where it comes from without bothering importing specifics.
examples:

```python
from . import utils

# Then used like this
utils.compute_range(args)
```

About naming convention, those generic library are generally named `utils`, `resources`, `lib`, or `helpers`  
Ehere - another a personal choice - I like to name it `fn.py` (when it's only keeping function).  
It's shorter to write the imports and feels right to call function like this `fn.compute_range(args)`

Note: When you have various type of lib in this file,it can be interesting to split it as well, same as the operator file.  
ex: all drawing utilities in a `draw.py` file, etc.  

<!-- can add further notes about register order and logging methods -->