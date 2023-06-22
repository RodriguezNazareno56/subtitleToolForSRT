docker compose up -d
sleep 1m
for i in 01 02 03
do
	python3 main.py "Mad.Men.S01E$i.1080p.BluRay.x265-RARBG.srt" "Mad.Men.S01E$i.1080p.oneLine.srt"
done
docker compose down



