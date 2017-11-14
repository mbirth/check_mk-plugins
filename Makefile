ALL_FOLDERS := ${shell find ./src/ -mindepth 1 -maxdepth 1 -type d -print0 | xargs -0}
#ALL_FOLDERS := $(dir $(wildcard ./src/*/.))

#ALL_TARGETS = $(ALL_FOLDERS:./src/%=build/%.mkp)
ALL_TARGETS := ${shell bin/findtargets.py build/ $(ALL_FOLDERS)}

all: $(ALL_TARGETS)


$(ALL_TARGETS): $(ALL_FOLDERS)
	@echo "Building $@ from $<"
	bin/makemkp.py $< ./build/


# cleanup

.PHONY: clean show_targets
clean:
	-rm ./build/*.mkp

show_targets:
	@echo $(ALL_TARGETS)
