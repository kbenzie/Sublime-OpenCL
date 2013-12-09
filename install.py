#!/usr/bin/python

import os
import shutil
import platform

# Build the archive
path = os.path.join(os.path.curdir, "C++")
shutil.make_archive(path, "zip", path)

# Build and rename the archive
archive_path = path + ".sublime-package"
os.rename(path + ".zip", archive_path)
archive_dir, archive_name = os.path.split(archive_path)
print("Created archive: " + archive_name)

# Function installs package at the install path
def install_package(package_path, install_path):
	if os.path.exists(install_path):
		print("Found: " + install_path)
		confirmation = raw_input("Install here? (yes/no): ")
		while not ("yes" in confirmation or "no" in confirmation):
			confirmation = raw_input("Try again (yes/no): ")
		if "yes" in confirmation:
			shutil.copy(package_path, install_path)
			path, filename = os.path.split(package_path)
			print("Installed: " + os.path.join(install_path, filename))
		else:
			print("Skipping: " + install_path)
			return False
		return True
	else:
		return False

# Function searches for sublime data directory the calls install_package()
def find_sublime_dir_install(config_dir, sublime_text_dir, spacer):
	if os.path.exists(config_dir):
		# Test for Sublime Text config directory
		if install_package(archive_path, os.path.join(os.path.join(config_dir, sublime_text_dir), "Installed Packages")):
			return True
		# Test for Sublime Text 2 config directory
		if install_package(archive_path, os.path.join(os.path.join(config_dir, sublime_text_dir + spacer + "2"), "Installed Packages")):
			return True
		# Test for Sublime Text 3 config directory
		if install_package(archive_path, os.path.join(os.path.join(config_dir, sublime_text_dir + spacer + "3"), "Installed Packages")):
			return True
	return False

# Determine operating system
platform_info = platform.platform()
# print(platform_info)
installed = False
if "Linux" in platform_info:
	# Determine is config directory exists and install
	installed = find_sublime_dir_install(os.path.expanduser("~/.config"), "sublime-text", "-")

elif "Windows" in platform_info:
	# Determine is config directory exists and install
	# todo testing required
	print("Windows")
	app_data_path = os.environ.get("APPDATA")
	print("APPDATA: "  + app_data_path)
	installed = find_sublime_dir_install(app_data_path, "Sublime Text", " ")

elif "OSX" in platform_info:
	# Determine is config directory exists and install
	# todo testing required
	installed = find_sublime_dir_install(os.path.expanduser("~/Library/Application Support"), "Installed Packages", " ")

if not installed:
	print(archive_name + " was not installed, please install manually")
else:
	os.remove(archive_path)
