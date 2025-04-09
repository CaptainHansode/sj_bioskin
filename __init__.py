# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "SJ Bio Skin",
    "author": "CaptainHansode",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location":  "View3D > Sidebar > Tool Tab",
    "description": "Weight paint support tool.",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Rigging",
}


import bpy
import collections
import json
import os
import re
import numpy
import math
from bpy.app.handlers import persistent
from bpy_extras.io_utils import ExportHelper


def edit_mode_toggle(self, context):
    r"""頂点選択の切り替え"""
    if context.scene.sj_bioskin_props.select_ver_mode:
        context.object.data.use_paint_mask_vertex = True
        bpy.ops.wm.tool_set_by_id(name="builtin.select_box")
    else:
        context.object.data.use_paint_mask_vertex = False
        bpy.ops.wm.tool_set_by_id(name="builtin_brush.Draw")


class SJBioSkinProperties(bpy.types.PropertyGroup):
    r"""カスタムプロパティを定義する"""
    b_name: bpy.props.StringProperty(name="Name", default="")

    selected_only: bpy.props.BoolProperty(name="Selected Only", default=False)
    add_vg_forcibly: bpy.props.BoolProperty(name="AddVertsG", default=False)

    # ポジション閾値
    bpy.props.FloatProperty()
    pos_threshold: bpy.props.FloatProperty(
        name="Threshold", 
        default=0.0001, min=0.0, max=10.0, step=0.01, precision=5)
    # 閾値
    normalize_threshold: bpy.props.FloatProperty(
        name="Threshold", 
        default=0.001, min=0.0001, max=0.1, step=0.01, precision=4)

    at_vert_pos: bpy.props.BoolProperty(name="At Vert Pos", default=False)
    # 今は考えない
    # at_world_pos: bpy.props.BoolProperty(name="At World Pos", default=False)

    select_ver_mode: bpy.props.BoolProperty(
        default=False, update=edit_mode_toggle)

# bpy.types.WindowManager.my_operator_toggle = bpy.props.BoolProperty(
#                                                  default = False,
#                                                  update = update_function)


class SJBioSkinBweight0(bpy.types.Operator):
    r"""Set paint blush"""
    bl_idname = "object.sj_bioskin_brushweight0"
    bl_label = "Weight 0"

    def execute(self, context):
        r""""""
        context.scene.tool_settings.unified_paint_settings.weight = 0.0
        return {'FINISHED'}


class SJBioSkinBweight01(bpy.types.Operator):
    r"""Set paint blush"""
    bl_idname = "object.sj_bioskin_brushweight01"
    bl_label = "Weight 0."

    def execute(self, context):
        r""""""
        context.scene.tool_settings.unified_paint_settings.weight = 0.1
        return {'FINISHED'}


class SJBioSkinBweight02(bpy.types.Operator):
    r"""Set paint blush"""
    bl_idname = "object.sj_bioskin_brushweight02"
    bl_label = "Weight 0.2"

    def execute(self, context):
        r""""""
        context.scene.tool_settings.unified_paint_settings.weight = 0.2
        return {'FINISHED'}


class SJBioSkinBweight03(bpy.types.Operator):
    r"""Set paint blush"""
    bl_idname = "object.sj_bioskin_brushweight03"
    bl_label = "Weight 0.3"

    def execute(self, context):
        r""""""
        context.scene.tool_settings.unified_paint_settings.weight = 0.3
        return {'FINISHED'}


class SJBioSkinBweight04(bpy.types.Operator):
    r"""Set paint blush"""
    bl_idname = "object.sj_bioskin_brushweight04"
    bl_label = "Weight 0.4"

    def execute(self, context):
        r""""""
        context.scene.tool_settings.unified_paint_settings.weight = 0.4
        return {'FINISHED'}


class SJBioSkinBweight05(bpy.types.Operator):
    r"""Set paint blush"""
    bl_idname = "object.sj_bioskin_brushweight05"
    bl_label = "Weight 0.5"

    def execute(self, context):
        r""""""
        context.scene.tool_settings.unified_paint_settings.weight = 0.5
        return {'FINISHED'}


class SJBioSkinBweight06(bpy.types.Operator):
    r"""Set paint blush"""
    bl_idname = "object.sj_bioskin_brushweight06"
    bl_label = "Weight 0.6"

    def execute(self, context):
        r""""""
        context.scene.tool_settings.unified_paint_settings.weight = 0.6
        return {'FINISHED'}


