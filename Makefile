SRC_DIR := src/
ALL_FOLDERS := $(shell find $(SRC_DIR) -mindepth 1 -maxdepth 1 -type d -print0 | xargs -0)
ALL_MODULES := $(sort $(subst $(SRC_DIR),,$(ALL_FOLDERS)))
ALL_TARGETS := ${shell bin/findtargets.py build/ $(ALL_FOLDERS)}

all: $(ALL_TARGETS)

# cleanup

.PHONY: clean show_targets
clean:
	-rm ./build/*.mkp

# debug

show_targets:
	@echo $(ALL_FOLDERS)
	@echo $(ALL_TARGETS)
	@echo $(ALL_MODULES)

# setup

define make-goal
${shell bin/findtargets.py build/ $(SRC_DIR)$1}: $(SRC_DIR)$1
	echo "Building $$@"
	bin/makemkp.py $$< ./build/
endef

$(foreach mod,$(ALL_MODULES),$(eval $(call make-goal,$(mod))))
