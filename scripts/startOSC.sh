cd $PLAGIAT_SETUP_DIR/OpenStageControl
taskset -a 0x01 open-stage-control -p 3000 -l hub.json -c custom-module.js -t styles.css -s 127.0.0.1:2001 --force-gpu --disable-vsync --fullscreen