class SJBioSkinBweight07(bpy.types.Operator):
    r"""Set paint blush"""
    bl_idname = "object.sj_bioskin_brushweight07"
    bl_label = "Weight 0.7"

    def execute(self, context):
        r""""""
        context.scene.tool_settings.unified_paint_settings.weight = 0.7
        return {'FINISHED'}


class SJBioSkinBweight08(bpy.types.Operator):
    r"""Set paint blush"""
    bl_idname = "object.sj_bioskin_brushweight08"
    bl_label = "Weight 0.8"

    def execute(self, context):
        r""""""
        context.scene.tool_settings.unified_paint_settings.weight = 0.8
        return {'FINISHED'}


class SJBioSkinBweight09(bpy.types.Operator):
    r"""Set paint blush"""
    bl_idname = "object.sj_bioskin_brushweight09"
    bl_label = "Weight 0.9"

    def execute(self, context):
        r""""""
        context.scene.tool_settings.unified_paint_settings.weight = 0.9
        return {'FINISHED'}


class SJBioSkinBweight1(bpy.types.Operator):
    r"""Set paint blush"""
    bl_idname = "object.sj_bioskin_brushweight10"
    bl_label = "Weight 1.0"

    def execute(self, context):
        r""""""
        context.scene.tool_settings.unified_paint_settings.weight = 1.0
        return {'FINISHED'}


class SJBioSkinBsize5(bpy.types.Operator):
    r"""Set paint blush"""
    bl_idname = "object.sj_bioskin_brushsize5"
    bl_label = "Brush Size 5"

    def execute(self, context):
        r""""""
        context.scene.tool_settings.unified_paint_settings.size = 5
        return {'FINISHED'}


class SJBioSkinBsize10(bpy.types.Operator):
    r"""Set paint blush"""
    bl_idname = "object.sj_bioskin_brushsize10"
    bl_label = "Brush Size 10"

    def execute(self, context):
        r""""""
        context.scene.tool_settings.unified_paint_settings.size = 10
        return {'FINISHED'}


class SJBioSkinBsize20(bpy.types.Operator):
    r"""Set paint blush"""
    bl_idname = "object.sj_bioskin_brushsize20"
    bl_label = "Brush Size 20"

    def execute(self, context):
        r""""""
        context.scene.tool_settings.unified_paint_settings.size = 20
        return {'FINISHED'}


class SJBioSkinBsize35(bpy.types.Operator):
    r"""Set paint blush"""
    bl_idname = "object.sj_bioskin_brushsize35"
    bl_label = "Brush Size 35"

    def execute(self, context):
        r""""""
        context.scene.tool_settings.unified_paint_settings.size = 35
        return {'FINISHED'}


class SJBioSkinBsize50(bpy.types.Operator):
    r"""Set paint blush"""
    bl_idname = "object.sj_bioskin_brushsize50"
    bl_label = "Brush Size 50"

    def execute(self, context):
        r""""""
        context.scene.tool_settings.unified_paint_settings.size = 50
        return {'FINISHED'}


class SJBioSkinBsize80(bpy.types.Operator):
    r""""""
    bl_idname = "object.sj_bioskin_brushsize80"
    bl_label = "Brush Size 80"

    def execute(self, context):
        r""""""
        context.scene.tool_settings.unified_paint_settings.size = 80
        return {'FINISHED'}


class SJBioSkinBsize120(bpy.types.Operator):
    r""""""
    bl_idname = "object.sj_bioskin_brushsize120"
    bl_label = "Brush Size 120"

    def execute(self, context):
        r""""""
        context.scene.tool_settings.unified_paint_settings.size = 120
        return {'FINISHED'}


