# models/level_model.py

roles = [
    (0, 'Pollito Bebé'),
    (10, 'Pollito Joven'),
    (20, 'Pollito Explorador'),
    (30, 'Pollito Aventurero'),
    (40, 'Pollito Guerrero'),
    (50, 'Pollito Maestro')
]

def get_role(level):
    """Return the role and next level up."""
    for role_level, role_name in reversed(roles):
        if level >= role_level:
            return role_name, role_level
    return roles[0][1], roles[0][0]


