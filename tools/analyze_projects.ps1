$ErrorActionPreference = 'SilentlyContinue'
$root = '~\source\project'

$results = @()

Get-ChildItem -Path $root -Directory | ForEach-Object {
    $dir = $_
    $name = $dir.Name
    if ($name -eq '.vscode') { return }

    $firstDate = $dir.CreationTime
    $lastDate = $dir.LastWriteTime
    $gitFound = $false
    $firstCommit = ''
    $lastCommit = ''
    $commitCount = 0

    $gitDir = Join-Path $dir.FullName '.git'
    if (Test-Path $gitDir) {
        $gitFound = $true
        try {
            $logFirst = git -C $dir.FullName log --reverse --format="%ad" --date=format:"%Y-%m-%d" 2>$null | Select-Object -First 1
            $logLast = git -C $dir.FullName log -n 1 --format="%ad" --date=format:"%Y-%m-%d" 2>$null
            $count = (git -C $dir.FullName rev-list --count HEAD 2>$null)
            if ($logFirst) { $firstCommit = $logFirst }
            if ($logLast) { $lastCommit = $logLast }
            if ($count) { $commitCount = [int]$count }
        } catch {}
    }

    # 各種設定ファイル検出
    $files = Get-ChildItem -Path $dir.FullName -Recurse -File -Depth 3 -ErrorAction SilentlyContinue

    $exts = $files | Group-Object Extension | Select-Object -ExpandProperty Name
    $hasPy = ($files | Where-Object { $_.Extension -eq '.py' }).Count -gt 0
    $hasCs = ($files | Where-Object { $_.Extension -eq '.cs' }).Count -gt 0
    $hasCpp = ($files | Where-Object { $_.Extension -in '.cpp', '.cxx', '.cc', '.h', '.hpp' }).Count -gt 0
    $hasJsTs = ($files | Where-Object { $_.Extension -in '.js', '.jsx', '.ts', '.tsx' }).Count -gt 0
    $hasHtml = ($files | Where-Object { $_.Extension -in '.html', '.htm' }).Count -gt 0
    $hasSql = ($files | Where-Object { $_.Extension -in '.sql', '.db', '.sqlite', '.sqlite3' }).Count -gt 0

    $packageJsonPath = Join-Path $dir.FullName 'package.json'
    $packageJson = $null
    if (Test-Path $packageJsonPath) {
        try {
            $packageJson = Get-Content $packageJsonPath -Raw | ConvertFrom-Json
        } catch {}
    }

    $reqPath = Join-Path $dir.FullName 'requirements.txt'
    $requirements = $null
    if (Test-Path $reqPath) {
        try {
            $requirements = Get-Content $reqPath | Select-Object -First 30
        } catch {}
    }

    $csprojs = $files | Where-Object { $_.Extension -eq '.csproj' } | Select-Object -ExpandProperty Name

    # 最古のファイル作成日・更新日（node_modulesや.git除く）
    $contentFiles = $files | Where-Object { $_.FullName -notmatch '\\(\.git|node_modules|\.venv|venv|bin|obj)\\' }
    $minFileDate = ($contentFiles | Measure-Object -Property CreationTime -Minimum).Minimum
    $maxFileDate = ($contentFiles | Measure-Object -Property LastWriteTime -Maximum).Maximum

    $results += [PSCustomObject]@{
        Name = $name
        DirCreation = $dir.CreationTime.ToString('yyyy-MM-dd')
        DirLastWrite = $dir.LastWriteTime.ToString('yyyy-MM-dd')
        MinFileDate = if ($minFileDate) { $minFileDate.ToString('yyyy-MM-dd') } else { '' }
        MaxFileDate = if ($maxFileDate) { $maxFileDate.ToString('yyyy-MM-dd') } else { '' }
        GitFirst = $firstCommit
        GitLast = $lastCommit
        CommitCount = $commitCount
        HasPython = $hasPy
        HasCSharp = $hasCs
        HasCpp = $hasCpp
        HasJsTs = $hasJsTs
        HasHtml = $hasHtml
        HasSql = $hasSql
        Csprojs = ($csprojs -join ', ')
        PackageDeps = if ($packageJson -and $packageJson.dependencies) { ($packageJson.dependencies.PSObject.Properties.Name -join ', ') } else { '' }
        PackageDevDeps = if ($packageJson -and $packageJson.devDependencies) { ($packageJson.devDependencies.PSObject.Properties.Name -join ', ') } else { '' }
        RequirementsSnippet = if ($requirements) { ($requirements -join '; ') } else { '' }
    }
}

$results | ConvertTo-Json -Depth 4 | Out-File -FilePath '~\.gemini\antigravity-ide\brain\a3e97f15-97b9-4139-87a9-99685f0a833b\scratch\scan_summary.json' -Encoding utf8
