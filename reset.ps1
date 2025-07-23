# reset desktop settings
$desktopKey = "HKCU:\Control Panel\Desktop"
Set-ItemProperty -Path $desktopKey -Name "WallpaperStyle" -Value "10"
Set-ItemProperty -Path $desktopKey -Name "TileWallpaper" -Value "0"

# force a settings refresh
Stop-Process -Name "explorer" -Force -ErrorAction SilentlyContinue
Start-Sleep -Seconds 2
Start-Process "explorer"