# Windows Dynamic Wallpaper
PowerShell script to change windows desktop wallpaper depending on time of day

## Setup
Install the packages in `requirements.txt`

Include the path to the wallpaper directory and wallpaper image paths in `config.ps1`

Add the full path of the PowerShell script to `script.vbs`

## Task Scheduler
Create a new task in Task Scheduler and use these Actions configurations
- Program/script: `wscript.exe`
- Add arguments (optional): `[full path of script.vbs]`
