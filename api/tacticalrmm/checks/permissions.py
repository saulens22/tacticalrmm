from rest_framework import permissions

from tacticalrmm.permissions import _is_su


class ManageChecksPerms(permissions.BasePermission):
    def has_permission(self, r, view):
        if r.method == "GET":
            return True

        return _is_su(r) or r.user.can_manage_checks


class RunChecksPerms(permissions.BasePermission):
    def has_permission(self, r, view):
        return _is_su(r) or r.user.can_run_checks