class SJBioSkin(object):
    r"""ウェイト設定"""
    def __init__(self, *args, **kwargs):
        # obj = args[0]
        pass

    def def_weight_table(self):
        return {
            "info": {
                "description": 0
            },
            "object": {
                "name": "",
                "matrix_world": []  # WM用
            },
            "vertex_group": {
                # 0: "BoneA",
                # 1: "BoneB"
            },
            "weight_table": {
                # 0: {
                #     "position": [0, 0, 0],
                #     "weights": {
                #         3: 0.20,
                #         2: 0.80
                #     }
                # }
            }
        }

    def remove_all_vertex_groups(self, obj):
        r"""全ての頂点グループを削除"""
        return True
    
    def remove_all_vertex_group_assign(self, obj, v_list):
        r"""頂点のウェイト情報を削除"""
        # 頂点が属しているグループ情報を一度削除する
        for v_grp in obj.vertex_groups:
            v_grp.remove(v_list)
        return True

    def get_weight_table(self, obj=None, verts=[]):
        r"""渡された頂点のデータから"""
        ret = self.def_weight_table()
        ret["object"]["name"] = obj.name
        wm = obj.matrix_world
        ret["object"]["matrix_world"].append([wm[0].x, wm[0].y, wm[0].z, wm[0].w])
        ret["object"]["matrix_world"].append([wm[1].x, wm[1].y, wm[1].z, wm[1].w])
        ret["object"]["matrix_world"].append([wm[2].x, wm[2].y, wm[2].z, wm[2].w])
        ret["object"]["matrix_world"].append([wm[3].x, wm[3].y, wm[3].z, wm[3].w])

        idx = 0
        for v_grp in obj.vertex_groups:
            ret["vertex_group"][idx] = v_grp.name
            idx += 1  # weight_table

        for v in verts:
            ret["weight_table"][v.index] = {}
            ret["weight_table"][v.index]["position"] = [v.co.x, v.co.y, v.co.z]
            ret["weight_table"][v.index]["weights"] = {}
            for g in v.groups:
                ret["weight_table"][v.index]["weights"][g.group] = g.weight

        return ret

    def save_weight_table(self, path, w_data):
        r"""頂点テーブルを読み込み"""
        # path = "D:\\Prj_SJTools\\SJTools\\dcc\\blender\\sj_bioskin\\test.json"
        save_file = open(path, 'w')
        json.dump(w_data, fp=save_file, indent=4)
        save_file.close()
        return True

    def load_weight_table(self, obj, w_matrix):
        r"""頂点テーブルを読み込み"""
        if os.path.exists(self.path) is False:
            pass
        return True

    def get_mirror_vert(self, sel_verts, tag_verts, thrld=0.0001):
        r"""ミラー側の頂点を取得"""
        td = thrld
        ret_v = []
        for sv in sel_verts:  # 総当たり検索
            sp = sv.co
            for tv in tag_verts:
                tp = tv.co
                if ((tp.x - td) <= -sp.x) and (-sp.x <= (tp.x + td)):
                    if ((tp.y - td) <= sp.y) and (sp.y <= (tp.y + td)):
                        if ((tp.z - td) <= sp.z) and (sp.z <= (tp.z + td)):
                            ret_v.append(tv)
        return ret_v

    def mirror_selection(self, obj, thrld=0.0001):
        r""""""
        mesh = obj.data
        # ミラー側の頂点（検索対象）
        # m_verts = [v for v in mesh.vertices if v.co.x < 0.0]
        sel_verts = [v for v in mesh.vertices if v.select]
        ret = self.get_mirror_vert(sel_verts, mesh.vertices, thrld)
        for sv in sel_verts:
            sv.select = False  # deselect
        for v in ret:
            v.select = True
        return True

    def replace_mirror_name(self, src_name):
        r"""左右の名前入れ替え あとでなんとかする"""
        if re.match(r".+(\.L$)", src_name) is not None:
            return re.sub(r'\.L$', '.R', src_name)
        if re.match(r".+(\.R$)", src_name) is not None:
            return re.sub(r'\.R$', '.L', src_name)
        if re.match(r".+(\.l$)", src_name) is not None:
            return re.sub(r'\.l$', '.r', src_name)
        if re.match(r".+(\.r$)", src_name) is not None:
            return re.sub(r'\.r$', '.l', src_name)
        return src_name

    def err_report(
        self, err_a="", err_b="", err_c="", title="Message", icon='INFO'):
        def draw(self, context):
            # self.layout.label(text="Not Found Vertex Group.")
            self.layout.label(text=err_a)
            # self.layout.label(text="Failed mirroring.")
            self.layout.label(text=err_b)
            self.layout.label(text=err_c)
        bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)

    def mirror_weight(self, obj, thrld=0.0001, sel_only=False, add_vg=True):
        r"""ウェイトテーブルでウェイトを設定"""
        # 頂点毎なので遅いはず
        mesh = obj.data
        if sel_only:
            src_verts = [
                v for v in mesh.vertices if v.select and v.co.x > 0.0 + thrld]
        else:
            src_verts = [v for v in mesh.vertices if v.co.x > 0.0 + thrld]
        
        dist_verts = [v for v in mesh.vertices if v.co.x < 0.0]  # 貼り付け側
        # dist_idx = [v.index for v in mesh.vertices if v.co.x < 0.0 - thrld]

        # ウェイトテーブルを作成 必要ないかも
        w_table = self.get_weight_table(obj, src_verts)

        # 反対側の頂点のグループをクリア 選択がある場合は
        # dist_idx = [v.index for v in self.get_mirror_vert(src_verts, dist_verts)]
        # self.remove_all_vertex_group_assign(obj, dist_idx)
        
        sel_verts = []  # 最後に選択する
        err_verts = []  # 最後の報告用
        notfound_bone = []  # 骨が見つからない

        for v in w_table["weight_table"]:
            # 見つかるのは一つだけのハズ
            m_v = self.get_mirror_vert([mesh.vertices[v]], dist_verts)
            if len(m_v) == 0:  # ミラー頂点が見つからない
                err_verts.append(v)
                continue

            m_v = m_v[0]
            self.remove_all_vertex_group_assign(obj, [m_v.index])
                
            for wv in w_table["weight_table"][v]["weights"]:
                # グループ名をミラー
                g_name = self.replace_mirror_name(w_table["vertex_group"][wv])
                w = w_table["weight_table"][v]["weights"][wv]  # ウェイト値

                if g_name in obj.vertex_groups:  # グループが存在していれば
                    vg = obj.vertex_groups[g_name]
                    vg.add([m_v.index], w, 'REPLACE')
                else:
                    if add_vg:  # 強制的に作成するか?
                        bpy.ops.object.vertex_group_add()
                        obj.vertex_groups[-1].name = g_name
                        vg = obj.vertex_groups[g_name]
                        vg.add([m_v.index], w, 'REPLACE')
                    else:
                        notfound_bone.append(g_name)

            sel_verts.append(m_v)

        for v in sel_verts:
            v.select = True

        # 失敗を報告
        if len(err_verts) != 0 or len(notfound_bone) != 0:
            msg_vg = "Not found {} vertex group".format(len(set(notfound_bone)))
            msg_v = "Failed {} vertex weights mirroring".format(len(err_verts))
            # msg_vg = ", ".join(notfound_bone)
            # er_v = [str(n) for n in err_verts]
            # msg_v = "Failed {} vertex  weights mirroring. {}".format(
            #     len(err_verts), ",".join(er_v))
            # g_name
            self.err_report(
                err_a=msg_vg, err_b=msg_v, title="Note.", icon="INFO")

        return True

    def get_close_vertices_from_w_table(self, v, w_table):
        r"""近い頂点を見つける"""
        ret_v = "0"
        vp = v.co

        # まずはベクトルリストを作る
        vec = []
        for v in w_table["weight_table"]:
            tp = w_table["weight_table"][v]["position"]
            vec.append(
                math.sqrt(
                    ((vp.x - tp[0]) ** 2) + ((vp.y - tp[1]) ** 2) + ((vp.z - tp[2]) ** 2)))

        return numpy.argmin(vec)

    def set_weight_at_vert_pos(self, obj, w_table, sel_only=False):
        r"""近しい位置の頂点のウェイトで読み込み"""
        # 頂点毎なので遅いはず
        mesh = obj.data
        if sel_only:
            dist_verts = [v for v in mesh.vertices if v.select]  # 貼り付け側
            dist_idx = [v.index for v in mesh.vertices if v.select]
        else:
            dist_verts = [v for v in mesh.vertices]  # 貼り付け側
            dist_idx = [v.index for v in mesh.vertices]

        self.remove_all_vertex_group_assign(obj, dist_idx)
        
        sel_verts = []  # 最後に選択する

        for v in dist_verts:
            # 必ず1つは見つかる キー値はストリングなので変換
            v_idx = str(self.get_close_vertices_from_w_table(v, w_table))
            # ウェイト割り当て
            for wv in w_table["weight_table"][v_idx]["weights"]:
                w = w_table["weight_table"][v_idx]["weights"][wv]
                g_name = w_table["vertex_group"][wv]  # グループ名
                if (g_name in obj.vertex_groups) is False:
                    bpy.ops.object.vertex_group_add()
                    obj.vertex_groups[-1].name = g_name
                vg = obj.vertex_groups[g_name]
                vg.add([v.index], w, 'REPLACE')
            sel_verts.append(v)

        for v in sel_verts:
            v.select = True

        return True

    def set_weight(
        self, obj, w_table, thrld=0.0001, at_vert_pos=False, at_w_matrix=False):
        r"""ウェイトテーブルでウェイトを設定"""
        mesh = obj.data
        dist_idx = [v.index for v in mesh.vertices]

        # 全部除去
        self.remove_all_vertex_group_assign(obj, dist_idx)
        err = False

        if len(mesh.vertices) != len(w_table["weight_table"]):
            err = True
            msg_a = "Number of vertices do not match. {} {}".format(
                len(mesh.vertices), len(w_table["weight_table"]))

        cnt = 0
        # for v in range(0, len(w_table["weight_table"])):
        for v in w_table["weight_table"]:
            if cnt > len(mesh.vertices):
                break
            for wv in w_table["weight_table"][v]["weights"]:
                g_name = w_table["vertex_group"][wv]  # グループ
                w = w_table["weight_table"][v]["weights"][wv]  # ウェイト値

                if (g_name in obj.vertex_groups) is False:  # グループがない
                    bpy.ops.object.vertex_group_add()
                    obj.vertex_groups[-1].name = g_name

                vg = obj.vertex_groups[g_name]
                vg.add([int(v)], w, 'REPLACE')
            cnt += 1

        if err:
            self.err_report(err_a=msg_a, title="Note.", icon="INFO")

        return True

    def remove_weights_sel_verts(self, obj):
        r"""選択した頂点のウェイトをクリア"""
        dist_idx = [v.index for v in obj.data.vertices if v.select]
        self.remove_all_vertex_group_assign(obj, dist_idx)
        return True

    def test_run(self, obj):
        return True


