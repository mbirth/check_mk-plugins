SRC_DIR := src/
ALL_FOLDERS := $(sort $(shell find $(SRC_DIR) -mindepth 1 -maxdepth 1 -type d -print0 | xargs -0))
ALL_MODULES := $(sort $(subst $(SRC_DIR),,$(ALL_FOLDERS)))
ALL_TARGETS := $(shell bin/findtargets.py build/ $(ALL_FOLDERS))

all: $(ALL_TARGETS)

# cleanup

.PHONY: clean
clean:
	-rm ./build/*.mkp

# debug

.PHONY: show_targets
show_targets:
	@echo $(ALL_FOLDERS)
	@echo $(ALL_TARGETS)
	@echo $(ALL_MODULES)

# https://stackoverflow.com/questions/4219255/how-do-you-get-the-list-of-targets-in-a-makefile
.PHONY: list
list:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | xargs

# setup

define make-targets
$(eval OUTPUT_FILE := $(shell bin/findtargets.py build/ $(SRC_DIR)$(1)))

$(OUTPUT_FILE): $(SRC_DIR)$(1) $(shell find $(SRC_DIR)$(1) -type f -print0 | xargs -0)
	@echo "Building $$@"
	@bin/makemkp.py $$< ./build/

$(1): $(OUTPUT_FILE)
endef

$(foreach mod,$(ALL_MODULES),$(eval $(call make-targets,$(mod))))
