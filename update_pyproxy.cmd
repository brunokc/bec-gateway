set PYPROXY_SOURCE=..\..\..\pyProxy\pyproxy
copy %PYPROXY_SOURCE%\* venv\Lib\site-packages\pyproxy /y
docker cp %PYPROXY_SOURCE%/. bectest:/usr/local/lib/python3.10/site-packages/pyproxy
docker exec -t bectest bash -c "killall python"
