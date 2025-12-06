$sw = [Diagnostics.Stopwatch]::StartNew()
py -m "day_$($args[0]).main" $args[1]
$sw.Stop()
Write-Host "Execution took $($sw.Elapsed.TotalMilliseconds) ms." -ForegroundColor cyan