# Detect OS using .NET API
$osPlatform = [System.Environment]::OSVersion.Platform

# Loop through IPs
for ($octet = 1; $octet -le 254; $octet++) {
    $ip = "192.168.0.$octet"

    # Choose ping command based on OS
    if ($osPlatform -eq "Win32NT") {
        $ping_output = ping -n 1 -w 1000 $ip
        $host_up = $ping_output -match "Reply from"
    }
    elseif ($osPlatform -eq "Unix" -or $osPlatform -eq "MacOSX") {
        $ping_output = ping -c 1 $ip
        $host_up = $ping_output -match "bytes from"
    }
    else {
        Write-Warning "Unsupported OS platform: $osPlatform"
        break
    }

    # Print if host is up
    if ($host_up) {
        Write-Host "Host up: $ip"
    }
}