class SJBioSkinSelectMore(bpy.types.Operator):
    bl_idname = "object.select_more"
    bl_label = "More"
    bl_description = "Select more"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        pre_m = bpy.context.object.mode
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.select_more()
        bpy.ops.object.mode_set(mode=pre_m)
        return {'FINISHED'}


class SJBioSkinSelectLess(bpy.types.Operator):
    bl_idname = "object.select_less"
    bl_label = "Less"
    bl_description = "Select less"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        pre_m = bpy.context.object.mode
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.select_less()
        bpy.ops.object.mode_set(mode=pre_m)
        return {'FINISHED'}


class SJBioSkinSelectRing(bpy.types.Operator):
    bl_idname = "object.select_ring"
    bl_label = "Ring"
    bl_description = "Select ring"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        pre_m = bpy.context.object.mode
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.loop_multi_select(ring=False)
        bpy.ops.object.mode_set(mode=pre_m)
        return {'FINISHED'}


class SJBioSkinSelectLoop(bpy.types.Operator):
    bl_idname = "object.select_loop"
    bl_label = "Loop"
    bl_description = "Select loop"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        pre_m = bpy.context.object.mode
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.loop_multi_select(ring=True)
        bpy.ops.object.mode_set(mode=pre_m)
        return {'FINISHED'}


