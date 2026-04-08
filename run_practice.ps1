param(
    [ValidateSet("check", "explore", "image", "batch", "video", "track", "summary")]
    [string]$Step = "check",
    [string]$Source = "",
    [double]$Conf = 0.25
)

$ErrorActionPreference = "Stop"

$Scripts = Join-Path $PSScriptRoot "scripts"

switch ($Step) {
    "check" {
        & python (Join-Path $Scripts "01_check_env.py")
    }
    "explore" {
        & python (Join-Path $Scripts "02_explore_data.py")
    }
    "image" {
        if ($Source) {
            & python (Join-Path $Scripts "03_detect_image.py") --source $Source --conf $Conf
        } else {
            & python (Join-Path $Scripts "03_detect_image.py") --conf $Conf
        }
    }
    "batch" {
        & python (Join-Path $Scripts "04_detect_batch.py") --conf $Conf
    }
    "video" {
        if ($Source) {
            & python (Join-Path $Scripts "05_detect_video.py") --source $Source --conf $Conf
        } else {
            & python (Join-Path $Scripts "05_detect_video.py") --conf $Conf
        }
    }
    "track" {
        if ($Source) {
            & python (Join-Path $Scripts "05_detect_video.py") --mode track --source $Source --conf $Conf
        } else {
            & python (Join-Path $Scripts "05_detect_video.py") --mode track --conf $Conf
        }
    }
    "summary" {
        & python (Join-Path $Scripts "06_summarize_results.py")
    }
}
