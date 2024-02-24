# no more duplicate code 
# one general function to iterate through list
def get_names(objects):
    names = []
    for obj in objects:
        name = f"{obj.name.first_name} {obj.name.last_name}"
        names.append(name)
    return names

team_members = TeamMember.objects.all()
managers = Manager.objects.all()

manager_names = get_names(managers)
team_member_names = get_names(team_members)
