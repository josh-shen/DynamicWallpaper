. "$PSScriptRoot\config.ps1"

Function Set-WallPaper($Image) {
 
Add-Type -TypeDefinition @" 
using System; 
using System.Runtime.InteropServices;
  
public class Params
{ 
    [DllImport("User32.dll",CharSet=CharSet.Unicode)] 
    public static extern int SystemParametersInfo (Int32 uAction, 
                                                   Int32 uParam, 
                                                   String lpvParam, 
                                                   Int32 fuWinIni);
}
"@  
    $ret = [Params]::SystemParametersInfo(0x14, 0, $Image, 0)
 
}

$t_minute = (Get-Date).Hour * 60 + (Get-Date).Minute

# run Python script to setup time markers
python setup.py

$times = Get-Content -Path "$PSScriptRoot\times.txt"

$wallpaper_path = switch ($t_minute) {
    {$_ -ge $times[0] -and $_ -lt $times[1]} {
        Join-Path -Path $wallpaper_directory -ChildPath $image1
    }
    {$_ -ge $times[1] -and $_ -lt $times[2]} {
        Join-Path -Path $wallpaper_directory -ChildPath $image2
    }
    {$_ -ge $times[2] -and $_ -lt $times[3]} {
        Join-Path -Path $wallpaper_directory -ChildPath $image3
    }
    {$_ -ge $times[3] -and $_ -lt $times[4]} {
        Join-Path -Path $wallpaper_directory -ChildPath $image4
    }
    {$_ -ge $times[4] -and $_ -lt $times[5]} {
        Join-Path -Path $wallpaper_directory -ChildPath $image5
    }
    {$_ -ge $times[5] -and $_ -lt $times[6]} {
        Join-Path -Path $wallpaper_directory -ChildPath $image6
    }
    {$_ -ge $times[6] -and $_ -lt $times[7]} {
        Join-Path -Path $wallpaper_directory -ChildPath $image7
    }
    {$_ -ge $times[7] -or $_ -lt $times[0]} {
        Join-Path -Path $wallpaper_directory -ChildPath $image8
    }
}

# get current wallpaper image path
$bytes = (New-Object -ComObject WScript.Shell).RegRead("HKEY_CURRENT_USER\Control Panel\Desktop\TranscodedImageCache"); 
$current_wallpaper = ([System.Text.Encoding]::Unicode.GetString($bytes[24..($bytes.length-1)]) -split "\0")[0]

if ($current_wallpaper -ne $wallpaper_path) {
    Set-Wallpaper -Image $wallpaper_path

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logMessage = "$timestamp - Changed wallpaper to: $wallpaper_path"
    $logMessage | Out-File -FilePath "$PSScriptRoot\log.txt" -Append
}
