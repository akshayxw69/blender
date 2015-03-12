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

# <pep8 compliant>

# Note: This will be a simple addon later, but until it gets to master, it's simpler to have it
#       as a startup module!

import bpy
from bpy.types import AssetEngine
from bpy.props import (
        StringProperty,
        BoolProperty,
        IntProperty,
        FloatProperty,
        EnumProperty,
        CollectionProperty,
        )

class AssetEngineFlame(AssetEngine):
    bl_label = "Flame"

    def __init__(self):
        self.jobs = {}

    def status(self, job_id):
        if job_id:
            job = self.jobs.get(job_id, None)
            #~ if job is not None:
                #~ return {'VALID'}
            return set()
        else:
            return {'VALID'}

    def progress(self, job_id):
        return 0.5

    def kill(self, job_id):
        pass

    def list_dir(self, job_id, entries):
        if len(entries.entries) == 0:
            entry = entries.entries.add()
            entry.type = {'BLENDER'}
            entry.relpath="foobar"
            variant = entry.variants.add()
            entry.variants.active = variant
            rev = variant.revisions.add()
            variant.revisions.active = rev
        return 1

if __name__ == "__main__":  # only for live edit.
    bpy.utils.register_module(__name__)
    bpy.utils.register_class(AssetEngineFlame)
