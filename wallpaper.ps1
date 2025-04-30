. "$PSScriptRoot\config.ps1"

Function Write-Log($Message) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$timestamp - $Message" | Out-File -FilePath "$PSScriptRoot\log.txt" -Append
}

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

    $SPI_SETDESKWALLPAPER = 0x0014
    $UpdateIniFile = 0x01
    $SendChangeEvent = 0x02
  
    $fWinIni = $UpdateIniFile -bor $SendChangeEvent
  
    $ret = [Params]::SystemParametersInfo($SPI_SETDESKWALLPAPER, 0, $Image, $fWinIni)
    return $ret
}

$t_minute = (Get-Date).Hour * 60 + (Get-Date).Minute

try {
    # run Python script to setup time markers
    python setup.py
    $times = Get-Content -Path "$PSScriptRoot\times.txt"
} catch {
    Write-Log "ERROR: Failed to run Python script"
    exit 1
}

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

# Check if image exists at path
if (-not (Test-Path -Path $wallpaper_path -PathType Leaf)) {
    Write-Log "ERROR: No image was found at path: $wallpaper_path"
    exit 1
}

$result = Set-Wallpaper -Image $wallpaper_path

# get current wallpaper image path
$bytes = (New-Object -ComObject WScript.Shell).RegRead("HKEY_CURRENT_USER\Control Panel\Desktop\TranscodedImageCache"); 
$current_wallpaper = ([System.Text.Encoding]::Unicode.GetString($bytes[24..($bytes.length-1)]) -split "\0")[0]

# log results
if ($result -eq 0) {
    Write-Log "ERROR: Wallpaper change failed"
} else if ($result -eq 1 -and $current_wallpaper -ne $wallpaper_path) {
    Write-Log "${result}: Wallpaper changed from $current_wallpaper to $wallpaper_path"
}