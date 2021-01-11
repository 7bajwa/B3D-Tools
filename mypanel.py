import bpy
from . myfuncs import Vert_Op

class MyPanel(bpy.types.Panel):
    bl_idname = "Test_PT_Panel"
    bl_label = "Test Panel"
    bl_category = "BaajTools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("view3d.flat_x" , icon = "EVENT_X" )
        row.operator("view3d.flat_x" , icon = "EVENT_Y" )
        row.operator("view3d.flat_x" , icon = "EVENT_Z" )
        row = layout.row()
        row.operator(Vert_Op.bl_idname, icon = "GHOST_ENABLED" )



        #icon = "PIVOT_CURSOR"

# obj = bpy.context.active_object
# bpy.ops.object.editmode_toggle()
# bpy.ops.mesh.select_all(action='DESELECT')
# bpy.context.object.active_material_index = 1
# bpy.ops.object.material_slot_select()
# vg = obj.vertex_groups.new(name='Leaf')
# bpy.ops.object.vertex_group_assign()
# bpy.ops.object.editmode_toggle()
