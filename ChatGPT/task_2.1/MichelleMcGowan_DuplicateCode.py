team_members = TeamMember.objects.all()
managers = Manager.objects.all()
for m in managers:
        name = f"{m.name.first_name} {m.name.last_name}"
//reset of the code are the same
for t in team_members:
        name = f"{t.member.first_name} {t.member.last_name}"
//reset of the code are the same
