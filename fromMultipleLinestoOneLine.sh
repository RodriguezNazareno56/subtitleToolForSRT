docker compose up -d
sleep 1m
for i in 01 02 03
do
	python3 main.py "Mad.Men.S01E$i.1080p.BluRay.x265-RARBG.srt" "Mad.Men.S01E$i.1080p.oneLine.srt"
done
docker compose down

## LIST FORMAT
#list=(
#'001 Introduction_en.srt'
#'002 Composition Part 1_en.srt'
#)
#
#docker compose up -d
#sleep 1m
#
#for i in "${list[@]}"
#do
#  echo ./srtOriginal/$i
#  python3 main.py "./srtOriginal/$i" "./srtDouble/$i"
#done
#
#docker compose down