class SJBioSkinSelectX(bpy.types.Operator):
    r"""select X"""
    bl_idname = "object.sj_bioskin_select_x"
    bl_label = "Sel X"
    bl_description = "Select X"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        r""""""
        thrld = context.scene.sj_bioskin_props.pos_threshold
        mesh = context.active_object.data
        verts = [v for v in mesh.vertices if v.co.x > 0.0 + thrld]
        for v in verts:
            v.select = True
        return {'FINISHED'}


class SJBioSkinSelectMinusX(bpy.types.Operator):
    r"""select -X"""
    bl_idname = "object.sj_bioskin_select_minus_x"
    bl_label = "Sel -X"
    bl_description = "Select -X"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        r""""""
        thrld = context.scene.sj_bioskin_props.pos_threshold
        mesh = context.active_object.data
        verts = [v for v in mesh.vertices if v.co.x < 0.0 - thrld]
        for v in verts:
            v.select = True
        return {'FINISHED'}


class SJBioSkinSelectionMirror(bpy.types.Operator):
    r"""selection mirror"""
    bl_idname = "object.sj_bioskin_selection_mirror"
    bl_label = "Selection Mirror"
    bl_description = "Selection mirror"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        r""""""
        # sjbs_props = context.scene.sj_bioskin_props
        sjbs = SJBioSkin()
        sjbs_props = context.scene.sj_bioskin_props
        sjbs.mirror_selection(context.active_object, sjbs_props.pos_threshold)
        return {'FINISHED'}


class SJBioSkinSelectionInvert(bpy.types.Operator):
    r"""Selection invert"""
    bl_idname = "object.sj_bioskin_selection_invert"
    bl_label = "Invert"
    bl_description = "Selection invert"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        r""""""
        bpy.ops.paint.vert_select_all(action='INVERT')
        return {'FINISHED'}


class SJBioSkinDeselect(bpy.types.Operator):
    r"""select deselect"""
    bl_idname = "object.sj_bioskin_deselect"
    bl_label = "Deselect"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        r""""""
        return context.active_object is not None

    def execute(self, context):
        r""""""
        mesh = context.active_object.data
        for v in mesh.vertices:
            v.select = False
        return {'FINISHED'}


