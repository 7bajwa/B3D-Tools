# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "BaajTools",
    "author" : "7Bajwa",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy



# classes = (Flatten , MyPanel)

register_classes = []
register_operators = []

from . testop import Flatten
register_classes.append(Flatten)
from . mypanel import MyPanel
register_classes.append(MyPanel)
from . myfuncs import Vert_Op
register_operators.append(Vert_Op)

# register , unregister = bpy.utils.register_classes_factory(classes)

def register():
    for c in register_classes:
        bpy.utils.register_class(c)
    for o in register_operators:
        bpy.utils.register_class(o)

def unregister():
    for c in register_classes:
        bpy.utils.unregister_class(c)
    for o in register_operators:
        bpy.utils.unregister_class(o)