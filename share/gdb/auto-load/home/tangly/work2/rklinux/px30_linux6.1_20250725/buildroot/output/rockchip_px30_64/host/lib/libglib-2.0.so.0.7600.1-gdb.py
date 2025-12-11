import sys
import gdb

# Update module path.
dir_ = '/home/tangly/work2/rklinux/px30_linux6.1_20250725/buildroot/output/rockchip_px30_64/host/share/glib-2.0/gdb'
if not dir_ in sys.path:
    sys.path.insert(0, dir_)

from glib_gdb import register
register (gdb.current_objfile ())
