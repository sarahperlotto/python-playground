
branch_names = [
  'HI-1474'
]
local_delete_command = 'git branch -D '
remote_delete_command = 'git push origin --delete '

local_commands = [local_delete_command + bn for bn in branch_names]
remote_commands = [remote_delete_command + bn for bn in branch_names]

print(*local_commands, sep='\n')
print(*remote_commands, sep='\n')

