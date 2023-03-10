set PYWSP_SOURCE=..\..\..\pyWSP\pywsp
copy %PYWSP_SOURCE%\* venv\Lib\site-packages\pywsp /y
docker cp %PYWSP_SOURCE%/. bectest:/usr/local/lib/python3.10/site-packages/pywsp
docker exec -t bectest bash -c "killall python"
