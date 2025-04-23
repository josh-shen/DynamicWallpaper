# Windows Dynamic Wallpaper
Script to change windows desktop wallpaper depending on time of day

## Setup
Include the path to the wallpaper directory and wallpaper image paths in config.ps1

Add the full path of the powershell script to script.vbs

## Task Scheduler
Create a new task in Task Scheduler and use these configurations

### Triggers
Begin the task: At log on
Repeat task every: 1 minute, for a duration of: Indefinetly

### Actions
- Program/script: `wscript.exe`
- Add arguments (optional): `[full path of script.vbs]`