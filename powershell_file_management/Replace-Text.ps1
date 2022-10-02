$file = Read-Host "File Path"
$tempFile = [System.IO.Path]::GetTempFileName()

$targetText = "target text"
$replacementText = "replacement text"

Get-Content $file | 
    Foreach-Object {$_ -creplace $targetText, $replacementText} | 
    Add-Content $tempFile

Remove-Item $file
Move-Item $tempFile $file