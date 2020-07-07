PLUGIN_DIR=$(if $(XDG_CONFIG_HOME),$(XDG_CONFIG_HOME),$(HOME)/.config)/ranger/plugins

install:
	install -Dm644 gitplug.py $(PLUGIN_DIR)/gitplug.py

uninstall:
	$(RM) $(PLUGIN_DIR)/gitplug.py
