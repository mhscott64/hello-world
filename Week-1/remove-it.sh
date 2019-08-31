source mhs-wk-1/bin/deactivate
export TARGET_DIR=mhs-wk-1
if [ -d "$TARGET_DIR" ]; then rm -Rf $TARGET_DIR; fi
export TARGET_DIR=__pycache__
if [ -d "$TARGET_DIR" ]; then rm -Rf $TARGET_DIR; fi