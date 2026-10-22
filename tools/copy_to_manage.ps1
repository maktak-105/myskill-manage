$srcDir = 'C:\Users\0120025-Z100\.gemini\antigravity-ide\brain\a3e97f15-97b9-4139-87a9-99685f0a833b'
$destDir = 'c:\Users\0120025-Z100\source\manage'

$files = @(
    'skill_and_tech_stack_history.md',
    'skill_and_capability_map.md',
    'skill_capability_map.html'
)

foreach ($f in $files) {
    $srcPath = Join-Path $srcDir $f
    $destPath = Join-Path $destDir $f
    if (Test-Path $srcPath) {
        Copy-Item -Path $srcPath -Destination $destPath -Force
        Write-Output "Copied: $f -> $destPath"
    }
}

Get-ChildItem -Path $destDir | Select-Object Name, Length, LastWriteTime
