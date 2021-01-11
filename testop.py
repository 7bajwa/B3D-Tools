import bpy

class Flatten(bpy.types.Operator):
    bl_idname = "view3d.flat_x"
    bl_label = ""
    bl_description = "Flatten the selection to a axis"

    def execute(self, context):
        bpy.ops.transform.resize(0,1,1)
        return {"FINISHED"}