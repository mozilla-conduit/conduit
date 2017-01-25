#!/bin/sh
# Build the project's static UI assets.
#
# Run this script from the root of the ui sources (where package.json is).

# 1. Yarn deletes the /build directory contents and compiles React.
yarn build

# 2. We need to include the fixtures/ subdirectory in the bundle of static
# assets, which 'yarn build' doesn't include.
cp -r src/fixtures build/