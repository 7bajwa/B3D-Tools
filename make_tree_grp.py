import bpy

class Op_tree_grp(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.Op_tree_grp"
    bl_label = "Tree Group"

    # @classmethod
    # def poll(cls, context):
    #     return context.active_object is not None

    def execute(self, context):
        print(context.scene)
        print(context.active_object)
        return {'FINISHED'}