class SJBioSkinRemoveWeight(bpy.types.Operator):
    r"""selection mirror"""
    bl_idname = "object.sj_bioskin_remove_weight"
    bl_label = "Remove Weight"
    bl_description = "Remove Weight"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        r""""""
        return context.active_object is not None

    def execute(self, context):
        r""""""
        sjbs = SJBioSkin()
        sjbs.remove_weights_sel_verts(context.active_object)
        return {'FINISHED'}


class SJBioSkinNormalize(bpy.types.Operator):
    r"""Weight normalize"""
    bl_idname = "object.sj_bioskin_remove_amount_weight"
    bl_label = "Remove small amount weight"
    bl_description = "Remove small amount weight"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        r""""""
        return context.active_object is not None

    def execute(self, context):
        r""""""
        sjbs = SJBioSkin()
        sjbs.remove_weights_sel_verts(context.active_object)
        return {'FINISHED'}


class SJBioSkinMirror(bpy.types.Operator):
    r"""set mirror"""
    bl_idname = "object.sj_bioskin_mirror"
    bl_label = "Mirror Weight"
    bl_description = "Mirroring Weights"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        r""""""
        return context.active_object is not None

    def execute(self, context):
        r""""""
        sjbs_p = context.scene.sj_bioskin_props
        sjbs = SJBioSkin()
        # round(number[, ndigits])
        sjbs.mirror_weight(
            context.active_object,
            sjbs_p.pos_threshold,
            sjbs_p.selected_only,
            sjbs_p.add_vg_forcibly)
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)  # 再描画
        return {'FINISHED'}


class SJBioSkinSave(bpy.types.Operator, ExportHelper):
    bl_idname = "sjbioskin.save"
    bl_label = "Save Skin Weight"
    bl_description = "Save skin weight table."
    filename_ext = ".json"
    bl_options = {'UNDO', 'PRESET'}

    def execute(self, context):
        filepath = self.filepath
        # path = "D:\\Prj_SJTools\\SJTools\\dcc\\blender\\sj_bioskin\\test.json"
        sjbs = SJBioSkin()
        obj = context.active_object
        w_data = sjbs.get_weight_table(obj, obj.data.vertices)
        save_file = open(filepath, 'w')
        json.dump(w_data, fp=save_file, indent=4)
        save_file.close()
        return{'FINISHED'}


class SJBioSkinLoad(bpy.types.Operator, ExportHelper):
    bl_idname = "sjbioskin.load"
    bl_label = "Load Skin Data"
    bl_description = "Load skin weight table."
    filename_ext = ".json"
    bl_options = {'UNDO', 'PRESET'}

    def execute(self, context):
        filepath = self.filepath
        if os.path.exists(filepath) is False:
            return{'FINISHED'}

        load_file = open(filepath, 'r')
        w_data = json.load(
            load_file, object_pairs_hook=collections.OrderedDict)
        load_file.close()

        obj = context.active_object
        sjbs = SJBioSkin()
        sjbs_p = context.scene.sj_bioskin_props

        if sjbs_p.at_vert_pos:
            sjbs.set_weight_at_vert_pos(obj, w_data, sjbs_p.selected_only)
        else:
            sjbs.set_weight(obj, w_data)
        print("aasdasdasdasdasdasd")
        return{'FINISHED'}


class SJBioSkinAssistPanel(bpy.types.Panel):
    r"""UI"""
    bl_label = "SJ Bio Skin Paint Assist"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'  # UIのタイプ
    bl_context = "weightpaint"
    bl_category = 'Tool'
    # bl_category = 'SJTools'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        sjsp = context.scene.sj_bioskin_props

        row = layout.row(align=True)
        row.label(text="Weight")
        row.operator("object.sj_bioskin_brushweight0", text="0")
        row.operator("object.sj_bioskin_brushweight01", text="0.1")
        row.operator("object.sj_bioskin_brushweight02", text="0.2")
        row.operator("object.sj_bioskin_brushweight03", text="0.3")
        row.operator("object.sj_bioskin_brushweight04", text="0.4")
        row.operator("object.sj_bioskin_brushweight05", text="0.5")
        row.operator("object.sj_bioskin_brushweight06", text="0.6")
        row.operator("object.sj_bioskin_brushweight07", text="0.7")
        row.operator("object.sj_bioskin_brushweight08", text="0.8")
        row.operator("object.sj_bioskin_brushweight09", text="0.9")
        row.operator("object.sj_bioskin_brushweight10", text="1.0")
        row = layout.row(align=True)
        row.label(text="Radius")
        row.operator("object.sj_bioskin_brushsize5", text="5")
        row.operator("object.sj_bioskin_brushsize10", text="10")
        row.operator("object.sj_bioskin_brushsize20", text="20")
        row.operator("object.sj_bioskin_brushsize35", text="35")
        row.operator("object.sj_bioskin_brushsize50", text="50")
        row.operator("object.sj_bioskin_brushsize80", text="80")
        row.operator("object.sj_bioskin_brushsize120", text="120")


