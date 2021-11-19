#---------------------------------------------------------------------------------------------------------------[import]
#$puzzle                 = [string](Get-Content .\testing.txt)
$puzzle                         = [string](Get-Content .\input.txt)
#------------------------------------------------------------------------------------------------------------[variables]
#format puzzle
$puzzle                         = $puzzle.Replace('contain', ' =').Replace('[ ]?bag[s]?[ ]?', '').Replace('.', "`n")
#convert to dictionary
$puzzle                         = ConvertFrom-StringData $puzzle
$bag                            = 'shiny gold'
$bagCount                       = 0
$countedBags                    = ''
# Master list of jobs you need to check the result of later
$jobs                           = New-Object System.Collections.Generic.List[System.Management.Automation.Job]
#---------------------------------------------------------------------------------------------------------[Calculations]
function get-bags {
    param ($bag)
    
    foreach ($key in $puzzle.keys) {
        if ($puzzle.$key -match $bag) {
            $global:bagCount    += 1
            $newBag             = $key 
            $global:countedBags += ($newBag.replace(' ','_') + ' ')
            $job = Start-Job -ScriptBlock {get-bags $newBag}
            if (-not ($global:countedBags -contains $newBag.replace(' ','_'))){[void]$jobs.Add($job)} #Write-Host $puzzle.$key
        }
    } #END foreach $key in $puzzle

}
get-bags $bag
write-host "bag count =" $bagCount

# Wait for the jobs to be done
Write-Host 'Waiting for all jobs to complete...'
while( $jobs | Where-Object { $_.State -eq 'Running' } ){
  Start-Sleep -s 10
}

<# WRONG ANSWERS:
                    625

#>