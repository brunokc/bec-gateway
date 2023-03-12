docker cp src/. bectest:/usr/local/lib/python3.10/site-packages/bec
docker exec -t bectest bash -c "killall python"
