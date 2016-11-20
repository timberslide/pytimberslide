SRC_DIR=.
DST_DIR=.

all:
	python -m grpc.tools.protoc -I=$(SRC_DIR) --python_out=$(DST_DIR) --grpc_python_out=$(DST_DIR) $(SRC_DIR)/timberslide.proto
