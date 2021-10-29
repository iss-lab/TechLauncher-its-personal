#!/bin/sh

set -e
set -x

make
podir=`dirname $0`
find lib/ tool/ -name \*.js -or -name \*.ts > po/POTFILES
mkdir -p $podir/tmp
for f in $podir/../data/builtins/*/manifest.tt ; do
	kind=$(basename $(dirname $f))
	ts-node $podir/extract-translatable-annotations $f > $podir/tmp/$kind.js
	echo $podir/tmp/$kind.js >> po/POTFILES
done
xgettext -kN_ -c -f po/POTFILES -x po/POTFILES.skip -LJavaScript -o po/${npm_package_name}.pot --from-code UTF-8 --package-name ${npm_package_name} --package-version ${npm_package_version}
