@echo off
setlocal EnableDelayedExpansion

for /l %%i in (1,1,100) do (
    if %%i lss 10 (
        set num=00%%i
    ) else if %%i lss 100 (
        set num=0%%i
    ) else (
        set num=%%i
    )
    echo. > !num!song.txt
)

endlocal

