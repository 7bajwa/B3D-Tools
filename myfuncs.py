import bpy

class Vert_Op(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.vert_operatoe"
    bl_label = "Simple Vertex Group Operator for trees"

    # @classmethod
    # def poll(cls, context):
    #     return context.active_object is not None

    def execute(self, context):
        obj = context.active_object
        obj.location = ( 0, 0, 0 )
        obj.rotation_euler = (0,15,0)
        # print(context.scene)
        # print(context.active_object)
        # obj = bpy.context.active_object
        # bpy.ops.object.editmode_toggle()
        # bpy.ops.mesh.select_all(action='DESELECT')
        # bpy.context.object.active_material_index = 1
        # bpy.ops.object.material_slot_select()
        # vg = obj.vertex_groups.new(name='Leaf')
        # bpy.ops.object.vertex_group_assign()
        # bpy.ops.object.editmode_toggle()
        return {'FINISHED'}
