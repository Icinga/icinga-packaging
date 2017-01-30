#!/usr/bin/make -f
# Run uglifyjs to 'compile' the .min.js ourself
#
# Fallback to yui-compressor if uglifyjs is not available.

SOURCE_PATH = ../../public/js/vendor
SOURCES = jquery-1.11.0.js jquery-2.1.0.js jquery.sparkline.js jquery.tipsy.js
FILES = $(patsubst %.js,%.min.js,$(SOURCES))

UGLIFY_OPTS = -m "toplevel=true" -r '$$,require,exports' -c "hoist_funs=false,loops=false,unused=false"

CAN_UGLIFYJS := $(shell command -v uglifyjs 2>/dev/null)

all: source uglify

clean:
	rm -f *.js *.map *.head

source: $(SOURCES)

uglify: $(FILES)

%.min.js: %.js
	$(eval map := $(patsubst %.min.js,%.min.map,$@))
ifdef CAN_UGLIFYJS
	uglifyjs \
	  $(UGLIFY_OPTS) \
	  -o $@ \
	  --source-map $(map) \
	  --source-map-url $(map) -- $<
	#  --preamble "$$(cat $<.head)" \
	# Add explicit newline (https://dev.icinga.org/issues/12328)
	echo >> $@
else
	yui-compressor $< -o $@
endif

%.js:
	$(eval min := $(patsubst %.js,%.min.js,$@))
	#grep -Pzo '/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/' $(SOURCE_PATH)/$(min) > $@.head
	cp $(SOURCE_PATH)/$@ .
