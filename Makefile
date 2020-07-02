PLUGIN_DIR=$(if $(XDG_CONFIG_HOME),$(XDG_CONFIG_HOME),$(HOME)/.config)/ranger/plugins

install:
	install -Dm644 git-plug.py $(PLUGIN_DIR)/git-plug.py

uninstall:
	$(RM) $(PLUGIN_DIR)/git-plug.py
