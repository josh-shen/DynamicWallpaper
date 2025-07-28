# Windows Dynamic Wallpaper
Script to change windows desktop wallpaper depending on time of day

![wallpaper](images/Appearances.gif)

## Setup
Add the full path to the `images` directory in config.ps1 

Add the full path of `wallpaper.ps1` to script.vbs

## Task Scheduler
Create a new task in Task Scheduler with these configurations

### Triggers
- Begin the task: At log on
- Repeat task every: 1 minute, for a duration of: Indefinetly

### Actions
- Program/script: `wscript.exe`
- Add arguments (optional): `[full path of script.vbs]`
