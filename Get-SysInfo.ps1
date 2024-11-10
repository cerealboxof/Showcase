# Get-ComputerInfo | Format-List * | Out-File -FilePath C:\Scripts\SysInfo.txt


# Get-Volume | Format-List * | Out-File -FilePath C:\Scripts\SysInfo.txt -Append
# $Processor = Get-ComputerInfo | Select-Object CsProcessors
# $S = Out-String -InputObject $Processor
$P = [PSCustomObject]@{
    CsProcessors = (Get-ComputerInfo).CsProcessors
}
$P
Get-ComputerInfo | Select-Object CsName, CsModel, OsName, CsDomain, CsProcessors, CsPhyicallyInstalledMemory | Export-Csv C:\Scripts\SysInfo.csv -NoTypeInformation -Append
Get-ComputerInfo | Select-Object CsName, CsModel, OsName, CsDomain, CsProcessors, CsPhyicallyInstalledMemory | Out-File -FilePath C:\Scripts\SysInfo.txt -Append

# Get-ComputerInfo -Property "os" | Format-List * | Out-File -FilePath C:\Scripts\SysInfo.txt -Append