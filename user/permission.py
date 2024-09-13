


class IsManagerOrSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name__in=['Manager', 'Superadmin']).exists()
    