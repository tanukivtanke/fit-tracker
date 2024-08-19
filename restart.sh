docker stop fit-tracker
docker container rm fit-tracker
docker run -d --name fit-tracker -p 80:80 -v /root/project:/project fit-tracker
