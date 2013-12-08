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

# Determine operating system
platform_info = platform.platform()
installed = False
if "Linux" in platform_info:
	# Determine is config direcotyr exists
	config_dir = os.path.expanduser("~/.config")
	if os.path.exists(config_dir):
		# Test for Sublime Text 2 condig directory
		if install_package(archive_path, os.path.join(os.path.join(config_dir, "sublime-text-2"), "Installed Packages")):
			installed = True
		# Test for Sublime Text 3 condig directory
		if install_package(archive_path, os.path.join(os.path.join(config_dir, "sublime-text-3"), "Installed Packages")):
			installed = True

elif "Windows" in platform_info:
	# Determine is config direcotyr exists
	config_dir = "%APPDATA%"
	if os.path.exists(config_dir):
		# Test for Sublime Text 2 condig directory
		if install_package(archive_path, os.path.join(os.path.join(config_dir, "Sublime Text 2"), "Installed Packages")):
			installed = True
		# Test for Sublime Text 3 condig directory
		if install_package(archive_path, os.path.join(os.path.join(config_dir, "Sublime Text 3"), "Installed Packages")):
			installed = True

elif "OSX" in platform_info:
	# Determine is config direcotyr exists
	config_dir = "~/Library/Application Support"
	if os.path.exists(config_dir):
		# Test for Sublime Text 2 condig directory
		if install_package(archive_path, os.path.join(os.path.join(config_dir, "Sublime Text 2"), "Installed Packages")):
			installed = True
		# Test for Sublime Text 3 condig directory
		if install_package(archive_path, os.path.join(os.path.join(config_dir, "Sublime Text 3"), "Installed Packages")):
			installed = True

if not installed:
	print(archive_name + " was not installed, please install manually")
else:
	os.remove(archive_path)
