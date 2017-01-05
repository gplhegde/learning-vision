EXE = obj-detect
OBJ_DIR = obj
CAFFE_LIB_DIR = 
CC = g++

include sources.mk

LDFLAGS = `pkg-config --libs opencv` -L$(CAFFE_LIB_DIR) -lcaffe 
INC_DIRS = -I./inc

CFLAGS =  $(INC_DIRS) $(LDFLAGS) -O3

OBJS = $(addprefix $(OBJ_DIR)/, $(notdir $(patsubst %.cpp, %.o, $(filter %.cpp, $(SRCS)))))
vpath %.cpp $(dir $(SRCS))

all: obj $(EXE)

$(exec):$(OBJS)
	@echo "Linking..."
	$(CC) -o $@ $(OBJS) $(CFLAGS) -lm

$(OBJS):$(OBJ_DIR)/%.o:%.cpp
	@echo "Building $< ..."
	$(CC) -c $(CFLAGS) $< -o $@

obj:
	mkdir -p $(OBJ_DIR)


.phony: print clean
print:
	@echo "SRCS = $(SRCS)"
	@echo "OBJS = $(OBJS)"
	@echo "INC_DIR_FLAGS = $(INC_DIRS)"
	@echo "LIB_DIR_FLAGS = $(LDFLAGS)"
	@echo "CFLAGS = $(CFLAGS)"

clean:
	rm -rf $(EXE) $(OBJ_DIR)