class SJBioSkinSelectPanel(bpy.types.Panel):
    r"""UI"""
    bl_label = "SJ Bio Skin Select Assist"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'  # UIのタイプ
    bl_context = "weightpaint"
    bl_category = 'Tool'
    # bl_category = 'SJTools'

    # bpy.ops.object.vertex_weight_copy
    # bpy.ops.paint.weight_paint_toggle()
    # bpy.types.Panel.bl_context
    # bpy.ops.object.vertex_weight_normalize_active_vertex()

    def draw(self, context):
        r""""""
        scene = context.scene
        sjbs = context.scene.sj_bioskin_props
        obj = context.active_object

        layout = self.layout
        row = layout.row(align=True)
        row.scale_y = 1.2
        
        lb = "Vertex Select"
        ic = "VERTEXSEL" if sjbs.select_ver_mode else "SELECT_SET"
        row.prop(sjbs, 'select_ver_mode', text=lb, icon=ic, toggle=True)
        # bpy.ops.wm.tool_set_by_id(name="builtin.select_box")
        # bpy.ops.wm.tool_set_by_id(name='builtin.cursor')
        # layout.operator("wm.tool_set_by_id").name = "builtin.select_box"

        row = layout.row(align=True)
        row.operator("object.sj_bioskin_deselect", icon="RESTRICT_SELECT_ON")
        row.operator("object.sj_bioskin_selection_invert", text="Invert", icon="ANCHOR_CENTER")

        row = layout.row(align=True)
        # 標準機能の選択拡充を追加
        row.operator("object.select_more", text="Add", icon="ADD")
        row.operator("object.select_less", text="Less", icon="REMOVE")

        row.operator("object.select_ring", text="Ring", icon="CURVE_BEZCIRCLE")
        row.operator("object.select_loop", text="Loop", icon="CUBE")
        row = layout.row(align=True)

        row.operator("object.sj_bioskin_select_x")
        row.operator("object.sj_bioskin_select_minus_x")
        row.operator(
            "object.sj_bioskin_selection_mirror", text="Mirror", icon="MOD_MIRROR")


# class SomeModalOperator(bpy.types.Operator):
#     bl_idname = "my.operator"
#     bl_label = "My Operator"
#     def modal(self, context, event):
#         print("running")
#         if not context.window_manager.my_operator_toggle:
#             context.window_manager.event_timer_remove(self._timer)
#             return {'FINISHED'}
#         return {'PASS_THROUGH'}
#     def invoke(self, context, event):
#         self._timer = context.window_manager.event_timer_add(0.01, context.window)
#         context.window_manager.modal_handler_add(self)
#         return {'RUNNING_MODAL'}
# def update_function(self, context):
#     if self.my_operator_toggle:
#         bpy.ops.my.operator('INVOKE_DEFAULT')
#     return


class SJBioSkinMirrorWeightPanel(bpy.types.Panel):
    r"""UI"""
    bl_label = "SJ Bio Skin Mirror Weight"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'  # UIのタイプ
    bl_context = "weightpaint"
    bl_category = 'Tool'
    # bl_category = 'SJTools'

    def draw(self, context):
        r""""""
        scene = context.scene
        sjbs = context.scene.sj_bioskin_props
        layout = self.layout
        row = layout.row()
        row.scale_y = 1.5
        row.operator("object.sj_bioskin_mirror", text="-X  <<  X")
        row = layout.row()
        row.scale_y = 1.5
        row.operator("object.sj_bioskin_mirror", text="-X  >>  X")
        row.enabled = False

        row = layout.row()
        row.operator("object.sj_bioskin_remove_weight", text="Remove Weight")

        row = layout.row()
        row.prop(sjbs, "selected_only", text="Selected Only")
        row.enabled = True

        row = layout.row()
        row.prop(sjbs, "add_vg_forcibly", text="Add Vertex Group Forcibly")
        # bl_description = "If the vertex group cannot be found, create it"
        row.enabled = True

        row = layout.row()
        row.prop(sjbs, "pos_threshold")


