docker cp src/. bectest:/bec
docker exec -t bectest bash -c "killall python"
