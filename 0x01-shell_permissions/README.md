# 0x01. Shell, permissions
Learn goals
- What do the commands chmod, sudo, su, chown, chgrp do
- Linux file permissions
- How to represent each of the three sets of permissions (owner, group, and other) as a single digit
- How to change permissions, owner and group of a file
- Why cant a normal user chown a file
- How to run a command with root privileges
- How to change user ID or become superuser
---
# Files
Those are the files that you can find into this projects
| File | Features |
| ------ | ------ |
| **0-iam_betty** | Changes user ID to betty |
| **1-who_am_i** | Prints current user ID |
| **2-groups** | Prints all the groups the current ser is part of |
| **3-new_owner** | Changes the owner of the file hello to the user betty |
| **4-empty** | Creates an empty file called hello |
| **5-execute** | Adds execute permission to the owner of the file hello |
| **6-multiple_permissions** | Adds execute permission to the owner and the group owner, and read permission to other users, to the file hello | 
| **7-everybody** | Adds execution permission to the owner, the group owner and the other users, to the file hello |
| **8-James_Bond** | Script that sets the permission to the file hello, Owner to no permissionat all, Group to no permission at all, other to all permissions | 
| **9-John_Doe write** | Sets the mode of the file hello -rwxr-x-wx |
| **10-mirror_permissions** | Sets the mode of the file hello the same as ollehs mode |
| **11-directories_permissions** | Adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed | 
| **12-directory_permissions** | Creates a directory called dir_holberton with permissions 751 in the working directory |
| **13-change_group** | Changes the group owner to holberton for the file hello |
| **14-change_owner_and_group** | Changes the owner to betty and the group owner to holberton for all the files and directories in the working directory |
| **15-symbolic_link_permissions** | Changes the owner and the group owner of the file _hello to betty user and holberton group | 
| **16-if_only** | Changes the owner of the file hello to betty only if it is owned by the user guillaume | 
| **100-Star_Wars** | Plays the StarWars IV episode in the terminal |