class SJBioSkinMirrorWeightPanel(bpy.types.Panel):
    r"""UI"""
    bl_label = "SJ Bio Skin Mirror Weight"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'  # UIのタイプ
    bl_context = "weightpaint"
    bl_category = 'Tool'
    # bl_category = 'SJTools'

    def draw(self, context):
        r""""""
        scene = context.scene
        sjbs = context.scene.sj_bioskin_props
        layout = self.layout
        row = layout.row()
        row.scale_y = 1.5
        row.operator("object.sj_bioskin_mirror", text="-X  <<  X")
        row = layout.row()
        row.scale_y = 1.5
        row.operator("object.sj_bioskin_mirror", text="-X  >>  X")
        row.enabled = False

        row = layout.row(align=True)
        row.prop(sjbs, "add_vg_forcibly", text="Add Vertex Group Forcibly")

        # row = layout.row(align=True)
        row.prop(sjbs, "selected_only", text="Selected Only")
        row.enabled = True

        row = layout.row()
        row.prop(sjbs, "pos_threshold")


class SJBioSkinSaveLoadPanel(bpy.types.Panel):
    r"""UI"""
    bl_label = "SJ Bio Skin Save Load"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'  # UIのタイプ
    bl_context = "weightpaint"
    bl_category = 'Tool'
    # bl_category = 'SJTools'

    def draw(self, context):
        scene = context.scene
        sjbs = context.scene.sj_bioskin_props
        layout = self.layout

        row = layout.row()
        row.operator("object.sj_bioskin_remove_weight", text="Remove Weight")

        # column = layout.column()
        row = layout.row(align=True)
        row.operator(
            "object.sj_bioskin_remove_amount_weight", text="Remove small amount weight")
        row.prop(sjbs, "normalize_threshold")
        row.enabled = False

        layout.separator(factor=2)

        row = layout.row(align=True)
        row.scale_y = 1.5
        row.operator("sjbioskin.save", text="Save", icon="EXPORT")

        row = layout.row(align=True)
        row.scale_y = 1.5
        row.operator("sjbioskin.load", text="Load", icon="IMPORT")

        # row.operator("export_scene.fbx", text="FBX")
        # print(operator.use_selection)
        # row.enabled = False

        row = layout.row(align=True)
        row.label(text="Option")

        col = layout.column(align=True)
        col.prop(sjbs, "selected_only")
        col.prop(sjbs, "at_vert_pos", text="Vertex Position")
        # row.prop(sjbs, "at_world_pos", text="At World Position")
        # row.enabled = False


class SJBioSkinWeightTable(bpy.types.Panel):
    r"""UI"""
    bl_label = "SJ Bio Skin Weight Table"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'  # UIのタイプ
    bl_context = "weightpaint"
    bl_category = 'Tool'
    # bl_category = 'SJTools'

    def draw(self, context):
        scene = context.scene
        sjsp = context.scene.sj_bioskin_props
        layout = self.layout
        row = layout.row()
        row.scale_y = 1.5
        row.operator("object.sj_bioskin_mirror", text="Weight Table")
        row.enabled = False


classes = (
    SJBioSkinProperties,
    SJBioSkinWeightTable,
    SJBioSkinMirror,
    SJBioSkinSelectRing, SJBioSkinSelectLoop,
    SJBioSkinSelectionMirror,
    SJBioSkinSelectX,
    SJBioSkinSelectMinusX,
    SJBioSkinDeselect,
    SJBioSkinSelectMore,
    SJBioSkinSelectLess,
    SJBioSkinSelectionInvert,
    SJBioSkinRemoveWeight,
    SJBioSkinNormalize,
    SJBioSkinSave, SJBioSkinLoad,

    SJBioSkinBsize5, SJBioSkinBsize10, SJBioSkinBsize20, SJBioSkinBsize35,
    SJBioSkinBsize50, SJBioSkinBsize80, SJBioSkinBsize120,

    SJBioSkinBweight0, SJBioSkinBweight01, SJBioSkinBweight02,
    SJBioSkinBweight03, SJBioSkinBweight04, SJBioSkinBweight05,
    SJBioSkinBweight06, SJBioSkinBweight07, SJBioSkinBweight08,
    SJBioSkinBweight09, SJBioSkinBweight1,
    SJBioSkinAssistPanel,
    SJBioSkinSelectPanel,
    SJBioSkinMirrorWeightPanel,
    SJBioSkinSaveLoadPanel
    )


# Register all operators and panels
def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.sj_bioskin_props = bpy.props.PointerProperty(
        type=SJBioSkinProperties)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.sj_bioskin_props


if __name__ == "__main__":
    register()
